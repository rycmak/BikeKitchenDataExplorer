import streamlit as st

def app(data):
  st.image("bike_kitchen_logo.jpg", use_column_width=True)
  st.title("Bike Kitchen Data")
    
  st.subheader("Bike Kitchen is a non-profit focused on fixing and giving bikes \
                 to those in our community who need one.")
                 
  st.subheader("Please use the navigation on the left to explore our data.")

  st.subheader("Happy exploring!")