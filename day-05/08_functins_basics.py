
def order(menu):
    print(f"Order placed: your order is {menu}")


def calculate_total(menu):
    base_price = 25.5
    VAT = 0.15

    totalPrice = (base_price + len(menu)) * (1 + VAT)
    return totalPrice


def get_order():
    print("Preparing order...")
    return "Collect your order"


myFood = input("What would you like to order? ")

order(myFood)

total = calculate_total(myFood)
print(f"Your total, including VAT, is R{total:.2f}")

print(get_order())
