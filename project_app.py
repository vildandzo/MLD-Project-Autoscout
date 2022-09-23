import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import pickle
from PIL import Image
import time
from urllib.request import urlopen


st.markdown("<h2 style='text-align:center; color:Black;'>Car Price Prediction Autoscout</h2>", unsafe_allow_html=True)

#image
img = Image.open("image.jpg")
col1, col2, col3 = st.columns([1,8,1]) 
with col2:
    st.image(img,caption="Predicting the Prices of Cars",width = 500)




df = pd.read_csv("final_scout.csv")
st.markdown("## Data Show")
features = ["make_model", "hp_kW", "km","age", "Gearing_Type", "Gears","price"]
df = df[features]

if st.checkbox("To see the data, PRESS"):
     st.write(df)



st.sidebar.title("User Input Features")

def user_input_features() :
    make_model = st.sidebar.selectbox("Make Model", ("Audi A3","Audi A1","Opel Insignia", "Opel Astra", "Opel Corsa", "Renault Clio", "Renault Espace", "Renault Duster"))
    Gearing_Type = st.sidebar.selectbox("Gearing Type", ("Manual","Automatic", "Semi-automatic"))
    age = st.sidebar.number_input("Age:",min_value=0, max_value=3)
    # age = st.sidebar.selectbox("age", ("0","1", "2", "3"))
    # Gears = st.sidebar.slider("Gears", 5.0, 8.0, 5.0)
    Gears = st.sidebar.radio("Gears",(5,6,7,8))
    hp_kW = st.sidebar.slider("Horse Power(kW)", df["hp_kW"].min(), df["hp_kW"].max(), float(df["hp_kW"].median()),1.0)
    km = st.sidebar.slider("Kilometer(km)", df["km"].min(), df["km"].max(), float(df["km"].median()),1.0)
   
    
    data = {"make_model" : make_model,
            "Gearing_Type" : Gearing_Type,
            "age" : age,
            "hp_kW" : hp_kW,
            "km" : km,
            "Gears" : Gears}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.success("## Your Selection:")
st.write(input_df)

# reading the model
model = pickle.load(open("final_model_autoscout","rb"))


# button
# if st.button('Make Prediction'):
#      st.success(f'Analyze Predict:&emsp;{model.predict(input_df)[0].round(2)}')

if st.button('Make Prediction'):
    prediction = model.predict(input_df)
    st.success(f'Your Car price is:&emsp;{model.predict(input_df)[0].round(2)}')