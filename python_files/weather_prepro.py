import pandas as pd
import requests

def weather_df(lat:float,
              lon:float,
              start_date:str, # "YYYY-MM-DD"
              end_date:str    # "YYYY-MM-DD"
              )-> pd.DataFrame:
    """
    Given a latitude, longitude, start date, and end date, provide
    a daily dataframe of all features.
    """
    weather_url = 'https://archive-api.open-meteo.com/v1/era5'
    weather_params = {
      "latitude" : lat,
      "longitude" : lon,
      "start_date" : start_date,
      "end_date" : end_date,
      "timezone" : "Europe/Madrid",
      "daily" : ["temperature_2m_max",
                  "temperature_2m_min",
                  "precipitation_sum",
                  "rain_sum",
                  "snowfall_sum",
                  "precipitation_hours",
                  "sunrise",
                  "sunset",
                  "windspeed_10m_max",
                  "windgusts_10m_max",
                  "winddirection_10m_dominant",
                  "shortwave_radiation_sum", # ! IMPORTANT METRIC
                  "et0_fao_evapotranspiration"]
    }
    weather_data = requests.get(weather_url, params=weather_params)
    weather_dict = weather_data.json()
    weather_df = pd.DataFrame(weather_dict["daily"])
    return weather_df


def preprocess_weather_df(weather_df:pd.DataFrame) -> pd.DataFrame:
    """
    This function aggregates all the rows by summing or averaging them.
    """
    # To Datetime
    weather_df["sunrise"] = pd.to_datetime(weather_df["sunrise"])
    weather_df["sunset"] = pd.to_datetime(weather_df["sunset"])
    weather_df.drop("time", axis=1, inplace=True)

    # Aggregates
    max_temp = weather_df["temperature_2m_max"].mean()
    min_temp = weather_df["temperature_2m_min"].mean()
    prec_sum = weather_df["precipitation_sum"].sum()
    rain_sum = weather_df["rain_sum"].sum()
    snow_sum = weather_df["snowfall_sum"].sum()
    prec_hours = weather_df["precipitation_hours"].sum()
    sun_hours = (weather_df["sunset"] - weather_df["sunrise"]).mean()
    wind_speed_max = weather_df["windspeed_10m_max"].mean()
    wing_gusts_max = weather_df["windgusts_10m_max"].mean()
    wind_direction = weather_df["winddirection_10m_dominant"].mean()
    solar_radiation = weather_df["shortwave_radiation_sum"].sum()
    evapotransp = weather_df["et0_fao_evapotranspiration"].sum()

    # To DataFrame
    aggregates_list = [max_temp, min_temp, prec_sum, rain_sum, snow_sum,
                       prec_hours, sun_hours, wind_speed_max, wing_gusts_max,
                       wind_direction, solar_radiation, evapotransp]
    weather_df_agg = pd.DataFrame(aggregates_list).T
    weather_df_agg.columns = ['temperature_2m_max', 'temperature_2m_min',
                              'precipitation_sum','rain_sum', 'snowfall_sum',
                              'precipitation_hours', 'sun hours',
                              'windspeed_10m_max', 'windgusts_10m_max',
                              'winddirection_10m_dominant',
                              'shortwave_radiation_sum',
                              'et0_fao_evapotranspiration']
    return weather_df_agg
