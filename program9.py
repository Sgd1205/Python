#to find percentage of six subjects 
sub1 = int(input("Enter Subject 1 marks: "))
sub2 = int(input("Enter Subject 2 marks: "))
sub3 = int(input("Enter Subject 3 marks: "))
sub4 = int(input("Enter Subject 4 marks: "))
sub5 = int(input("Enter Subject 5 marks: "))
sub6 = int(input("Enter Subject 6 marks: "))

total = 600 #total marks 
stu_total = sub1+sub2+sub3+sub4+sub5+sub6 #student total

percentage = (stu_total/total)*100

print("Percentage of student: ",percentage)