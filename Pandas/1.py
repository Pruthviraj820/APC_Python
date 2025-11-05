import pandas as pd

data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': [250, 300, 200, 400, 150, 350]
}
df = pd.DataFrame(data)

grouped = df.groupby('Region')['Sales'].sum()
print(grouped)
