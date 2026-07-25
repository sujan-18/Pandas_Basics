import pandas as pd
students = pd.DataFrame({
    "Name":["Alice","Bob"]
},index=[1001,1002])

marks = pd.DataFrame({
    "Marks":[90,85]
},index=[1001,1002])

result = students.join(marks) # Joining two DataFrames based on the index
print(result) # Displaying the joined DataFrame based on the index