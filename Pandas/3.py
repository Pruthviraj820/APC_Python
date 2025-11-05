import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, None, 92, None]
}
df = pd.DataFrame(data)

df['Score'].fillna(df['Score'].mean(), inplace=True)
print(df)
