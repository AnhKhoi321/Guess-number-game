a = int(input())
b = int(input())

for i in range(1, min(a,b) + 1):
        result = a / i
        result2 = b / i
        if a % i == 0 and b % i == 0:
            print(f"{a} / {i} = {result}")
            print(f"{b} / {i} = {result2}")