import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [88, 45, 72, 90]
})

filtered = df[df['Marks'] > 70]
print(filtered)
