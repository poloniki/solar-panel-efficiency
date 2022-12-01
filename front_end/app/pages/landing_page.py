import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk


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

# ST.MAP
#map_data = pd.read_csv("../../raw_data/listado-longitud-latitud-municipios-espana.csv")
solar_stations = pd.read_csv("../../raw_data/Spain_energy_df_2017.csv")
map_solar_stations = solar_stations[solar_stations["primary_fuel"]=="Solar"]

st.map(map_solar_stations)


# PYDECK

layer2 = pdk.Layer(
            'ScatterplotLayer',
            map_solar_stations,
            get_position=['lon', 'lat'],
            auto_highlight=True,
            get_color='[200, 30, 0, 160]',
            get_radius=10000)

layer = pdk.Layer(
    'HexagonLayer',  # `type` positional argument is here
    map_solar_stations,
    get_position=['lon','lat'],
    auto_highlight=True,
    elevation_scale=50,
    radius=10000,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1)

view_state = pdk.ViewState(
        longitude=-3.7038,
        latitude=40.4168,
        zoom=6,
        min_zoom=5,
        max_zoom=15,
        pitch=40.5,
        bearing=-27.36)

r = pdk.Deck(layers=[layer,layer2], initial_view_state=view_state)
st.pydeck_chart(r)

# PLOTLY

fig = px.scatter_geo(map_solar_stations,lat='lat',lon='lon',
                     color="estimated_generation_gwh_2017",
                     template="simple_white",
                     color_continuous_scale=px.colors.sequential.Greens
                     )
fig.update_geos(
    center=dict(lon=-3.7038, lat=40.4168),
    lataxis_range=[1,7], lonaxis_range=[35, 45],
    visible=False, resolution=50, scope="europe",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="White",
    showframe=False, showland=True,
)

fig.update_traces(marker=dict(size=12,
                              line=dict(width=1,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))


st.plotly_chart(fig)
