import quandl
import pandas as pd

quandl.ApiConfig.api_key = "KQmy_Miw-rVLxRzXxHai"

df = quandl.get("WIKI/AMZN")
df = df[["Adj. Close"]]

print(df.head())