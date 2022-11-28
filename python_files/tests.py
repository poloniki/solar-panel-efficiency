from weather_prepro import weather_df, aggregates_df
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    df = weather_df(41.3874, 2.1686, "2017-01-01", "2017-12-01")
    new_df = aggregates_df(df)
    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(new_df[['temperature_2m_max', 'temperature_2m_min',
                                'precipitation_sum',
       'rain_sum', 'snowfall_sum', 'precipitation_hours',
       'windspeed_10m_max', 'windgusts_10m_max', 'winddirection_10m_dominant',
       'shortwave_radiation_sum', 'et0_fao_evapotranspiration']])
    print(scaled_df)
