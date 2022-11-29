from weather_prepro import weather_df, aggregates_df
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    df = weather_df(41.3874, 2.1686, "2017-01-01", "2017-12-01")
    new_df = aggregates_df(df)
    print(new_df)
