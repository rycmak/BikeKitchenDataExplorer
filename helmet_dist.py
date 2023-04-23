import streamlit as st
import pandas as pd
import altair as alt

def app(data):
  age_dist_chart = (
    alt.Chart(data)
    .mark_bar(color='green', opacity=0.8)
    .encode(
      x=alt.X('Helmet Supplied:N', 
              axis=alt.Axis(labelAngle=-20), 
              sort=["Yes", "No"]),
      y=alt.Y("count(Helmet Supplied):O", 
              axis=alt.Axis(title="Number of people", titlePadding=10)),
    )
    .properties(title="How many people needed helmets?", height=600, width=800)
    .configure_title(fontSize=30, anchor="middle")
    .configure_axis(labelFontSize=20, titleFontSize=20, titlePadding=20)
  )

  st.altair_chart(age_dist_chart, use_container_width=True)
