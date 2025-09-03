def sum_even(n):
    sum = 0
    for i in n:
        if i % 2 == 0:
            sum += i
    return sum

n = [1, 2, 3, 4, 5, 6]
result = sum_even(n)
print(result)