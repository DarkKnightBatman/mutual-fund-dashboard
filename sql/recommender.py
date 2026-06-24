"""
recommender.py

Simple Mutual Fund Recommendation System

Input:
    Risk Appetite (Low / Moderate / High)

Output:
    Top 3 funds ranked by Sharpe Ratio
"""

import pandas as pd


scheme_perf = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

fund_master = pd.read_csv(
    "data/processed/01_fund_master_clean.csv"
)


df = pd.merge(
    scheme_perf,
    fund_master[
        [
            "amfi_code",
            "scheme_name",
            "risk_category",
            "category",
            "fund_house"
        ]
    ],
    on="amfi_code",
    how="left"
)


df["risk_category"] = (
    df["risk_category"]
    .astype(str)
    .str.lower()
)


risk = input(
    "\nEnter Risk Appetite (Low / Moderate / High): "
).lower()


if risk == "low":
    filtered = df[
        df["risk_category"].str.contains(
            "low|conservative",
            case=False,
            na=False
        )
    ]

elif risk == "moderate":
    filtered = df[
        df["risk_category"].str.contains(
            "moderate",
            case=False,
            na=False
        )
    ]

elif risk == "high":
    filtered = df[
        df["risk_category"].str.contains(
            "high|very high",
            case=False,
            na=False
        )
    ]

else:
    print("Invalid input!")
    exit()

recommendations = (
    filtered
    .sort_values(
        by="sharpe_ratio",
        ascending=False
    )
    .head(3)
)


print("\n==============================")
print("Recommended Funds")
print("==============================")

print(
    recommendations[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_category",
            "sharpe_ratio",
            "return_5yr_pct",
            "aum_crore"
        ]
    ]
)


recommendations.to_csv(
    "reports/recommended_funds.csv",
    index=False
)

print("\nRecommendations saved to:")
print("reports/recommended_funds.csv")
