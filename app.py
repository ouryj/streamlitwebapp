import streamlit as st
import pandas as pd
import plotly_express as px

# Reading CSV file into pandas DataFrame
df = pd.read_csv('vehicles_us.csv')

# Adding a header to the app
st.header('Vehicle Dataset Dashboard')

# Creating a histogram of the price column
# Calculate the lower and upper bounds for outliers
lower_bound = df['price'].quantile(0.05)
upper_bound = df['price'].quantile(0.95)

# Checkbox for excluding outliers
exclude_outliers = st.checkbox('Exclude Outliers from Price Distribution')

if exclude_outliers:
    # Filter the DataFrame to exclude outliers
    df_filtered = df[(df['price'] >= lower_bound) & (df['price'] <= upper_bound)]
    st.write(f'Outliers excluded. Showing prices between ${lower_bound:.2f} and ${upper_bound:.2f}.')
else:
    df_filtered = df  # Use the full dataset if outliers are not excluded

# Creating a histogram of the price column
hist = px.histogram(df_filtered, x='price', title='Vehicle Price Distribution')

# Displaying the histogram with Streamlit
if st.checkbox('Show Histogram: Price Distribution'):
    st.plotly_chart(hist)

# Creating a scatter plot for price vs odometer
scatter_plot = px.scatter(df_filtered, x='price', y='odometer', title='Price Vs Mileage (Odometer)')

# Display the scatter plot
if st.checkbox('Show Scatter Plot: Price Vs Mileage'):
    st.plotly_chart(scatter_plot)

# Adding a checkbox to display the raw data table
if st.checkbox('Show Raw Data'):
    st.write(df_filtered)

# Finished now loading the app through the terminal


