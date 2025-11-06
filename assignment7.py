import pandas as pd

data = {
    'Name': ['Rahul', 'Shubham', 'Vishal', 'Soham', 'Pranav'],
    'Age': [25, 30, 35, 40, 29],
    'Salary': [50000, 60000, 75000, 80000, 65000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR']
}

df = pd.DataFrame(data)
print(" Original DataFrame:\n", df, "\n")


print("Selecting 'Name' column:\n", df['Name'], "\n")

print("Selecting first 3 rows:\n", df.head(3), "\n")


print(" Employees with Salary > 60000:\n", df[df['Salary'] > 60000], "\n")
print("Employees from IT Department:\n", df[df['Department'] == 'IT'], "\n")


df['Bonus'] = df['Salary'] * 0.10
print(" After Adding 'Bonus' Column:\n", df, "\n")




print(" Sorting by Salary (Descending):\n", df.sort_values(by='Salary', ascending=False), "\n")




df_dropped = df.drop(columns=['Bonus'])
print(" After Dropping 'Bonus' Column:\n", df_dropped, "\n")

df_row_dropped = df.drop(index=2)
print("After Dropping Row with index 2:\n", df_row_dropped, "\n")


print("Statistical Summary:\n", df.describe(), "\n")


