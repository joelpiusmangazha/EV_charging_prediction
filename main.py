import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('ev_charging_patterns.csv')    #load dataset
#display first 5 rows
print(data.head())  
#display shape
print("\nDataset Shape:")   
print(data.shape)
#display column info
print("\nDataset Information:") 
print(data.info())
#Missing values
print("\nMissing Values:")  
print(data.isnull().sum())
#statistical summary
print("\nStatistical Summary:")
print(data.describe())

#check missing values before cleaning
print("\nMissing Values Before Cleaning:")
print(data.isnull().sum())

# Fill missing numerical values with the median
numerical_columns = data.select_dtypes(include="number").columns

for column in numerical_columns:
    data[column] = data[column].fillna(data[column].median())

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(data.isnull().sum())

# Display dataset shape
print("\nDataset Shape After Cleaning:")
print(data.shape)

# Target variable analysis
print("\nCharging Duration Statistical Summary:")
print(data["Charging Duration (hours)"].describe())

plt.figure(figsize=(8, 5))

sns.histplot(
    data["Charging Duration (hours)"],
    bins=30,
    kde=True
)

plt.title("Distribution of Charging Duration")
plt.xlabel("Charging Duration (hours)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
