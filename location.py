# import clean dataframe
from data_clean import df_prediction


# libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


# Feature Engineering
# Date Parsing: Convert the 'Date' column into a datetime format and extract relevant time features if not already done. This could include the year, month, day, and possibly creating a cyclic feature to capture seasonal effects (if applicable).
# Lag Features: For time series forecasting, creating lag features based on past earthquakes (e.g., magnitude and depth of the last earthquake) can be valuable.
# Rolling Window Features: Calculate rolling statistics (mean, standard deviation, etc.) over past events to capture trends over time.


# RSME value for magnitude
X = df_prediction[['Latitude', 'Longitude', 'Depth']]
y = df_prediction['Magnitude']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print(f"RMSE: {rmse}")
