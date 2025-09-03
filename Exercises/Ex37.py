n = int(input())
if n == -1:
    print("Stop")
else:
    max_n = n
    min_n = n


while True:
    n = int(input("Enter the number: "))
    if n == -1:
        print("Stop")
        break
    if n > max_n:
        max_n = n
    if n < min_n:
        min_n = n
print(max_n)
print(min_n)


