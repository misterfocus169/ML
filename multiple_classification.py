# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 10:14:14 2026

@author: Lab
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu  import option_menu

#load model
loan_model = pickle.load(open('loan_model.sav','rb'))
ridingmower_model = pickle.load(open('RidingMowers_model.sav','rb'))
bmi_model = pickle.load(open('bmi_model.sav','rb')) 

with st.sidebar:
    selected = option_menu(
        'Classification',
        ['Loan',"RidingMower",'BMI'])

if(selected == 'RidingMower'):
    st.title('RidingMower Predict')
    
    Income = st.text_input('Income')
    LotSize = st.text_input('LotSize')
    ridingmower_predict = ''
    
    if st.button('Predict'):
        ridingmower_predict = ridingmower_model.predict([[ 
            float(Income),
            float(LotSize)
        ]])
        if ridingmower_predict[0]==0:
            ridingmower_predict='Non Owner'
        else:
            ridingmower_predict = 'Owner'
    
    st.success(ridingmower_predict)
    
    
if(selected == 'Loan'):
    st.title('Loan Predict')
    
    person_age = st.text_input('person_age')
    person_gender = st.text_input('person_gender')
    person_education = st.text_input('person_education')
    person_income = st.text_input('person_income')
    person_emp_exp = st.text_input('person_emp_exp')
    person_home_ownership = st.text_input('person_home_ownership')
    loan_amnt = st.text_input('loan_amnt')
    loan_intent = st.text_input('loan_intent')
    loan_int_rate = st.text_input('loan_int_rate')
    loan_percent_income = st.text_input('loan_percent_income')
    cb_person_cred_hist_length = st.text_input('cb_person_cred_hist_length')
    credit_score = st.text_input('credit_score')
    previous_loan_defaults_on_file = st.text_input('previous_loan_defaults_on_file')
    
    loan_predict = ''
    
    if st.button('Predict'):
        loan_predict = loan_model.predict([[ 
            float(person_age),
            float(person_gender),
            float(person_education),
            float(person_income),
            float(person_emp_exp),
            float(person_home_ownership),
            float(loan_amnt),
            float(loan_intent),
            float(loan_int_rate),
            float(loan_percent_income),
            float(cb_person_cred_hist_length),
            float(credit_score),
            float(previous_loan_defaults_on_file)
        ]])
        if loan_predict[0]==0:
            loan_predict='Not Accept'
        else:
            loan_predict = 'Accept'
    
    st.success(loan_predict)
        
if(selected == 'BMI'):
    st.title('BMI Classification')
    
    Gender = st.selectbox('Gender', ['Male', 'Female'])
    Gender = 0 if Gender == 'Male' else 1
    Height = st.text_input('Height (cm)')
    Weight = st.text_input('Weight (kg)')
    bmi_predict = ''
    
    if st.button('Predict'):
        bmi_predict = bmi_model.predict([[ 
            float(Gender),
            float(Height),
            float(Weight)
        ]])
        if bmi_predict[0]==0:
            bmi_predict='Weak'
        else:
            bmi_predict = 'Obesity'
    
    st.success(bmi_predict)










