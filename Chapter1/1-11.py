import math

#while(1):
#    x = int(input("enter number: "))
#    try:
#        print(math.sqrt(x))
#    except:
#        print("printing the absolute value instead")
#        print(math.sqrt(abs(x)))

while(1):
    x = int(input("enter number: "))
    if x < 0:
        raise RuntimeError("you cant use a negative integer")
    else:
        print(math.sqrt(x))

