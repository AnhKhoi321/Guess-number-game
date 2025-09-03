# n = int(input())

# if n < 2:
#     is_Prime = False
# else: 
#     i = 2 
#     is_Prime = True
#     while i < n:
#         if n % i == 0:
#             is_Prime = False
#             break
#         i += 1
# if is_Prime:
#     print(f"{n} là số nguyên tố")
# else: 
#     print(f"{n} ko phải là số nguyên tố")

n = int(input())

if n < 2:
    is_Prime = False
else: 
    i = 2 
    is_Prime = True
    while i < n:
        if n % i == 0:
            is_Prime = False
            break
        i += 1

if is_Prime:
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} ko phải là số nguyên tố ")

