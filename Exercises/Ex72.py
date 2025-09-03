def add_product(product, amount=1):
    return product, amount

product = input()
amount_input = input()
if amount_input:
    amount = int(amount_input)
else:
    amount = 1
    
print(add_product(product, amount))
