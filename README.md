 # Pulsify: A smart and hybrid Web Application

 Pulsify: Cardiac Disease Predictor Web Application

# Abstract
Pulsify is a web-based application built with Django that usess a trained Gradient Boosting Machine Learning model to predict heart disease based on user input. This project helps patients, doctors,and administrators to predict and manage their cardiac health with the ease of their home.


## Features

Login and Sign up system for patients, doctors and admins
ML based heart disease prediction using Gradient Boosting
User friendly health prediction web application interface
Patient health records and history
Admin dashboard with doctor and patient reports and feedback
Admin Panel for managing users and system logs



## Tools and Technology Used           

Backend: Python as django         
Frontend: HTML, CSS, JavaScript    
ML Model: Gradient Boosting        
Data Scaling: StandardScaler scalar.pkl
Database: SQLite                   
Model Storage: Pickle gradient_boosting_model.pkl



## Machine Learning Model

Algorithm: Gradient Boosting Classifier
Preprocessing: Standard scaler trained and saved in scalar.pkl
Training Dataset: UCI heart disease dataset 
Output: Healthy or unhealthy which is 0 and 1 binary classification

## Model files import pandas as pd 
gradient_boosting.pkl trained model
scaler.pkl used for feature scaling

import pickle
scaler=pickle.load(open('scaler.pkl' , 'rb'))
model=pickle.load(open('gradient_boosting.pkl' , 'rb'))


## Usage Guide
Register or log in as patient, doctor, or admin.
As a patient go to the prediction form and enter health data.
View the result of heart disease prediction.
Doctors can view patient records and give appointment availability.
Admins manage the entire system including users.

## Performance Metrics

Accuracy and precision of result in form of output


## ML Model Integration
The gradient_boosting_model.pkl file contains the trained model.
The scalar.pkl file contains the standardscaler used during model training.
It loads these .pkl files to preprocess input and make predictions during runtime.




# How to Run the Project Locally

### Prerequisites
Python 3.12.6
pip
Virtual Environment

# Setup Instructions

### 1. Github repository link
https://github.com/maryamfatima6722/pulsify.git
cd pulsify

### 2. Create and activate a virtual environment
python -m venv .venv
Windows: .venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run migrations
python manage.py makemigrations
python manage.py migrate

### 5. Create a superuser just for admin access
python manage.py createsuperuser

### 6. Run the server
python manage.py runserver



## Future Improvements
Model improvement
Integration of additional real time data
Mobile App version with React native or flutter
Visualization of prediction trends over time



# Project members
Developed as a Final Year Project by:
# Name:
 Maryam Fatima, Kiran mukhtar and Maryam Nadeem
# University:
 Govt degree college Mandi bahauddin affiliated by PUCIT
# Supervisor: 
Prof fayyaz Ch.

