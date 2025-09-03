import random
def password(n):
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%", k = n))


n = int(input())
print(password(n))
