import streamlit as st
import pandas as pd
import numpy as np

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

# BODY | MAP
map_data = pd.read_csv("../../raw_data/listado-longitud-latitud-municipios-espana.csv")

st.map(map_data)
