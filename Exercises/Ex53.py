def sum_1_to_10(n):
    sum = 0 
    for i in range(1, n + 1):
        sum += i
    return sum

n = int(input())
result = sum_1_to_10(n)
print(result)