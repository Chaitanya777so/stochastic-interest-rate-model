import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Quant Finance Dashboard",
    layout="wide"
)

st.title(
    "Stochastic Interest Rate Modeling System"
)

st.write("""
This dashboard simulates future
interest-rate behavior using the
Vasicek stochastic model and
Monte Carlo simulation.
""")

st.sidebar.header("Simulation Parameters")

r0 = st.sidebar.slider(
    "Initial Interest Rate",
    0.0,
    10.0,
    4.0
)

a = st.sidebar.slider(
    "Mean Reversion Speed",
    0.01,
    1.0,
    0.15
)

b = st.sidebar.slider(
    "Long-Term Mean",
    0.0,
    10.0,
    5.0
)

sigma = st.sidebar.slider(
    "Volatility",
    0.01,
    2.0,
    0.3
)

st.write("Selected Parameters")

st.write("Initial Rate:", r0)
st.write("Mean Reversion:", a)
st.write("Long-Term Mean:", b)
st.write("Volatility:", sigma)