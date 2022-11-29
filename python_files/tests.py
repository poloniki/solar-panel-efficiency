from weather_prepro import weather_df, aggregates_df
from panels_prepro import get_dataframe_option3
from aggregate import df_to_model
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == "__main__":
    df = get_dataframe_option3().head(20)
    (df_to_model(df,0,supervised=True)).to_csv("allyears_supervised_df.csv")
