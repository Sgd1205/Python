#to print fibonacci series 
print("Fibonacci series")
term1=0
term2=1
nextterm=term1+term2
n = int(input("Enter the number of terms to be printed: "))
print(term1)
print(term2)
for i in range(2,n):
    term1=term2
    term2=nextterm
    nextterm=term1+term2
    print(nextterm)