#string formatting

print ("hello","world")
print ("hello","world", sep = '') #if you dont want the space

print ("hello","world",sep = '***', end = '>>>\n')

name = "advay"
age = 18

print(name,"is",age,"years old")
print("%s is %d years old" %(name, age))

#other formatting tools

price = 6
item = 'banana'

print(item, "is", price, "rupees")
print(item,"is %5.2f rupees" %(price)) 

itemdect = {"item":"banana", "cost":6}

print("the %(item)s costs %(cost)5.1f rupees" %(itemdect))

#f strings
print('----------------------------------')

print (f"the {item:10} costs {price:10.2f} rupees")
print (f"the {item:>10} costs {price:<10.2f} rupees")
print (f"the {item:^10} costs {price:^10.2f} rupees") # ^ is for center

print (f"Item:{itemdect['item']:>10}\n" + f"Price:{itemdect['cost']:9.2f}")