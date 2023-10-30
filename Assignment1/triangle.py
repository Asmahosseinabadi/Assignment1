print("Enter 3 numbers for making a triangle ")
first=float(input("enter the first number:"))
second=float(input("enter the second number:"))
third=float(input("enter the third number:"))

if first<second+third and second<first+third and third<first+second :
    print("yes you can make a triangle")
else:
    print("No,you cannot make a triangle with this numbers")
