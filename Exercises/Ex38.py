num = input("Enter number: ")
total = 0
while True:
    if num == 0:
        print("Stop")
        break
    else:
        num = int(input("Continue: "))
    total += num
print(total)