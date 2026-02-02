import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Confidence Interval Calculator', layout='wide')

st.title('Confidence Interval Calculator for Z Procedure')

st.write('''
This app calculates the confidence interval for a population mean using a Z-procedure and displays a graph of the interval.
''')

with st.sidebar:
    st.header('Input Parameters')
    degrees_freedom = st.number_input('Degrees Of Freedom', value=1.0)

x = np.array([])
for i in range(0,degrees_freedom):
    x += (np.random.normal(loc=0, scale=1, size=100))**2  
    


# Display results
st.write(f'Critical Value (z-score): {z_score:.2f}')

# Plot the confidence interval
fig, ax = plt.subplots(figsize=(3, 2))

sns.kdeplot(x, clip=(x.min(),x.max()), ax=ax)

ax.set_title('Chi-Square Distribution Visualization')
ax.legend()

st.pyplot(fig)
