"""
Write program that will take a number (Integers only) and
return a statement that will let the user know if it is even or odd
"""
x = int(input("To determine if even or odd, insert INTEGER here: "))
if x % 2 == 0:
    print(x, "is an even number.")
elif x % 2 == 1:
    print(x, "is an odd number.")
else:
    print("Cmon man you didn't put in an INTERGER...")