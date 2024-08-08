a = int(input("enter 1 number :"))
b = int(input("enter 2 number :"))
c = int(input("enter 3 number :"))

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c
print(f"The largest number is {largest}")
