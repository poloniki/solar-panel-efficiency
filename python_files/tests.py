from weather_prepro import weather_df, preprocess_weather_df

if __name__ == "__main__":
    df = weather_df(41.3874, 2.1686, "2017-01-01", "2017-12-01")
    print(preprocess_weather_df(df))
