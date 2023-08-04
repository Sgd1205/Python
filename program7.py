#to concatenate a dictionary to a new one 
dic1 = {1:"Apple",2:"Banana"}
dic2 = {3:"Cherry",4:"Mango"}
d1 = list(dic1.items())
d2 = list(dic2.items())
print(d1)
print(d2)
d3= d1+d2
print(d3)
