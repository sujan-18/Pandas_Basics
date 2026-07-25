import pandas as pd
# s = pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])
# print(s)

# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# print(df)

external_data = pd.read_csv('random.csv')
# print(external_data)
# print(external_data.head())
# print(external_data.tail())
# print(external_data.describe())
# print(external_data.info())
# print(type(external_data["year"]))
# print(external_data[["year", "unit"]])
# print(external_data.iloc[0])
# print(external_data.dropna())
# print(external_data.rename(columns={'year':'Y', 'unit':'U'}))
# external_data["year"]=external_data["year"].astype(int)
# print(external_data)
# print(external_data["new_column"])

# Add a new column
# external_data["new_column"] = "sujan"
# external_data.loc[:4,"prize"]=1000
# external_data.loc[5: ,"prize"]=1000
# print(external_data)

external_data["new_data"] = [2000 if i < 5 else 1000 for i in range(len(external_data))]
print(external_data)


def func(value):
    return value * 2
external_data["new_data*2"] = external_data["new_data"].apply(func)
print(external_data)
