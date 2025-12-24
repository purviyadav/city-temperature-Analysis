import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("city_temperature.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(data.head())

# Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Clean the data
cleaned_data = data.dropna()

# Basic analysis
print("\nBasic statistics:")
print(cleaned_data.describe())

# Visualization
plt.figure()
plt.plot(cleaned_data.index, cleaned_data.iloc[:, 0])
plt.title("City Temperature Trend")
plt.xlabel("Index")
plt.ylabel("Temperature")
plt.show()
