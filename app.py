import streamlit as st
import pandas as pd
import plotly_express as px

#Reading csb file into pandas dataframe
df = pd.read_csv('vehicles_us.csv')
# adding a header to the app
st.header('Vehicle Dataset Dashboard')

#creating a histogram of the price column
hist = px.histogram(df, x='price', title='Vehicle Price Distribution')

# displaying the histogram with streamlit
st.plotly_chart(hist)

# creating a scatter plot for price vs odometer
scatter_plot = px.scatter(df,x='price', y='odometer', title='Price Vs Mileage (Odometer)')

#Display the scatter plot
st.plotly_chart(scatter_plot)
# adding a checkbox to toggle the scatter plot
if st.checkbox('Show Scatter Plot: Price Vs Mileage'):
    st.plotly_chart(scatter_plot)

#adding a checkbox to toggle the histogram
if st.checkbox('Show Histogram: Price Distribution'):
    st.plotly_chart(hist)

#finished now loading the app through the terminal


