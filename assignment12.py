import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip()
df = df.drop_duplicates()

obj_cols = df.select_dtypes(include="object").columns
for c in obj_cols:
    df[c] = df[c].astype(str).str.strip().str.lower()

num = df.select_dtypes(include="number")
if not num.empty:
    q1 = num.quantile(0.01)
    q99 = num.quantile(0.99)
    mask = ((num >= q1) & (num <= q99)).all(axis=1)
    df = df[mask]

df = df.dropna()
df = pd.get_dummies(df, drop_first=True)
df = df.loc[:, df.nunique() > 1]

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape, X_test.shape)
