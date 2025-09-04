#Shopping cart
products = []
def shopping_cart(product_name, amount):
        product = {
        "Tên": product_name,
        "Số lượng": amount
        }
        products.append(product)

def show_shopping_cart():
    for i, product in enumerate(products, 1):
        print(f"{i}. Name: {product['Tên']} | Amount: {product['Số lượng']}") 
def delete_shopping_cart(name_to_delete):
    try:
        for product in products:
            if product['Tên'] == name_to_delete:
                products.remove(product)
                print(f"Deleted {name_to_delete}")
                return
        raise IndexError("The product you enter doesn't exist")
    except IndexError as e:
            print("Invalid", e)

#Add product

while True:
    print("Add the products you want to buy!!!")
    product_name = input("Product's name: ")
    amount = int(input("How many do you want?: "))
    shopping_cart(product_name,amount)
    stop = input("Do you want to continue?(stop to finish): ")
    if stop.lower() == "stop":
            break               

#Show the cart

print("\nYour shopping cart: ")
show_shopping_cart()

#Delete product

while True:
    delete_product = input("Enter the product you want to remove: ")
    if delete_product.lower() == "stop":
         break
    delete_shopping_cart(delete_product)

#Show the updated cart

print("\n Your shopping cart: ")
show_shopping_cart()