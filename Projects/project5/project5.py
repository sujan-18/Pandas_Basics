import pandas as pd
data = pd.read_csv("train.csv")
# print(data.head())
# print(data.tail(3))
# print(data.shape)
# print(data.shape[0])
# print(data.shape[1])
# print(data.info())
# print(data.describe())
# print(data.columns)
# print(data['Name'])
# print(data[['Name', 'Age']])
# print(data['sex']=='male')
# print(data.isnull().sum())

import seaborn as sns
import matplotlib.pyplot as plt

# sns.heatmap(data.isnull())
# plt.show()
# print(data.isnull().sum()*100/len(data))

# print(data["Embarked"].value_counts())
# print(data["Embarked"].mode())
# print(data[data["Embarked"].isnull()])
# data["Embarked"]=data["Embarked"].fillna("s",inplace=True)
# print(data["Embarked"].isnull().sum())
# print(data.columns)
# print(data["Age"].value_counts())
# print(data["Age"].isnull().sum())
# print(data["Age"].isnull().value_counts())
# print(data[data["Age"].isnull()])
# data["Age"] = data["Age"].fillna(18)
# x = data["Sex"].map({'male': 0, 'female': 1})
# print(data['Sex'].value_counts())

# print(data['Sex'])
# data.insert(5,"Gender",data["Sex"])
# print(data["Gender"])
# print(data.columns)
# print(data['Embarked'].value_counts())
# data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
# print(data['Embarked'])
# print(pd.get_dummies(data,columns=['Embarked'], dtype=int))
# print(pd.get_dummies(data,columns=['Embarked']))
# print(pd.get_dummies(data,columns=['Embarked'], drop_first=True))
# print(data['Survived'].value_counts())
# sns.countplot(data['Survived'])
# plt.show()
# import seaborn as sns
# import matplotlib.pyplot as plt

# print(data["Pclass"].value_counts())

# sns.countplot(x="Pclass", data=data)
# plt.show()

# sex=data['Sex'].value_counts()
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.countplot(x='Sex', data=data)
# plt.show()

# for numeric data
# plt.hist(data['Age'])
# plt.show()

# sns.histplot(data['Age'])
# plt.show()

# sns.boxplot(data['Age'])
# plt.show()

# sns.countplot() → Categorical data
# sns.histplot() → Numerical distributions
# sns.boxplot() → Outlier detection and comparison
# plt.hist() → Learn it because it's the underlying Matplotlib function, but prefer sns.histplot() in most analysis projects.
# sns.barplot(x='Sex', y='Survived', data=data)
# plt.show()

# sns.barplot(x='Pclass', y='Survived', data=data)
# plt.show()

# Feature Engineering
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
# print(data['FamilySize'])
print(data.head(1))