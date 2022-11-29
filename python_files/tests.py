from weather_prepro import weather_df, aggregates_df
from panels_prepro import get_dataframe_option2
from aggregate import df_to_model
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == "__main__":
    df = get_dataframe_option2()
    (df_to_model(df,2017,supervised=True)).to_csv("2017_supervised_df.csv")
