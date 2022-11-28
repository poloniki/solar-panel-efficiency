from preprocess import get_dataframe_option1
from weather_prepro import weather_df, aggregates_df
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler


df = get_dataframe_option1()

scaler = MinMaxScaler()
scaler.fit(weather_df.loc[:, df.columns != 'sun hours']])
