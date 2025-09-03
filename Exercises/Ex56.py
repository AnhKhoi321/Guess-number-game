def giai_thua(n):
    num = 1 
    for i in range(1, n + 1):
        num *= i
    return num

n = int(input())
result = giai_thua(n)
print(result)