import matplotlib.pyplot as plt

categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [20, 35, 30, 25]

plt.bar(categories, values)
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.title("Bar Chart Example")
plt.show()
