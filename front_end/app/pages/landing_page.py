import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk
from urllib.request import urlopen
import json
import plotly
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(layout="wide")

# TITLE
st.markdown("""
    # Which is the best place to set up a Solar Panel Station?
    """)

# SIDEBAR
st.sidebar.markdown("""
                    ## Incremental investment in Solar Panel Generation
                    """)

option = st.sidebar.slider('Level of solar energy production\
                compared to aggregated energy production (in %)', 5, 100, 5)


# HEADER
col1, col2, col3 = st.columns(3)
col1.metric("Solar Stations", "14", option)
col2.metric("Solar Energy produced (GWh)", "1234.5", option)
col3.metric("Non-renewable energy produced (GWh)", "67890.5", option)

data = pd.read_csv('../../Energy_Province.csv')

layer = pdk.Layer(
    'HexagonLayer',  # `type` positional argument is here
    data,
    get_position=['lon', 'lat'],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1)


# Combined all of it and render a viewport
r = pdk.Deck(layers=[layer])
r.to_html('hexagon-example.html')
st.write(r)
