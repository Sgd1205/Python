#to check the number of days in a month by taking month and year input from user 
year = int(input("Enter year: "))
month = input("Enter month: ")

if month in ('January, March, May, July, August, October, December'):
    print("Number of days: 31")
elif month in ('April, June, September, November'):
    print("Number of days: 30")
elif month in ('February'):
    if year%4==0:
        print("Number of days: 29")
    else:
        print("Number of days: 28")
else:
    print("Invalid Month entered")
