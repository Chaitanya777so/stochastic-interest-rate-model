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
