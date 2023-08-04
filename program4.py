#to find greatest number among the entered three numbers taken from user 
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

if num1>num2 and num1>num3:
    print(num1, " is the greatest among the entered numbers")
elif num2>num1 and num2>num3:
    print(num2 ," is the greatest among the entered numbers")
else:
    print(num3, " is the greatest among the entered numbers")