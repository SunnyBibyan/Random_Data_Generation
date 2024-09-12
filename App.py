
# Import Libraries

import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt



# Streamlit App title

st.title("Random Data Generation and Analysis")

# User Input for Number of Data Points
st.sidebar.title("Data Points")
n_samples = st.sidebar.slider('Number of Data Points', 100, 5000, 1000)


# Generate Random Data


#  Column 1: Normal distribution (Gaussian)
mean1, std_dev1 = 100, 15
column1 = np.random.normal(loc=mean1, scale=std_dev1, size=n_samples)

#  Column 2: Uniform distribution 
column2 = np.random.uniform(low=10, high=50, size=n_samples)

# Column 3: Exponential distribution
column3 = np.random.exponential(scale=2.0, size=n_samples)

# Column 4: Random integers between 0 and 100
column4 = np.random.randint(low=0, high=100, size=n_samples)

# Column 5: Binomial distribution
n, p = 10, 0.5
column5 = np.random.binomial(n=n, p=p, size=n_samples)


# 3. Create a DataFrame

data_df = pd.DataFrame({
    'Normal Distribution': column1,
    'Uniform Distribution': column2,
    'Exponential Distribution': column3,
    'Random Integers': column4,
    'Binomial Distribution': column5
})


# Create Descriptive Statistics
st.subheader("Descriptive Statistics")
st.write(data_df.describe())


# Data Visualization
st.subheader("Data Visualizations")
plot_column = st.selectbox("Select column to visualize", data_df.columns)

fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data_df[plot_column], bins=30, kde=True, color='blue', ax=ax)
ax.set_title(f'Histogram of {plot_column}')

st.pyplot(fig)


# convert the DataFrame to a CSV
@st.cache_data 
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(data_df)


# CSV Download
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='simulated_data.csv',
    mime='text/csv'
)