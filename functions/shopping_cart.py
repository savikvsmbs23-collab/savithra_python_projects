cart = [
    {"item": "Apple", "price": 1.50, "quantity": 3},
    {"item": "Bread", "price": 2.00, "quantity": 1},
    {"item": "Milk", "price": 1.20, "quantity": 2},
]



def print_cart(cart):
    for product in cart:
        print(f"{product['item']} x{product['quantity']} = ${product['price'] * product['quantity']}")

def calculate_total(cart):
    total = 0
    for product in cart:
        total += product['price'] * product['quantity']
    return total

def apply_discount(total):
    if total > 10:
        total = total * 0.9
        return round(total, 2)

    else:
        return total


# Print all items in cart

print("--- Your Cart ---")
print_cart(cart)

# Calculate total
print(f"Total: ${calculate_total(cart)}")

# Apply 10% discount if total > 10
total = calculate_total(cart)
final = apply_discount(total)
if final == total:
    print("No discount applicable")
else:
    print(f"Discounted total: ${final}")

