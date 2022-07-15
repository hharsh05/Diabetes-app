import streamlit as st
import pandas as pd
import joblib
from PIL import Image
null=None
def load_images(file_name):
    img = Image.open(file_name)
    return st.image(img,width=300)
img='appDiabetes.jpg'
load_images(img)
# Title
st.header("Diabetes Checker app")
st.write("This app is intended to check wheather you are suffering from diabetes or not")
st.write("score 0 means you are not diabetic and score of  2 means you are diabetic")
st.text("Created by Mr.Harshit Harsh")


# Input bar 1
HeartDiseaseorAttack = st.number_input("Enter 1 if you suffer from Heart Disease or had an attack else enter 0")


# Input bar 2
BMI = st.number_input("Enter BMI, BMI = Weight(Kg)/(Height*Height(metre squared))")
HvyAlcoholConsump = st.number_input("Enter 1 if you consume alcohol frequently else enter 0")
Smoker = st.number_input("Enter 1 if you are smoker  else enter 0")
if st.button("Submit"):
    
    
    if ((HeartDiseaseorAttack ==0.00 or HeartDiseaseorAttack == 1.00) and (HvyAlcoholConsump ==0.00 or HvyAlcoholConsump ==1.00) and (Smoker==0.00 or Smoker ==1.00)):
        
   
        clf = joblib.load("clf.pkl")

    # Store inputs into dataframe
        x = pd.DataFrame([[HeartDiseaseorAttack,BMI,Smoker,HvyAlcoholConsump]],
                     columns = ["HeartDiseaseorAttack","BMI","Smoker","HvyAlcoholConsump"])
    # Get prediction
        prediction = clf.predict(x)[0]

    # Output prediction
        st.text(f"This instance is a {prediction}")
        if (prediction ==  2):
            st.text("Consult a Doctor")
    else:
        st.text(f"Please follow instructions")
   
           
 
        
    

   
           
 
        
    
