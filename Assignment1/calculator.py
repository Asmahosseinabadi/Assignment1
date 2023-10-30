import math
print("Hi,welcome to my calculator")
print("+ : sum")
print("- : sub")
print("* : mul")
print("/ : divide")
print("sin")
print("cos")
print("tan")
print("cot")
print("log")
print("sqrt")
print("factorial")
print("enter your choice:")
op=input()
if op=="+"or op=="-"or op=="*"or op=="/":
    a=float(input("enter the first number:"))
    b=float(input("enter the second number:"))
elif op=="factorial":
    a=int(input("enter your number:"))
elif op=="sin"or op=="cos"or op=="tan"or op=="cot":
    a=float(input("enter your number:"))
    a=a*math.pi/180
else  :
    a=float(input("enter the number:"))

if op=="+":
    result=a+b
elif op=="-":
    result=a-b
elif op=="*":
    result=a*b
elif op=="/":
    if b==0:
        result="cannot do this divide"     
    else:
        result=a/b


elif op=="log":
    result=math.log(a)

elif op=="sqrt":
    result=math.sqrt(a)

elif op=="factorial":
    result=math.factorial(a)

elif op=="sin":
    result=math.sin(a)

elif op=="cos":
    result=math.cos(a)

elif op=="tan":
    result=math.tan(a)

elif op=="cot":
    result=1/math.tan(a)


print(result)
