import pandas as pd
dict1 = {"Name":["Priyang","Aadhya", "Krishna", "Parshv", "Mittal", "Archana"],
         "Marks":[90, 85, 95, 80, 75, 70],
         "Gender":["Male", "Female", "Female", "Male", "Male", "Female"]}

df1 = pd.DataFrame(dict1)

# print(df1.head(3)) # Displaying the first 3 rows of the DataFrame
# print(df1.tail(3)) # Displaying the last 3 rows of the DataFrame
# print(df1.shape) # Displaying the shape of the DataFrame (number of rows and columns)
# print(df1.info()) # Displaying information about the DataFrame, including data types and non-null counts
# print(df1.isnull()) # Checking for missing values in the DataFrame
# print(df1.isnull().sum()) # Counting the number of missing values in each column of the DataFrame
# print(df1.describe()) # Displaying summary statistics for numerical columns in the DataFrame
# print(df1["Name"].unique()) # Displaying unique values in the DataFrame
# print(df1["Name"].nunique()) # Displaying unique values in the DataFrame
# print(df1["Gender"].unique()) # Displaying unique values in the "Gender
# print(df1["Gender"].nunique()) # Counting the number of unique values in the "Gender" column
# print(df1["Gender"].value_counts()) # Counting
# print(df1[df1["Marks"] >=90].value_counts())
# print(sum(df1["Marks"].between(80, 90))) # Counting the number of rows where "Marks" is between 80 and 90
# print(df1["Marks"].mean()) # Calculating the mean of the "Marks" column
# print(df1["Marks"].median()) # Calculating the median of the "Marks" column
# print(df1["Marks"].apply(lambda x: x + 5)) # Applying a lambda function to add 5 to each value in the "Marks" column

# def add_five(x):
#     return x + 5
# print(df1["Marks"].apply(add_five)) # Applying a custom function to add 5 to each value in the "Marks" column
# print(df1["Name"].map({"Priyang": "Priya", "Aadhya": "Aadya"})) # Mapping specific values in the "Name" column to new values
# print(df1["Name"].replace({"Priyang": "Priya", "Aadhya": "Aadya"})) # Mapping specific values in the "Name" column to new values
# droped=df1.drop("Gender", axis=1) # Dropping the "Gender" column from
# print(droped) # Dropping the "Gender" column
# print(df1.sort_values(by="Marks")) # Sorting the DataFrame by the "Marks" column in descending order
# print(df1.sort_values(by="Marks", ascending=False)) # Sorting the DataFrame by the "Marks" column in descending order
print(df1[df1["Gender"]=="Female"][["Name","Marks"]]) # Counting the occurrences of each unique value in the "Gender" column and displaying the "Name" and "Marks" columns for those rows