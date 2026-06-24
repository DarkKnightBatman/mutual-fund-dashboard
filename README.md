# 📈 Mutual Fund Dashboard & Analytics

A complete end-to-end Mutual Fund Analytics project built using **Python, SQL, Pandas, Jupyter Notebook, and Power BI**. The project performs ETL, exploratory data analysis, advanced risk metrics, and interactive dashboarding for Indian mutual fund schemes.

---

# 🚀 Project Objective

To analyze mutual fund performance, portfolio allocation, investor behavior, and risk metrics using real-world datasets and create an interactive dashboard for insights and decision-making.

---

# 📂 Project Structure

```
mutual-fund-dashboard/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── Advanced_Analytics.ipynb
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│
│
├── sql/
│   ├── schema.sql
│  
│
├── run_pipeline.py
├── recommender.py
├── requirements.txt
└── README.md
```

---

# 📊 Datasets Used

### 1. Fund Master

Contains scheme details, category, expense ratio, benchmark, fund house etc.

### 2. NAV History

Daily NAV values from 2022–2026.

### 3. Scheme Performance

Return metrics, Sharpe ratio, Sortino ratio, alpha, beta and risk statistics.

### 4. Portfolio Holdings

Stock holdings and sector allocation.

### 5. Investor Transactions

SIP, redemption and lumpsum transactions.

### 6. AUM Data

Assets Under Management of schemes.

### 7. Benchmark Data

### 8. Calendar Table

---

# ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Plotly
* Scikit-learn
* SQL
* SQLite
* Jupyter Notebook
* Power BI
* Git & GitHub

---

# 🔄 ETL Pipeline

### Data Cleaning

* Removed duplicates
* Parsed date columns
* Handled missing values
* Standardized column names
* Converted numeric columns

### Feature Engineering

* Daily Returns
* Rolling Sharpe Ratio
* Historical VaR (95%)
* CVaR (95%)
* Investor Cohorts
* Sector HHI Concentration

---

# 📈 Exploratory Data Analysis

Performed:

* NAV trend analysis
* Fund category distribution
* Sector allocation analysis
* Portfolio concentration study
* Top holdings analysis
* Fund performance comparison

---

# 📉 Advanced Analytics

## Historical VaR and CVaR

Computed 95% Value at Risk and Conditional VaR for all schemes.

---

## Rolling 90-Day Sharpe Ratio

```
Sharpe = Mean(Returns)/Std(Returns) × √252
```

Tracked risk-adjusted performance for top funds.

---

## Investor Cohort Analysis

Grouped investors based on their first transaction year and analyzed:

* Average SIP amount
* Total investment
* Preferred schemes

---

## SIP Continuity Analysis

Flagged investors with gaps greater than 35 days as "At Risk".

---

## Fund Recommendation System

Risk levels:

* Low
* Moderate
* High

Returns top 3 schemes based on Sharpe ratio.

---

## Sector HHI Concentration

Measured portfolio diversification using:

```
HHI = Σ(weight²)
```

Higher HHI indicates concentrated portfolios.

---

# 📊 Power BI Dashboard

## Page 1: Industry Overview

* Total AUM
* Number of Schemes
* Category Distribution
* NAV Trend
* Fund House Distribution

---

## Page 2: Performance Analytics

* Sharpe Ratio
* Sortino Ratio
* Return Comparison
* Alpha vs Beta Scatter Plot
* Risk vs Return

---

## Page 3: Portfolio Analytics

* Sector Allocation
* Top Holdings
* Stock Weight Distribution

---

## Page 4: NAV Analytics

* NAV Trend Over Time
* Top Schemes by NAV
* Year-wise NAV Trend

---

## KPI Cards

* Total Schemes
* Average Expense Ratio
* Average AUM
* Total NAV

---

# 📁 Deliverables

✔ Advanced_Analytics.ipynb

✔ var_cvar_report.csv

✔ rolling_sharpe_chart.png

✔ recommender.py

✔ bluestock_mf_dashboard.pbix

✔ Dashboard.pdf

✔ Final_Report.pdf

✔ Bluestock_MF_Presentation.pptx

---

# ▶ Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run ETL:

```bash
python run_pipeline.py
```

Run analytics notebook:

```bash
jupyter notebook
```

Open:

```
Advanced_Analytics.ipynb
```

Launch dashboard:

```
bluestock_mf_dashboard.pbix
```

---

# 📌 Key Insights

* Small-cap funds generated the highest returns.
* Sharpe ratio identified top risk-adjusted performers.
* Some portfolios were highly concentrated according to HHI.
* SIP continuity helped identify at-risk investors.
* Historical VaR highlighted downside risk among schemes.

---


---

# ⭐ Future Improvements

* Live NAV API Integration
* Fund Recommendation Web App
* Streamlit Dashboard
* Portfolio Optimizer
* Forecasting using LSTM

