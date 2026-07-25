import pandas as pd

df1 = pd.DataFrame({
    "Name":["Alice", "Bob", "Charlie", "David"]})

df2 = pd.DataFrame({"Name":["Alice", "Bob", "Charlie", "David"]})

df3 = pd.DataFrame({ 
    "Age":[25, 30, 35, 40]
})

result = pd.concat([df1, df2], ignore_index=True, axis=1) # Concatenating two DataFrames vertically and resetting the index
result1 = pd.concat([df1,df3], ignore_index=True, axis=1) # Concatenating two DataFrames vertically and resetting the index
print(result1) # Displaying the concatenated DataFrame
