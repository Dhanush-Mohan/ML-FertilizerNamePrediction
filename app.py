import streamlit as st
import pickle
import numpy as np
import pandas as pd
model = pickle.load(
    open('FertilizerFinal.pickle', 'rb'))


def predict_name(Temperature, Humidity, Moisture, SoilType, CropType, Nitrogen, Potassium, Phosphorous):
    df = pd.read_csv('Fertilizer Prediction.csv')
    df.drop('Fertilizer Name', axis=1, inplace=True)
    ctremap = {"Sugarcane": 0, "Cotton": 1, "Millets": 2, "Paddy": 3, "Pulses": 4,
               "Wheat": 5, "Tobacco": 6, "Barley": 7, "Oil seeds": 8, "Ground Nuts": 9, "Maize": 10}
    stremap = {"Loamy": 0, "Sandy": 1, "Clayey": 2, "Black": 3, "Red": 4}
    st2 = stremap[SoilType]
    ct2 = ctremap[CropType]

    input = pd.DataFrame({'Temparature': [Temperature], 'Humidity': [Humidity], 'Moisture': [Moisture], 'Soil Type': [st2], 'Crop Type': [ct2],
                          'Nitrogen': [Nitrogen], 'Potassium': [Potassium], 'Phosphorous': [Phosphorous]})

    res1 = model.predict(input)[0]

    return res1


def main():
    st.title("Fertilizer Name Prediction")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Fertilizer Name Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    Temperature = st.number_input("Temperature", 0, 50, 1)
    Humidity = st.number_input("Humidity", 0, 100, 1)
    Moisture = st.number_input("Moisture", 0, 100, 1)
    SoilType = st.text_input("SoilType", "Type Here")
    CropType = st.text_input("CropType", "Type Here")
    Nitrogen = st.number_input("Nitrogen", 0, 100, 1)
    Potassium = st.number_input("Potassium", 0, 100, 1)
    Phosphorous = st.number_input("Phosphorous", 0, 100, 1)
    if st.button("Predict"):
        output = predict_name(Temperature, Humidity, Moisture,
                              SoilType, CropType, Nitrogen, Potassium, Phosphorous)
        st.success(f"The name of the fertilizer is: {output}")


if __name__ == '__main__':
    main()
