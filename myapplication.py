import streamlit as st
import pandas as pd
import joblib
null=None
# Title
st.header("Diabetes Checker app")
st.write("This app is intended to check wheather you are suffering from diabetes or not")
st.write("score 0 means you are not diabetic and 1 means you are diabetic")
st.text("Created by Mr.Harshit Harsh")


# Input bar 1
MentalHealth = st.number_input("Enter Mental Health Score in Range 0-30")

# Input bar 2
BMI = st.number_input("Enter BMI, BMI = Weight(Kg)/(Height*Height(metre squared))")


# If button is pressed
if st.button("Submit"):

    # Unpickle classifier
    clf = joblib.load("clf.pkl")

    # Store inputs into dataframe
    x = pd.DataFrame([[MentalHealth,BMI]],
                     columns = ["MentalHealth","BMI"])
    # Get prediction
    prediction = clf.predict(x)[0]

    # Output prediction
    st.text(f"This instance is a {prediction}")
   st.text("Created by Mr.Harshit Harsh")
