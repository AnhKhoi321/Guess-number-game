def palindrome(n):
    return str(n) == str(n)[::-1]

n = str(input())
result = palindrome(n)
print(result)