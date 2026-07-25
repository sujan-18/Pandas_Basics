import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.DataFrame({
    "Name":["Alice", "Bob", "Charlie", "David"],
    "Age":[25, 30, 35, 40],
    "Student_id":[1001, 1002, 1003, 1004],
    "roll_no":[1, 2, 3, 4]
})

df2=pd.DataFrame({
    "Department":["CS", "Math", "Physics", "Chemistry"],
    "Student_id":[1001, 1002, 1003, 1004],
    "roll_no":[1, 2, 3, 4]    
})

result = pd.merge(df1,df2, on=["Student_id","roll_no"]) # Merging two DataFrames based on the common column "Student_id"
# print(result)
# print(plt.plot(result["Age"]))
print(plt.hist(result["Age"], bins=5, color='blue', alpha=0.7)) # Creating a histogram of the "Age" column from the merged DataFrame
plt.show() # Displaying the merged DataFrame based on the common column "Student_id" 