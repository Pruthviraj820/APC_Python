try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result:", y)
except ValueError:
    print("Oops! That’s not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This always runs, no matter what.")