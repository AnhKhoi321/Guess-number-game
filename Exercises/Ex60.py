def max(n):
    max_n = n[0]
    for i in n:
        if i > max_n:
            max_n = i
    return max_n

n = [1,2,3,4,5,6,7,8]
result = max(n)
print(result)