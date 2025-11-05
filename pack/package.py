#without init file
import my_package.rectangle 

len = float(input("Enter the length of the Rectangle:"))
wid = float(input("Enter the width of the Rectangle: "))

ar = my_package.rectangle.area(len,wid)
peri = my_package.rectangle.perimeter(len,wid)

print("The area of the Rectangle is:",ar)
print("The perimeter of the Rectangle is:",peri)

