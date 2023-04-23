import streamlit as st
import pandas as pd
import altair as alt

def app(data):
  bike_size_dist_chart = (
    alt.Chart(data)
    .mark_bar(color='blue', opacity=0.8)
    .encode(
      x=alt.X('Bike Size:N', 
              axis=alt.Axis(labelAngle=-20), 
              sort=["Small", "Medium", "Large", "Unspecified"]),
      y=alt.Y("count(Bike Size):O", 
              axis=alt.Axis(title="Number of bikes given out", titlePadding=10)),
    )
    .properties(title="Distribution of Bike Sizes", height=600, width=800)
    .configure_title(fontSize=30, anchor="middle")
    .configure_axis(labelFontSize=20, titleFontSize=20, titlePadding=20)
  )

  st.altair_chart(bike_size_dist_chart, use_container_width=True)
