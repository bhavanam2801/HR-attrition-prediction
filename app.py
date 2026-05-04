


import pickle
import streamlit as st
import numpy as np
import pandas as pd

st.title('👩‍💼 HR Attrition Prediction App')

# load model and scaler
model = pickle.load(open('svm_model.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

# input features
Age = st.number_input('Age', min_value=18, max_value=60, value=30)
DailyRate = st.number_input('Daily Rate', min_value=100, max_value=1500, value=800)
DistanceFromHome = st.number_input('Distance From Home', min_value=1, max_value=30, value=5)
Education = st.selectbox('Education', (1, 2, 3, 4, 5))
EmployeeCount = 1
EmployeeNumber = st.number_input('Employee Number', min_value=1, max_value=3000, value=1000)
EnvironmentSatisfaction = st.selectbox('Environment Satisfaction', (1, 2, 3, 4))
HourlyRate = st.number_input('Hourly Rate', min_value=30, max_value=100, value=60)
JobInvolvement = st.selectbox('Job Involvement', (1, 2, 3, 4))
JobLevel = st.selectbox('Job Level', (1, 2, 3, 4, 5))
JobSatisfaction = st.selectbox('Job Satisfaction', (1, 2, 3, 4))
MonthlyIncome = st.number_input('Monthly Income', min_value=1000, max_value=25000, value=5000)
MonthlyRate = st.number_input('Monthly Rate', min_value=1000, max_value=30000, value=15000)
NumCompaniesWorked = st.number_input('Number of Companies Worked', min_value=0, max_value=10, value=1)
PercentSalaryHike = st.number_input('Percent Salary Hike', min_value=10, max_value=30, value=15)
PerformanceRating = st.selectbox('Performance Rating', (3, 4))
RelationshipSatisfaction = st.selectbox('Relationship Satisfaction', (1, 2, 3, 4))
StandardHours = 80
StockOptionLevel = st.selectbox('Stock Option Level', (0, 1, 2, 3))
TotalWorkingYears = st.number_input('Total Working Years', min_value=0, max_value=40, value=5)
TrainingTimesLastYear = st.number_input('Training Times Last Year', min_value=0, max_value=6, value=2)
WorkLifeBalance = st.selectbox('Work Life Balance', (1, 2, 3, 4))
YearsAtCompany = st.number_input('Years At Company', min_value=0, max_value=40, value=3)
YearsInCurrentRole = st.number_input('Years In Current Role', min_value=0, max_value=20, value=2)
YearsSinceLastPromotion = st.number_input('Years Since Last Promotion', min_value=0, max_value=15, value=1)
YearsWithCurrManager = st.number_input('Years With Current Manager', min_value=0, max_value=20, value=2)

BusinessTravel = st.selectbox('Business Travel', ('Non-Travel', 'Travel_Frequently', 'Travel_Rarely'))
Department = st.selectbox('Department', ('Human Resources', 'Research & Development', 'Sales'))
EducationField = st.selectbox('Education Field', ('Human Resources', 'Life Sciences', 'Marketing', 'Medical', 'Other', 'Technical Degree'))
Gender = st.selectbox('Gender', ('Female', 'Male'))
JobRole = st.selectbox('Job Role', ('Healthcare Representative', 'Human Resources', 'Laboratory Technician',
                                    'Manager', 'Manufacturing Director', 'Research Director',
                                    'Research Scientist', 'Sales Executive', 'Sales Representative'))
MaritalStatus = st.selectbox('Marital Status', ('Divorced', 'Married', 'Single'))
OverTime = st.selectbox('Over Time', ('No', 'Yes'))

# Encoding
BusinessTravel_Travel_Frequently = 1 if BusinessTravel == 'Travel_Frequently' else 0
BusinessTravel_Travel_Rarely = 1 if BusinessTravel == 'Travel_Rarely' else 0

Department_Research_Development = 1 if Department == 'Research & Development' else 0
Department_Sales = 1 if Department == 'Sales' else 0

EducationField_Life_Sciences = 1 if EducationField == 'Life Sciences' else 0
EducationField_Marketing = 1 if EducationField == 'Marketing' else 0
EducationField_Medical = 1 if EducationField == 'Medical' else 0
EducationField_Other = 1 if EducationField == 'Other' else 0
EducationField_Technical_Degree = 1 if EducationField == 'Technical Degree' else 0

Gender_1 = 1 if Gender == 'Male' else 0

JobRole_Human_Resources = 1 if JobRole == 'Human Resources' else 0
JobRole_Laboratory_Technician = 1 if JobRole == 'Laboratory Technician' else 0
JobRole_Manager = 1 if JobRole == 'Manager' else 0
JobRole_Manufacturing_Director = 1 if JobRole == 'Manufacturing Director' else 0
JobRole_Research_Director = 1 if JobRole == 'Research Director' else 0
JobRole_Research_Scientist = 1 if JobRole == 'Research Scientist' else 0
JobRole_Sales_Executive = 1 if JobRole == 'Sales Executive' else 0
JobRole_Sales_Representative = 1 if JobRole == 'Sales Representative' else 0

MaritalStatus_Married = 1 if MaritalStatus == 'Married' else 0
MaritalStatus_Single = 1 if MaritalStatus == 'Single' else 0

OverTime_1 = 1 if OverTime == 'Yes' else 0

# define dataframe
input_features = pd.DataFrame({
    'Age': [Age],
    'DailyRate': [DailyRate],
    'DistanceFromHome': [DistanceFromHome],
    'Education': [Education],
    'EmployeeCount': [EmployeeCount],
    'EmployeeNumber': [EmployeeNumber],
    'EnvironmentSatisfaction': [EnvironmentSatisfaction],
    'HourlyRate': [HourlyRate],
    'JobInvolvement': [JobInvolvement],
    'JobLevel': [JobLevel],
    'JobSatisfaction': [JobSatisfaction],
    'MonthlyIncome': [MonthlyIncome],
    'MonthlyRate': [MonthlyRate],
    'NumCompaniesWorked': [NumCompaniesWorked],
    'PercentSalaryHike': [PercentSalaryHike],
    'PerformanceRating': [PerformanceRating],
    'RelationshipSatisfaction': [RelationshipSatisfaction],
    'StandardHours': [StandardHours],
    'StockOptionLevel': [StockOptionLevel],
    'TotalWorkingYears': [TotalWorkingYears],
    'TrainingTimesLastYear': [TrainingTimesLastYear],
    'WorkLifeBalance': [WorkLifeBalance],
    'YearsAtCompany': [YearsAtCompany],
    'YearsInCurrentRole': [YearsInCurrentRole],
    'YearsSinceLastPromotion': [YearsSinceLastPromotion],
    'YearsWithCurrManager': [YearsWithCurrManager],
    'BusinessTravel_Travel_Frequently': [BusinessTravel_Travel_Frequently],
    'BusinessTravel_Travel_Rarely': [BusinessTravel_Travel_Rarely],
    'Department_Research & Development': [Department_Research_Development],
    'Department_Sales': [Department_Sales],
    'EducationField_Life Sciences': [EducationField_Life_Sciences],
    'EducationField_Marketing': [EducationField_Marketing],
    'EducationField_Medical': [EducationField_Medical],
    'EducationField_Other': [EducationField_Other],
    'EducationField_Technical Degree': [EducationField_Technical_Degree],
    'Gender_1': [Gender_1],
    'JobRole_Human Resources': [JobRole_Human_Resources],
    'JobRole_Laboratory Technician': [JobRole_Laboratory_Technician],
    'JobRole_Manager': [JobRole_Manager],
    'JobRole_Manufacturing Director': [JobRole_Manufacturing_Director],
    'JobRole_Research Director': [JobRole_Research_Director],
    'JobRole_Research Scientist': [JobRole_Research_Scientist],
    'JobRole_Sales Executive': [JobRole_Sales_Executive],
    'JobRole_Sales Representative': [JobRole_Sales_Representative],
    'MaritalStatus_Married': [MaritalStatus_Married],
    'MaritalStatus_Single': [MaritalStatus_Single],
    'OverTime_1': [OverTime_1]
})

# scaling
input_features = scaler.transform(input_features)

# prediction
if st.button('Predict'):
    prediction = model.predict(input_features)

    if prediction[0] == 1:
        st.error('⚠️ Employee is likely to leave the company')
    else:
        st.success('✅ Employee is not likely to leave the company')
