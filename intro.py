import streamlit as st

def app(data):
  st.image("bike_kitchen_logo.jpg", use_column_width=True)
  st.subheader("Bike Kitchen Data")
    
  st.markdown('<p style="font-family:sans-serif; font-size: 20px;">\
                Bike Kitchen is a non-profit focused on fixing and giving bikes \
                to those in our community who need one.\
              </p>', unsafe_allow_html=True)

  st.markdown('<p style="font-family:sans-serif; font-size: 20px;">\
                Please use the navigation on the left to explore our data.\
              </p>', unsafe_allow_html=True)

  st.markdown('<p style="font-family:sans-serif; font-size: 20px;">\
                Happy exploring!\
              </p>', unsafe_allow_html=True)
                 