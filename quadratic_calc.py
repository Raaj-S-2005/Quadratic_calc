import math
#Ask for the three nunmbers (a, b, c)
a = float(input("What is a: "))

b = float(input("What is b: "))

c = float(input("what is c: "))

#Spacing
print("")
print("")

#Solve for the part inside the square_root
d = b ** 2 - (4 * a *c)

#If the part inside the square root is more than 0 then add/subtract with -b
if d > 0:
    a1 = (-(b) + math.sqrt(d)) / (2 * a)
    a2 = (-(b) - math.sqrt(d)) / (2 * a)
    #Print answers
    print(f"a1: {a1:.3f}")
    print(f"a2: {a2:.3f}")
        

#if the part inside the square_root is 0, then add/subtract with -b
elif d == 0:
    a1 = (-(b) + d) / (2 * a)
    a2 = (-(b) - d) / (2 * a)
    #Print answers
    print(f"a1: {a1:.3f}")
    print(f"a2: {a2:.3f}")

#If the part inside the square root is less than zero, then disaply that there are no root possible
else:
    print("No roots for this question!")

