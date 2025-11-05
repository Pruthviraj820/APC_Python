a = float(input())
b = float(input())
p = (a / b) * 100
if p >= 90:
    print("Excellent performance")
elif p >= 80:
    print("Very Good performance")
elif p >= 70:
    print("Good performance")
elif p >= 60:
    print("Average performance")
else:
    print("Poor performance")
