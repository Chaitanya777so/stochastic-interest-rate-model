# Stochastic Interest Rate Modelling and Prediction

## Project Overview

Interest rates play a critical role in financial markets, influencing investment decisions, lending activities, and economic policy. This project analyzes historical Federal Funds Rate data and develops forecasting models using both stochastic finance techniques and machine learning approaches.

The objective is to understand the behavior of interest rates, model their dynamics mathematically, and compare traditional financial models with modern data-driven forecasting methods.

---

## Problem Statement

Predicting future interest rates is a challenging task due to market uncertainty, economic events, and changing monetary policies. Financial institutions and investors require reliable models to estimate future rate movements and manage risk effectively.

This project investigates whether stochastic models and machine learning algorithms can capture interest-rate behavior and generate meaningful forecasts.

---

## Dataset

**Source:** Federal Reserve Economic Data (FRED)

**Variable Used:** Federal Funds Effective Rate (FEDFUNDS)

**Time Period:** 1954 – Present

The dataset contains historical observations of the U.S. Federal Funds Rate and serves as the foundation for all analysis, modeling, and visualization.

---

## Project Objectives

- Analyze historical Federal Funds Rate trends
- Perform exploratory data analysis (EDA)
- Engineer meaningful financial features
- Estimate Vasicek model parameters
- Implement the Cox-Ingersoll-Ross (CIR) model
- Build machine learning forecasting models
- Compare forecasting performance across models
- Create interactive Power BI dashboards for visualization

---

## Technologies Used

### Programming & Data Analysis
- Python
- Pandas
- NumPy

### Machine Learning
- Scikit-Learn
- Linear Regression
- Random Forest

### Database
- PostgreSQL
- SQL

### Visualization
- Power BI

### Version Control
- Git
- GitHub

---

## Methodology

### 1. Data Collection and Preprocessing

The historical Federal Funds Rate dataset was cleaned and transformed to ensure consistency and usability for modeling.

Tasks performed:

- Missing value handling
- Date formatting
- Feature engineering
- Creation of lag variables
- Rolling statistics calculation

---

### 2. Stochastic Interest Rate Models

#### Vasicek Model

The Vasicek model assumes that interest rates exhibit mean-reverting behavior and tend to move toward a long-term equilibrium level.

Key benefits:

- Simple mathematical formulation
- Captures mean reversion
- Widely used in fixed-income markets

#### CIR Model

The Cox-Ingersoll-Ross (CIR) model extends the Vasicek framework by ensuring non-negative interest rates.

Key benefits:

- Realistic rate behavior
- Suitable for bond pricing
- Popular in quantitative finance

---

### 3. Machine Learning Models

#### Linear Regression

A baseline predictive model used to establish benchmark forecasting performance.

#### Random Forest

An ensemble machine learning algorithm capable of capturing nonlinear relationships within interest-rate data.

Advantages:

- Robust performance
- Handles complex interactions
- Reduced overfitting risk

---

## Results and Findings

### Historical Analysis

- Interest rates exhibit strong cyclical behavior.
- Significant volatility occurred during major economic events.
- Long periods of low rates followed financial crises and economic slowdowns.

### Model Insights

- Both Vasicek and CIR models successfully captured mean-reverting characteristics.
- Machine learning models provided stronger predictive performance.
- Random Forest achieved the lowest prediction error among tested models.

### Forecasting Performance

The comparison indicates that data-driven machine learning approaches can outperform classical stochastic models when sufficient historical information is available.

---

## Dashboard Components

The Power BI dashboard includes:

### Historical Interest Rate Trend
Visualizes the evolution of Federal Funds Rates from 1954 to the present.

### Annual Average Interest Rate
Shows yearly average interest-rate behavior.

### Volatility Analysis
Highlights periods of increased economic uncertainty and market instability.

### Model Comparison
Compares forecasting performance using RMSE metrics.

### KPI Cards
- Current Interest Rate
- Current Volatility

---

## Key Conclusions

- Federal Funds Rates demonstrate long-term mean-reverting behavior.
- Stochastic models provide valuable theoretical insights into rate dynamics.
- Machine learning techniques improve predictive accuracy.
- Random Forest produced the strongest forecasting performance among tested models.
- Interactive dashboards enhance financial data interpretation and decision-making.

---

## Future Improvements

Potential extensions of this project include:

- XGBoost forecasting models
- LSTM deep learning networks
- Monte Carlo interest-rate simulations
- Real-time FRED API integration
- Advanced bond pricing applications

---

## Author

**Chaitanya Sonowal**

Integrated B.Tech in Geophysical Technology  
Indian Institute of Technology (IIT) Roorkee

---

## Repository Structure

```text
data/
notebooks/
src/
sql/
report/
dashboard/
README.md
requirements.txt
```

---

## Project Status

✅ Completed

This project successfully combines quantitative finance, machine learning, data engineering, SQL, and business intelligence techniques to analyze and forecast interest-rate behavior.
