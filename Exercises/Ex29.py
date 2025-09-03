a = int(input())

for i in range(1, a + 1):
    result = a / i
    if a % i == 0:
        print(f"{a} % {i} =", result)