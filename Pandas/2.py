import pandas as pd

customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

orders = pd.DataFrame({
    'OrderID': [101, 102, 103],
    'CustomerID': [1, 2, 1],
    'Amount': [250, 400, 150]
})

merged = pd.merge(customers, orders, on='CustomerID')
print(merged)
