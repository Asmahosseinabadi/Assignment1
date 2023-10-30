weight=float(input("enter your weight in kg: "))
height=float(input("enter your height in m: "))

BMI=weight/height**2
if BMI<=18.5:
    print("underweight")
elif BMI>18.5 and BMI<=24.9:
    print("normalweight")
elif BMI>=25 and BMI<=29.5:
    print("overweight")
elif BMI>=30 and BMI<=34.9:
    print("obesity")
elif BMI>=35 and BMI<=39.9:
    print("extreme obesity")
