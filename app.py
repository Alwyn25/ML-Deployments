# Import Libraries

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pickle

import warnings
warnings.filterwarnings('ignore')

# LOAD THE INSTANCES
with open('final_model.pkl','rb') as file:
    model = pickle.load(file)
with open('scaled_model.pkl','rb') as file:
    scaling = pickle.load(file)
with open('pca_model.pkl','rb') as file:
    pca = pickle.load(file)


def prediction(input_data):
    scaled_data = scaling.transform(input_data)
    pca_data = pca.transform(scaled_data)
    prdictions = model.predict(pca_data)[0]
    if pred ==0:
        return 'Under Developed'
    elif pred==1:
        return 'Developing'
    else:
        return 'Developed'


def main():
    st.title('Help International Foundation')
    st.subheader('This application will give the status of the country based on socio-economic factors')
    child_mort = st.text_input('Enter the child_mort rate')	
    exports = st.text_input('Enter the exports %GDP')
    health = st.text_input('Enter the Expenditure on health, Total health spending per capita. Given as %age of GDP per capita')
    imports = st.text_input('Enter the imports  %GDP, Imports of goods and services per capita. Given as %age of the GDP per capita')
    income = st.text_input('Enter the averae income per person, Net income per person')
    inflation = st.text_input('Enter the inflation, The measurement of the annual growth rate of the Total GDP')
    life_expec = st.text_input('Enter the life_expec rate,The average number of years a new born child would live if the current mortality patterns are to remain the same')
    total_fer = st.text_input('Enter the total_fer rate, The number of children that would be born to each woman if the current age-fertility rates remain the same.')
    gdpp = st.text_input('Enter the gdpp, The GDP per capita. Calculated as the Total GDP divided by the total population.')

    input_list = ['child_mort','exports','health','imports','income','inflation','life_expec','total_fer','gdpp']

    if st.button('Predict'):
        response = prediction(input_data=input_list)
        st.success(response)

if __name__ == '__main__':
    main()
