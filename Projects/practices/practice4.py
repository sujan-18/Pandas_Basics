import pandas as pd

# Create a pandas Series
my_data = pd.Series(
    {
        "apple": 240,
        "banana": 120,
        "orange": 200,
        "grape": 150
    }
)
# print(my_data.name)
my_data.name = "Fruit Prices"
# print(my_data)
# print(my_data.loc["apple"])
# print(my_data.iloc[0])
# print(my_data[my_data ==200])

# # Logical operators
# print(my_data[(my_data>150) & (my_data<250)])
# my_data["apple"] = 250
# print(my_data)

# Data Frame

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Student_id": [1001, 1002, 1003, 1004],
    "Department": ["CS", "Math", "Physics", "Chemistry"]
})

# print(df.loc[1]) # Accessing row by index label
# print(df.loc[df["Name"] == "Alice"]) # Accessing row by column name
# print(df.iloc[1]) # Accessing row by index position
# print(df.index)
df.index = ["Student1", "Student2", "Student3", "Student4"]
# print(df.index)
# print(df.loc["Student1"])
# print(df.loc["Student1", "Name"]) # Accessing specific column for a row
# print(df.iloc[ : ])
# print(df.loc["Student1" : "Student3"])
# print(df.loc[["Student1", "Student3"], ["Name", "Age"]]) 

# print(df.shape) # Accessing specific rows and columns
# print(df.columns) # Accessing column names
# print(df.drop("Department", axis = 1, inplace=True)) # Dropping a column
# print(df) # Displaying the DataFrame after dropping the column
# print(df.info()) # Displaying information about the DataFrame
# print(df["Department"].value_counts()) # Counting the occurrences of each unique value in the "Department" column
# print(df["Department"].unique()) # Displaying the unique values in the "Department" column
# print(df["Department"].iloc[0])
# print(df["Department"].loc["Student1"]) # Accessing a specific value in the "Department" column for a specific row

# Broadcasting values
# df["Age"] = df["Age"] + 5
# print(df["Age"])

# df["Age"] = df["Age"].apply(lambda x: x + 5)
# print(df["Age"]) 

# Rename Columns
# df.rename(columns={"Name": "name", "Age": "age"}, inplace=True)
# print(df)

# Data cleaning and handling missing values
print(df.isnull()) # Checking for missing values in the DataFrame
print(df.isnull().sum()) # Counting the number of missing values in each column

# dataframe with missing values
df1 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, None, 40],
    "Student_id": [1001, 1002, 1003, None]
})
# print(df1)
# print(df1.isnull()) # Checking for missing values in the new DataFrame
# print(df1.isnull().sum()) # Counting the number of missing values in each column of the new DataFrame
# print(df1.dropna(how="all")) # Dropping rows with all missing values
# print(df1.dropna(how="any")) # Dropping rows with any missing values
# print(df1) # Displaying the DataFrame after dropping rows with missing values

# Filling missing values
# print(df1.fillna(1))
# print(df1.fillna({"Age": df1["Age"].mean(), "Student_id": df1["Student_id"].median()})) # Filling missing values with the mean of the respective columns

# # print(df1["Name"].replace({"Alice": "Alicia", "Bob": "Robert"})) # Replacing specific values in the "Name" column
# print(df1["Name"].replace("Alice", "Alicia")) # Replacing specific values in the "Name" column
# print(df1.duplicated()) # Checking for duplicate rows in the DataFrame


# Making a duplicate dataframe row for testing
df2 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Alice"],
    "Age": [25, 30, None, 40, 25],
    "Student_id": [1001, 1002, 1003, None, 1001],
    "Department": ["CS", "Math", "Physics", "Chemistry", "CS"]
})

# print(df2.duplicated()) # Checking for duplicate rows in the new DataFrame
# print(df2.duplicated(keep = "first")) # Checking for duplicate rows in the new DataFrame, keeping the first occurrence
# print(df2.duplicated(keep = "last")) # Checking for duplicate rows in the new DataFrame, keeping the last occurrence

# dup = df2[df2.duplicated(keep = "first")] # Getting all duplicate rows in the new DataFrame
# dup = df2[df2.duplicated(keep = "last")] # Getting all duplicate rows in the new DataFrame

# dup = df2[df2.duplicated(keep = False)] # Getting all duplicate rows in the new DataFrame
# print(dup) # Displaying all duplicate rows in the new DataFrame
# print(df2.drop_duplicates(keep = "first")) # Dropping duplicate rows in the new DataFrame, keeping the first occurrence


# spliting name
df3= pd.DataFrame({
    "Name": ["Alice Smith", "Bob Johnson", "Charlie Brown", "David Wilson"],
    "Age": [25, 30, 35, 40]})
df3[["First Name", "Last Name"]] = df3["Name"].str.split(" ", expand=True) # Splitting the "Name" column into "First Name" and "Last Name" columns
print(df3) # Displaying the DataFrame after splitting the "Name" column