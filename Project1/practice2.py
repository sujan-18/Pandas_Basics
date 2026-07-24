import pandas as pd

# df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

# df3 = pd.concat([df1, df2], ignore_index=True)
# print(df3)

# df1= pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, 30, 35, 40]})
# df2= pd.DataFrame({'name': ['Alice', 'Bob', 'David'], 'city': ['New York', 'Los Angeles', 'Chicago']})  
# df3 = pd.merge(df1, df2, on='name')
# print(df3)

series1 = pd.Series([1, 2, 3, 4, 5])
series1.name = 'my_series'
print(series1.name)
print(series1.astype(str))