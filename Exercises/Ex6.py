a = int(input("Enter a number: "))

if a % 5 == 0 and a not in range(20, 71):
    print(True)
else: 
    print(False)