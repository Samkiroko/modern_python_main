"""
Louis wants to open a Pizza 🍕 Shop and needs to write
a program for accepting orders.

Tip -
-----
Always Visualize First, Then Start Coding.
"""

# -----------------------------------------------
# Variable Declaration
# -----------------------------------------------

customer: str = "Cece"
pizza_base: str = "Thin"
pizza_size: int = 12
topping: str = "Olives"
extra_cheese: bool = True
price: float = 8.99

# -----------------------------------------------
# Alternative 1 - Using Print Function
# -----------------------------------------------

# print(f"Receive order from : {customer}")
# print(f"Pizza Base: {pizza_base}, Size {pizza_size} inches, Topping: {topping}")
# print(f"Is Extra Cheese require: {extra_cheese}")
# print(f"Bill Amount: {price}")


# -----------------------------------------------
# Alternative 1 - Using Formatted String
# -----------------------------------------------

order_details: str = f"""
Receive order from : {customer}
Pizza Base: {pizza_base}, Size {pizza_size} inches, Topping: {topping}
Is Extra Cheese require: {extra_cheese}
Bill Amount: {price}
"""
print(order_details)


# -------------------------------------------------
# Alternative 1 - Using Formatted String in `print`
# -------------------------------------------------

print(
    f"""
Receive order from : {customer}
Pizza Base: {pizza_base}, Size {pizza_size} inches, Topping: {topping}
Is Extra Cheese require: {extra_cheese}
Bill Amount: {price}
"""
)
