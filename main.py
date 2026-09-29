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
