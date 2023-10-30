name=input("enter your name:")
family_name=input("enter your family name:")
score1=float(input("enter the first score:"))
score2=float(input("enter the second score:"))
score3=float(input("enter the third score:"))
average=(score1+score2+score3)/3
if average >= 17:
    print("Great")
elif average<17 and average>=12:
    print("Normal")
elif average<12:
    print("Fail")
