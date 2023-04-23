import streamlit as st
import pandas as pd
import altair as alt

def app(data):
  age_dist_chart = (
    alt.Chart(data)
    .mark_bar(color='red', opacity=0.8)
    .encode(
      x=alt.X('Age:N', 
              axis=alt.Axis(labelAngle=-20), 
              sort=["Child", "Youth", "Adult", "Unspecified"]),
      y=alt.Y("count(Age):O", 
              axis=alt.Axis(title="Number of bikes given out", titlePadding=10)),
    )
    .properties(title="Distribution of Ages", height=600, width=800)
    .configure_title(fontSize=30, anchor="middle")
    .configure_axis(labelFontSize=20, titleFontSize=20)
  )

  st.altair_chart(age_dist_chart, use_container_width=True)
