"""
Program Name: Lab 6
My name: Ishan Agarwal
Purpose: This lab is meant to deepen my understanding of dictionaries.
Starter Code: None
Date: 02/20/2026
"""

my_cart: dict[str, int] = {}

# Introduction + Instructions
print("Welcome to the store!")
print("Enter an item, or type 'view' to see your cart, or 'checkout' to finish.")
print("")

while True:
    # Ask about what action they take
    item: str = input("What would you like? ").lower().strip()

    # Check if they checkout
    if item == "checkout":
        break

    # Check if they want to view their cart
    elif item == "view":
        print("")
        print("-- YOUR CART --")
        if not my_cart:
            print("Your cart is empty.")
        else:
            for key, value in my_cart.items():
                print(f"{key}: {value}")
        print("---------------")
        print("")

    # Adding item to cart option
    else:
        item_quantity: int = int(input("How many? "))

        # Add item + Quantity to cart
        if item in my_cart:
            my_cart[item] += item_quantity
        else:
            my_cart[item] = item_quantity
        
        print(f"> {item_quantity}x {item} added to cart.")
        print("")

print("")

# Final Cart Conclusion
print("-- FINAL CART --")
if not my_cart:
    print("Your cart is empty.")
else:
    for key, value in my_cart.items():
        print(f"{key}: {value}")
print("---------------")

print("")

print("Thank you for shopping!")