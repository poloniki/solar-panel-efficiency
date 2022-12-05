import folium
import streamlit as st
from folium.plugins import Draw

from streamlit_folium import st_folium

m = folium.Map(location=[42.6563,-5.1753], zoom_start=6)
Draw(export=True).add_to(m)

output = st_folium(m, width=1000, height=500)


bounds = output['bounds']
#st.write(output)

import requests
URL = 'https://api.ohsome.org/v1/elements/count/density'
data = {"bboxes": f"{bounds['_southWest']['lat']},{bounds['_southWest']['lng']},{bounds['_northEast']['lat']},{bounds['_northEast']['lng']}", "format": "json", "time": "2022-05-07", "filter": "landuse=industrial"}
st.write(data)

response = requests.post(URL, data=data)
st.write(response.json())
