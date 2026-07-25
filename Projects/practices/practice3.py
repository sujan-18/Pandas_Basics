import pandas as pd

df1 = pd.DataFrame({
    "Name":["Alice", "Bob", "Charlie", "David"],
    "Age":[25, 30, 35, 40],
    "Student_id":[1001, 1002, 1003, 1004],
}, index=["A", "B", "C", "D"])
# print(df1)
# print(df1.dtypes)
# print(df1.describe())
# print(df1.info())
# print(df1.head())
# print(df1.tail())
# print(df1["Name"])
# print(df1.loc[0])
# print(df1.iloc[0])
# print(df1[df1["Age"] > 30])
# print(df1[df1["Age"] > 30][["Name", "Age"]])
# print(df1.loc["A"])
# print(df1.iloc[0])
# print(df1.iloc["A"])