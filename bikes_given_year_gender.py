import streamlit as st
import pandas as pd
import altair as alt

def app(data):
  selection = alt.selection_multi(fields=['Gender'], bind='legend')

  bikes_given_per_year_by_gender_chart = (
    alt.Chart(data[data["Year"].notna()])
    .mark_bar()
    .encode(
      alt.Facet('Year'),
      column=alt.Column("Year:O", header=alt.Header(
        title=None, labelOrient="bottom", labelPadding=10, labelFontSize=20)),
      x=alt.X('Gender', axis=None),
      y=alt.Y("count(Year):O", axis=alt.Axis(title="Number of bikes given out", titlePadding=10)),
      color=alt.Color("Gender"),
      opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
    )
    .properties(title="Number of Bikes Given Out Per Year by Gender", height=350, width=100)
    .configure_view(stroke='transparent')
    .configure_scale(bandPaddingInner=0, bandPaddingOuter=0.1)
    .configure_facet(spacing=5)
    .configure_title(fontSize=30, anchor="middle")
    .configure_axis(labelFontSize=20, titleFontSize=20, titlePadding=20)
    .configure_legend(titleFontSize=20, labelFontSize=20)
    .add_selection(selection)
  )

  st.altair_chart(bikes_given_per_year_by_gender_chart, use_container_width=False)
