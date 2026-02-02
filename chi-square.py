import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Chi-Square Visualization', layout='wide')

st.title('Chi-Square Distribution Visualization')


degrees_freedom = 1
with st.sidebar:
    st.header('Input Parameters')
    degrees_freedom = st.number_input('Degrees Of Freedom', value=1)

x = (np.random.normal(loc=0, scale=1, size=100))**2
for i in range(0,degrees_freedom-1):
    x = x + (np.random.normal(loc=0, scale=1, size=100))**2  
    



fig, ax = plt.subplots(figsize=(3, 2))

sns.kdeplot(x, clip=(x.min(),x.max()), ax=ax)

st.pyplot(fig)
