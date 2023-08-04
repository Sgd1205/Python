#to reverse a number 
num = int(input("Enter number: "))
print("Number: ",num)
rev_num = 0
#to reverse number
while num > 0:
    remainder = num % 10
    rev_num = (rev_num*10) + remainder
    num //=10

print ("Reversed number: ",rev_num)