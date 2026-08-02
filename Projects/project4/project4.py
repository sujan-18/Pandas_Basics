import pandas as pd
data = pd.read_csv("adult.csv")
# print(data.head(10))
# print(data.tail(10))
# print(data.shape[0])
# print(data.shape[1])
# print(data.info())
# print(data.sample(frac=0.1, random_state=111)) # Same random sample
# print(data.sample(frac=0.1, random_state=100)) # Different random sample
# print(data.isnull().sum(axis=0)) # Check for missing values
# print(data.isnull().sum(axis=1)) # Check for missing values
import matplotlib.pyplot as plt
import seaborn as sns
# print(sns.heatmap(data.isnull()))
# print(data.isin(['?']).sum(axis=0)) # Check for missing values
# print(data.isin(['?']).sum(axis=1)) # Check for missing values
import numpy as np
# data["workclass"] = data["workclass"].replace('?', np.nan)
# data["native-country"] = data["native-country"].replace('?', np.nan)
# data["occupation"] = data["occupation"].replace('?', np.nan)
# sns.heatmap(data.isin(['?']), cbar=False, cmap='viridis')
# print(data.isin(['?']).sum(axis=0))# Check for missing values
# print(data.duplicated().any()) # Check for duplicate rows
# data.drop_duplicates(inplace=True) # Drop duplicate rows
# print(data.duplicated().any()) # Check for duplicate rows
# data.describe() # Summary statistics for numerical columns

