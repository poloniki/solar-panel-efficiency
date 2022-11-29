from panels_prepro import get_dataframe_option1
from weather_prepro import weather_df, aggregates_df
import pandas as pd
import numpy as np
import time
#from sklearn.pipeline import make_pipeline
#from sklearn.preprocessing import MinMaxScaler

def unsupervised_df(df:pd.DataFrame,
                        year:int) -> pd.DataFrame:
    dict_ ={'latitude': [],
            'longitude': [],
            'year': [],
            'temperature_2m_max': [],
            'temperature_2m_min': [],
            'precipitation_sum': [],
            'rain_sum': [],
            'snowfall_sum': [],
            'precipitation_hours': [],
            'sun hours':[],
            'windspeed_10m_max':[],
            'windgusts_10m_max':[],
            'winddirection_10m_dominant':[],
            'shortwave_radiation_sum':[],
            'et0_fao_evapotranspiration':[]
            }
    loading=1
    for i, r in df.iterrows():
        try:
            print(f"💭 Computing {loading}/{df.shape[0]} row.")

            latitude = r["latitude"]
            longitude = r["longitude"]

            list_ = aggregates_df(weather_df(lat=latitude,
                                                lon=longitude,
                                                year=year))
            count = 0
            for k,v in dict_.items():
                dict_[k].append(list_[count])
                count +=1

            loading +=1
        except:
            time.sleep(5)
            continue
    return pd.DataFrame(dict_)


def supervised_df(df:pd.DataFrame,
                        year:int) -> pd.DataFrame:
    dict_ ={'latitude': [],
            'longitude': [],
            'year': [],
            'temperature_2m_max': [],
            'temperature_2m_min': [],
            'precipitation_sum': [],
            'rain_sum': [],
            'snowfall_sum': [],
            'precipitation_hours': [],
            'sun hours':[],
            'windspeed_10m_max':[],
            'windgusts_10m_max':[],
            'winddirection_10m_dominant':[],
            'shortwave_radiation_sum':[],
            'et0_fao_evapotranspiration':[],
            'production':[]
            }
    loading=1
    for i, r in df.iterrows():
        try:
            print(f"💭 Computing {loading}/{df.shape[0]} row.")

            latitude = r["latitude"]
            longitude = r["longitude"]
            target = r[-1] # Check if it works

            list_ = [latitude, longitude, year,
                     aggregates_df(weather_df(lat=latitude,
                                              lon=longitude,
                                              year=year)), target]
            print(list_)
            count = 0
            for k,v in dict_.items():
                dict_[k].append(list_[count])
                count +=1

            loading +=1
        except:
            time.sleep(5)
            continue
    return pd.DataFrame(dict_)
