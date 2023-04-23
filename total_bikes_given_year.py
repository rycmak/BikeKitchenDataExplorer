import streamlit as st
import pandas as pd
import altair as alt

def app(data):
  bikes_given_per_year_chart = (
    alt.Chart(data[data["Year"].notna()])
    .mark_bar(color='blue', opacity=0.8)
    .encode(
      x=alt.X('Year:O', axis=alt.Axis(labelAngle=-20)),
      y=alt.Y("count(Year):O", axis=alt.Axis(title="Number of bikes given out", titlePadding=10)),
    )
    .properties(title="Total Number of Bikes Given Out Per Year", height=600, width=800)
    .configure_title(fontSize=30, anchor="middle")
    .configure_axis(labelFontSize=20, titleFontSize=20, titlePadding=20)
  )

  st.altair_chart(bikes_given_per_year_chart, use_container_width=False)
