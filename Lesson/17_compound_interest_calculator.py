# Python compound interest calculator
# cong thuc tinh = A = P(1 + r/n)**t
# A = trial amount 
# P = initial principal balance
# r = number of time period elapsed

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the priciple amount: "))
    if principle < 0:
        print("Principle cam't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("rate can't be less than  zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("time can't be less than zero")
    else:
        break


total = principle * pow((1 + rate /100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
