class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Product '{product.name}' added to the cart.")

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.cart_items)
        return total

    def display_cart(self):
        if not self.cart_items:
            print("The cart is empty.")
        else:
            print("\nCart Contents:")
            for item in self.cart_items:
                print(f"Product name: {item.name}, Price: {item.price}, Quantity: {item.quantity}")