import streamlit as st
import pandas as pd
import pickle

st.image("http://www.ehtp.ac.ma/images/lo.png")
st.write("""
# MSDE4 : ML Project
## Price house Prediction App

This app predicts the **Price house** 
""")

st.sidebar.image("/Users/mehdi/Documents/téléchargement.jpeg",width=300)

st.sidebar.header('User Input Parameters')

option = st.selectbox(
     'How would you like to use the prediction model?',
     ('','House Prediction real-time', 'House Prediction Model'))

def user_input_features():
    OldNew = st.number_input("OldNew",min_value=0.0,max_value=1.0,format='%f',step=1.0)
    County = st.number_input("County",value=0.0,format='%f',step=1.0)
    latitude = st.number_input("latitude",value=0.0,format='%f',step=1.0) 
    longitude = st.number_input("longitude",value=0.0,format='%f',step=1.0)  
    Month = st.number_input("Month",min_value=1.0,max_value=12.0,format='%f',step=1.0) 
    Property_Type_is__D = st.sidebar.slider('Property_Type_is__D', 0.0, 1.0)
    Property_Type_is__F = st.sidebar.slider('Property_Type_is__F', 0.0, 1.0)
    Property_Type_is__S = st.sidebar.slider('Property_Type_is__S', 0.0, 1.0)
    Property_Type_is__T = st.sidebar.slider('Property_Type_is__T', 0.0, 1.0)
 
        
    data = {'OldNew': OldNew,
            'County': County,
            'latitude': latitude,
            'longitude': longitude,
            'Month': Month,
            'Property_Type_is__D': Property_Type_is__D,
            'Property_Type_is__F': Property_Type_is__F,
            'Property_Type_is__S': Property_Type_is__S,
            'Property_Type_is__T': Property_Type_is__T
                      }
    features = pd.DataFrame(data, index=[0])
    return features


def show_results():
    st.subheader(" Input parameters")
    st.write(cred)
    model_cred = pickle.load(open("/Users/mehdi/Documents/model_Bagg_Price.pkl", "rb"))
    prediction = model_cred.predict(cred)
    st.subheader("Prediction")
    st.write(prediction)



if option=='House Prediction real-time':
    st.sidebar.header('User Input Parameters')
    cred = user_input_features()
    show_results()


if option=='House Prediction Model':
    
    uploaded_file = st.file_uploader("Choose a file to load")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)

        model_loan=pickle.load(open("/Users/mehdi/Documents/model_Bagg_Price.pkl", "rb"))

        if st.button('Predict'):
            prediction = model_loan.predict(df)
            df["Prediction"] = prediction
            st.balloons()
            st.write(df)
    else:
        st.error("please try some prediction, then the data will be available here")
        
        