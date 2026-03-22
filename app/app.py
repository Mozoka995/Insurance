import streamlit as st #streamlit run app/app.py
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

df=pd.read_csv('data/cleaned/cleaned_data.csv')
df.drop(columns='Unnamed: 0',inplace=True)
model=joblib.load('artifacts/randomforestpipelinemodel.pkl')

st.set_page_config('Insurance',page_icon=':book:',layout='wide')

st.header('Calculate Your Insurance Charges',text_alignment='center',width='stretch')
#st.dataframe(df)


box1,box2,box3=st.columns(3)

age=box1.slider('Age',min_value=5,max_value=70)
sex=box2.selectbox('Sex',options=df['sex'].unique())
bmi=box3.slider('BMI',min_value=15,max_value=70)

box4,box5,box6=st.columns(3)
children=box4.selectbox('No. Of Children',options=df['children'].unique())
smoker=box5.selectbox('Smoker',options=df['smoker'].unique())
region=box6.selectbox('region',options=df['region'].unique())

data=pd.DataFrame({
    'age':[age],
    'sex': [sex],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker],
    'region': [region]
})


charges_predicted=model.predict(data)

st.write( f'<h2 style = "color:green;" > {charges_predicted} </h2>', unsafe_allow_html=True )





