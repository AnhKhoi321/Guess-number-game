def nam_nhuan(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 ==0):
        return True
    else:
        return False
    
n = int(input())
if nam_nhuan(n):
    print(f"{n} là năm nhuận")
else: 
    print(f"{n} ko phải là năm nhuận") 