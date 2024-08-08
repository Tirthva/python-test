number = int(input("enter a number: "))
a, b = 0, 1

print(f"{number} number:")

for i in range(number):
    print(a)
    a, b = b, a + b
