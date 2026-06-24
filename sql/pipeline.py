"""
run_pipeline.py

Master pipeline for Mutual Fund Analytics Project


"""

import pandas as pd
import numpy as np

print("Loading datasets...")


fund_master = pd.read_csv("data/processed/01_fund_master_clean.csv")
scheme_perf = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
nav_history = pd.read_csv("data/processed/nav_history_clean.csv")
portfolio = pd.read_csv("data/processed/09_portfolio_holdings_clean.csv")
txn = pd.read_csv("data/processed/08_investor_transactions_clean.csv")

nav_history["date"] = pd.to_datetime(nav_history["date"])
txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

print("Datasets loaded successfully.")



print("Computing daily returns...")

nav_history = nav_history.sort_values(
    ["amfi_code", "date"]
)

nav_history["daily_return"] = (
    nav_history
    .groupby("amfi_code")["nav"]
    .pct_change()
)


print("Computing VaR and CVaR...")

var_cvar = []

for scheme in nav_history["amfi_code"].unique():

    r = nav_history[
        nav_history["amfi_code"] == scheme
    ]["daily_return"].dropna()

    if len(r) > 0:

        var95 = np.percentile(r, 5)

        cvar95 = r[r <= var95].mean()

        var_cvar.append(
            [scheme, var95, cvar95]
        )

var_cvar_df = pd.DataFrame(
    var_cvar,
    columns=["amfi_code", "VaR_95", "CVaR_95"]
)

var_cvar_df.to_csv(
    "reports/var_cvar_report.csv",
    index=False
)

print("VaR report saved.")

print("Running cohort analysis...")

txn["year"] = txn["transaction_date"].dt.year

first_year = txn.groupby(
    "investor_id"
)["year"].min()

txn["cohort"] = txn["investor_id"].map(first_year)

cohort_summary = txn.groupby("cohort").agg(
    avg_sip_amount=("amount", "mean"),
    total_invested=("amount", "sum")
)

cohort_summary.to_csv(
    "reports/cohort_summary.csv"
)

print("Cohort analysis completed.")


print("Analyzing SIP continuity...")

sip_txn = txn[
    txn["transaction_type"] == "SIP"
].copy()

sip_txn = sip_txn.sort_values(
    ["investor_id", "transaction_date"]
)

sip_txn["gap"] = (
    sip_txn.groupby("investor_id")
    ["transaction_date"]
    .diff()
    .dt.days
)

gap_df = (
    sip_txn.groupby("investor_id")
    .agg(
        avg_gap=("gap", "mean"),
        count_txn=("gap", "count")
    )
)

gap_df = gap_df[
    gap_df["count_txn"] >= 6
]

gap_df["risk_flag"] = np.where(
    gap_df["avg_gap"] > 35,
    "At Risk",
    "Healthy"
)

gap_df.to_csv(
    "reports/sip_continuity.csv"
)

print("SIP continuity report saved.")



print("Calculating HHI concentration...")

portfolio["weight_sq"] = (
    portfolio["weight_pct"] / 100
) ** 2

hhi = portfolio.groupby(
    "amfi_code"
)["weight_sq"].sum()

hhi = hhi.reset_index()

hhi.columns = ["amfi_code", "HHI"]

hhi.to_csv(
    "reports/hhi_concentration.csv",
    index=False
)

print("HHI report saved.")


top_sharpe = (
    scheme_perf.sort_values(
        "sharpe_ratio",
        ascending=False
    )
)

top_sharpe.head(10).to_csv(
    "reports/top_sharpe_funds.csv",
    index=False
)

print("Top Sharpe report saved.")



print("="*40)
print("PIPELINE EXECUTED SUCCESSFULLY")
print("="*40)

print("Generated Files:")
print("✔ var_cvar_report.csv")
print("✔ cohort_summary.csv")
print("✔ sip_continuity.csv")
print("✔ hhi_concentration.csv")
print("✔ top_sharpe_funds.csv")
