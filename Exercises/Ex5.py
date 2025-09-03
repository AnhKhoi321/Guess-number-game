a = int(input("Enter a number: "))

if a % 3 == 0 and a in range(50, 101):
    print(True)
else:
    print(False)