import pandas as pd

file_name = "employee_dataset.csv"
df = pd.read_csv(file_name)

print(df.head())
print(df.info())
print(df.describe())
print(df[["Name", "Age", "Salary"]].head())
print(df[df["Age"] > 40].head())

sorted_df = df.sort_values(by="Salary", ascending=False)
print(sorted_df.head())

avg_salary = df.groupby("Department")["Salary"].mean().reset_index()
print(avg_salary)

df["Bonus"] = (df["Salary"] * 0.10).astype(int)
print(df.head())

df.to_csv("employee_dataset_processed.csv", index=False)
