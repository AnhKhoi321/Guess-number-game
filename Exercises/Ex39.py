count = 0
num = int(input("Enter number: "))
while num != 0:
    num = int(input())
    if num % 2 == 0:
        count+= 1
    elif num == 0:
        count +=0
print(count)