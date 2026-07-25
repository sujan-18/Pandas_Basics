import pandas as pd
data = pd.read_csv("Ecommerce Purchases")
# print(data.head(10)) # Displaying the first 10 rows of the DataFrame
# print(data.tail(10)) # Displaying the last 10 rows of the DataFrame
# print(data.info()) # Displaying information about the DataFrame, including data types and non-null counts
# print(data.dtypes)
# print(data.isnull()) # Checking for missing values in the DataFrame
# print(data.isnull().sum()) # Counting the number of missing values in each column of the DataFrame
# print(data.shape[0]) # Displaying the shape of the DataFrame (number of rows and columns)
# print(data.shape[1]) # Displaying the shape of the DataFrame (number of rows and columns)
# print(data["Purchase Price"].max()) # Displaying the maximum value in the "Purchase Price" column
# print(data["Purchase Price"].min()) # Displaying the minimum value in the "Purchase Price" column
# print(data["Purchase Price"].mean()) # Displaying the mean value in the "Purchase Price" column
# print(len(data[data["Language"]=="fr"]))
# print(data[data["Language"]=="fr"].count())
# print(data[data["Language"]=="fr"].sum())
# print(data["Job"].str.contains("engineer", case=False).sum()) # Counting the number of occurrences of the word "engineer" in the "Job" column
# print(len(data[data["Job"].str.contains("engineer", case=False)])) # Counting the number of occurrences of the word "engineer" in the "Job" column
# print(data[data["IP Address"]=="132.207.160.22"]["Email"]) # Displaying the email address associated with the IP address "
# print(data.columns)
# print(((data["CC Provider"]=="Mastercard") & (data["Purchase Price"] > 50)).sum()) # Counting the number of occurrences of the word "Mastercard" in the "CC Provider" column
# print(len(data[(data["CC Provider"]=="Mastercard") & (data["Purchase Price"] > 50)])) # Counting the number of occurrences of the word "Mastercard" in the "CC Provider" column
# print(data["AM or PM"].value_counts()) # Counting the number of occurrences of each unique value in the "AM or PM" column

# def func():
#     count=0
#     for Data in data["CC Exp Date"]:
#         if Data.split("/")[1]=="20":
#             count+=1
#     print(count)
# func()

# print(len(data[data["CC Exp Date"].apply(lambda x:x.split("/")[1]=="20")]))
print(data["Email"].apply(lambda x:x.split("@")[1]).value_counts().head())