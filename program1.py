#simple calculator 
print("Add=1, Subtract=2, Multiple=3, Divide=4")
c = int(input("Enter choice(1-4): "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if c==1:
    sum = a+b
    print("Addition: ",sum )
elif c==2:
    sub = a-b
    print("Subtraction: ",sub)
elif c==3:
    mult = a*b
    print("Multiplication: ",mult)
elif c==4:
    div = a/b
    print("Division: ",div)
else:
    print("Invalid choice")