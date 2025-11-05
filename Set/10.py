try:
    n=int(input("enter number="))
    print(1/n)
except ZeroDivisionError:
    print("zero not allowed")
except ValueError:
    print("alphabet not allowed")
finally:
    print("everything executed")