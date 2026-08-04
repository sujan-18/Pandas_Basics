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
# data.drop(['educational-num', 'capital-gain', 'capital-loss'], axis=1, inplace=True) # Drop columns
# print(data.columns)
# print(data['age'].describe(include='all')) # Summary statistics for age column
# print(data['age'].value_counts()) # Frequency counts for age column
# print(data['age'].hist(bins=20)) # Histogram for age column
# print(sum(data['age'] >= 17)) # Sum of all columns for rows where age is greater than or equal to 17
# print(sum(data['age'] <= 48)) # Sum of all columns for rows where age is less than or equal to 48
# print(sum((data['age'] >= 17) & (data['age'] <= 48))) # Sum of all columns for rows where age is between 17 and 48
# print(sum(data['age'].between(17, 48))) # Sum of all columns for rows where age is between 17 and 48
# plt.figure(figsize=(10, 6))
# print(data['workclass'].hist())
# plt.show()
# print(sum(data['education'] == 'Bachelors')) # Sum of all columns for rows where education is Bachelors
# f1 = data['education']== 'Bachelors'
# f2 = data['workclass']== 'Private'
# print(len(data[f1 | f2])) # Sum of all columns for rows where education is Bachelors or workclass is Private

# sum1=sum(data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) # Sum of all columns for rows where education is Bachelors, Masters or Doctorate
# print(sum1)
# sns.boxplot(x='income', y='age', data=data)
# plt.show()
# print(data['income'].unique()) # Frequency counts for income column
# print(data['income'].value_counts()) # Frequency counts for income columns
# sns.countplot(x='income', data=data)
# plt.show()
# print(data['workclass'])
# print(data.groupby('workclass'))
# print(data.groupby('workclass')['income'])
# print(data['income'])
# print(data['income'].dtype)
data['income'] = data['income'].map({
    '<=50K': 0,
    '>50K': 1
})
#  print(data['income'].dtype)
# print(data['income'].unique()) # Frequency counts for income column
# print(data['income'].value_counts()) # Frequency counts for income column
# print(data.groupby('workclass')['income'].mean().sort_values(ascending=False).head(1)) # Mean income by workclass
# print(data.groupby('gender')['income'].mean().sort_values(ascending=True))
print(data["workclass"].info())
data["workclass"]= data["workclass"].astype("category")
print(data["workclass"].info())
