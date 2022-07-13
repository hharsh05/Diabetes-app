import streamlit as st
import pandas as pd
import pickle
null=None
# Title
st.header("Streamlit Machine Learning App")

# Input bar 1
MentalHealth = st.number_input("Enter Mental Health Score")

# Input bar 2
BMI = st.number_input("Enter BMI")


# If button is pressed
if st.button("Submit"):

    # Unpickle classifier
    clf = pickle.load("clf.pkl",'rb')

    # Store inputs into dataframe
    x = pd.DataFrame([[MentalHealth,BMI]],
                     columns = ["MentalHealth","BMI"])
    # Get prediction
    prediction = clf.predict(x)[0]

    # Output prediction
    st.text(f"This instance is a {prediction}")
