# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 23:47:15 2025

@author: DELL
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model
diabetes_model=pickle.load(open('trained_model.sav','rb'))
 

#with st.sidebar from navigation
with st.sidebar:
    selected=option_menu('Diabetes Prediction System',
                         
                         [' Pregnancy Diabetes Prediction',
                          'Young Diabetes Prediction System',
                          'Adult Diabetes Prediction System'],
                         icons=['activity','heart','person'],
                         default_index=0)
    #diabetes prediction page
if(selected== 'Pregnancy Diabetes Prediction'):

#page title
  st.title('Diabetes Prediction Using Ml')  

#getting the input data from the user
  col1,col2,col3=st.columns(3)

  with col1:
    Pregnancies=st.text_input('Number of Pregnancy')
    
  with col2:
    Gulcose=st.text_input('Gulcose level')

  with col3:
    bloodPressure=st.text_input('Blood pressure level')
    
  with col1:
   SkinThickness=st.text_input('Skin Thickness level')

  with col2:
    Insulin=st.text_input('Insulin level')  
 
  with col3: 
    BMI=st.text_input('BMI level')
    
  with col1:
    DiabetesPedigreeFunction=st.text_input(' Diabetes Pedigree Function level') 
    
  with col2:
     Age=st.text_input('Age Value')
     
     #code for prediction
  diab_diagnosis=''
  
  #creating a button for prediction
  if st.button('Diabetes Test Result'):
      diab_prediction=diabetes_model.predict([[ Pregnancies, Gulcose,bloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
      if(diab_prediction[0]==1):
          diab_diagnosis='the person is diabetic'
      else:
          diab_diagnosis='the person is  not diabetic'
          
       
  st.success(diab_diagnosis)       