import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Mutual Fund Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Mutual Fund Analytics Dashboard")


fund_master = pd.read_csv("data/processed/01_fund_master_clean.csv")
scheme_perf = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
nav_history = pd.read_csv("data/processed/nav_history_clean.csv")
portfolio = pd.read_csv("data/processed/09_portfolio_holdings_clean.csv")

nav_history["date"] = pd.to_datetime(nav_history["date"])


fund_house = st.sidebar.multiselect(
    "Fund House",
    options=fund_master["fund_house"].unique(),
    default=fund_master["fund_house"].unique()
)

category = st.sidebar.multiselect(
    "Category",
    options=fund_master["category"].unique(),
    default=fund_master["category"].unique()
)

filtered_master = fund_master[
    (fund_master["fund_house"].isin(fund_house)) &
    (fund_master["category"].isin(category))
]


col1, col2, col3, col4 = st.columns(4)

col1.metric("Schemes", len(filtered_master))
col2.metric("Avg Expense Ratio",
            round(filtered_master["expense_ratio_pct"].mean(),2))

col3.metric("Fund Houses",
            filtered_master["fund_house"].nunique())

col4.metric("Categories",
            filtered_master["category"].nunique())


st.subheader("Category Distribution")

fig1 = px.pie(
    filtered_master,
    names="category",
    title="Fund Category Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

top_aum = scheme_perf.sort_values(
    "aum_crore",
    ascending=False
).head(10)

fig2 = px.bar(
    top_aum,
    x="scheme_name",
    y="aum_crore",
    color="aum_crore",
    title="Top 10 Funds by AUM"
)

st.plotly_chart(fig2, use_container_width=True)


st.subheader("Top Funds by Sharpe Ratio")

top_sharpe = scheme_perf.sort_values(
    "sharpe_ratio",
    ascending=False
).head(10)

fig3 = px.bar(
    top_sharpe,
    x="scheme_name",
    y="sharpe_ratio",
    color="sharpe_ratio"
)

st.plotly_chart(fig3, use_container_width=True)


st.subheader("Return vs Risk")

fig4 = px.scatter(
    scheme_perf,
    x="std_dev_ann_pct",
    y="return_5yr_pct",
    size="aum_crore",
    hover_name="scheme_name",
    color="category"
)

st.plotly_chart(fig4, use_container_width=True)


st.subheader("NAV Trend")

scheme = st.selectbox(
    "Select Scheme",
    nav_history["amfi_code"].unique()
)

temp = nav_history[
    nav_history["amfi_code"] == scheme
]

fig5 = px.line(
    temp,
    x="date",
    y="nav",
    title=f"NAV Trend for {scheme}"
)

st.plotly_chart(fig5, use_container_width=True)


st.subheader("Sector Allocation")

sector_data = portfolio.groupby(
    "sector"
)["weight_pct"].sum().reset_index()

fig6 = px.pie(
    sector_data,
    names="sector",
    values="weight_pct"
)

st.plotly_chart(fig6, use_container_width=True)


st.subheader("Top Holdings")

top_holdings = portfolio.groupby(
    "stock_name"
)["weight_pct"].sum().reset_index()

top_holdings = top_holdings.sort_values(
    "weight_pct",
    ascending=False
).head(15)

fig7 = px.bar(
    top_holdings,
    x="stock_name",
    y="weight_pct"
)

st.plotly_chart(fig7, use_container_width=True)


st.subheader("Scheme Performance Table")

st.dataframe(
    scheme_perf[
        ["scheme_name",
         "return_5yr_pct",
         "sharpe_ratio",
         "sortino_ratio",
         "aum_crore"]
    ]
)
