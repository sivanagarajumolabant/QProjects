
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

"""Data Collection & Processing"""

# loading the data from csv file to a Pandas DataFrame
calories = pd.read_csv('calories.csv')

# print the first 5 rows of the dataframe
calories.head()

exercise_data = pd.read_csv('exercise.csv')

exercise_data.head()

"""Combining the two Dataframes"""

calories_data = pd.concat([exercise_data, calories['Calories']], axis=1)

calories_data.head()

# checking the number of rows and columns
calories_data.shape

# getting some informations about the data
calories_data.info()

# checking for missing values
calories_data.isnull().sum()

"""Data Analysis"""

"""Converting the text data to numerical values"""

calories_data.replace({"Gender":{'male':0,'female':1}}, inplace=True)

calories_data.head()

"""Separating features and Target"""

X = calories_data.drop(columns=['User_ID','Calories'], axis=1)
Y = calories_data['Calories']

print(X)

print(Y)

"""Splitting the data into training data and Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training

XGBoost Regressor
"""

# loading the model
model = XGBRegressor()

# training the model with X_train
model.fit(X_train, Y_train)

"""Evaluation

Prediction on Test Data
"""

test_data_prediction = model.predict(X_test)

print(test_data_prediction)

"""Mean Absolute Error"""

mae = metrics.mean_absolute_error(Y_test, test_data_prediction)

print("Mean Absolute Error = ", mae)

