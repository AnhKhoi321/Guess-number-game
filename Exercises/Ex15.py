a = float(input())
b = float(input())
c = float(input())

sum1 = a + b
sum2 = b + c
sum3 = a + c
if sum1 > c and sum2 > a and sum3 > b:
    print("These numbers can form a triangle")
else:
    print("These numbers can't form a triangle")