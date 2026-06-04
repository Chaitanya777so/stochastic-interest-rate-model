import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:MyNewPassword123@localhost:5432/interest_rate_db"
)

print("Database connected successfully!")

df = pd.read_csv("data/raw/fedfunds.csv")

df.to_sql(
    "interest_rates",
    engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully!")