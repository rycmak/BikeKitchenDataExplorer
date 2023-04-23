import streamlit as st
import pandas as pd
import intro
import total_bikes_given_year
import bikes_given_year_gender
import bike_size_dist
import age_dist
import helmet_dist

st.set_page_config(
    layout="wide",
    page_icon="favicon.png",
    page_title="Roskill Bike Kitchen",
)

# Get url where data is stored
data_url = 'https://docs.google.com/spreadsheets/d/10DHQegH0nN9Hk-WYOBlDzfsPQC1ZILiY9-l3WRvakVQ/\
gviz/tq?tqx=out:csv&sheet=Given%20out%20(cleaned)'

# Read data into dataframe
data = pd.read_csv(data_url)
data["Datetime"] = pd.to_datetime(data["Date"])
data['Year'] = data['Datetime'].dt.strftime('%Y')
data['Month'] = data['Datetime'].dt.strftime('%m')

# List of all the pages needed for dashboard
PAGES = {
    "Introduction": intro,
    "Total bikes given out per year": total_bikes_given_year,
    "Bikes given out per year by gender": bikes_given_year_gender,
    "Bike size distribution": bike_size_dist,
    "Age distribution": age_dist,
    "Do people need helmets?": helmet_dist
}

# Adding all the elements
selection = st.sidebar.radio("Explore Bike Kitchen Data", list(PAGES.keys()))
page = PAGES[selection]

# initiating the page which is picked from Radio Selection
page.app(data)