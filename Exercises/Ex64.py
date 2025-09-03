def reverse(n):
    return ' '.join(word[::-1] for word in n.split())

n = input()
result = reverse(n)
print(result)