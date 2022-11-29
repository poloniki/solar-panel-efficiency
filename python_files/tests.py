from weather_prepro import weather_df, aggregates_df
from panels_prepro import get_dataframe_option2
from aggregate import supervised_df
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == "__main__":
    df = get_dataframe_option2().head(20)
    print(supervised_df(df,2017))
