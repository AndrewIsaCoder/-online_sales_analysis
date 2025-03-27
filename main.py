from product_manager import ProductManager
from cart import Cart as cart

manager = ProductManager()

manager.adauga_produs("Laptop", 1500.99, 28)  # Use adauga_produs
manager.adauga_produs("Smartphone", 800.0, 10)
manager.adauga_produs("Headphones", 150.0, 20)

print("\nProducts in the inventory:")
manager.afisare_toate_produsele()

manager.afisare_valoare_totala()

from product_manager import ProductManager

# Create an instance of ProductManager
manager = ProductManager()

while True:
    print("\nOptions:")
    print("1. Add product")
    print("2. Display all products")
    print("3. Display the total value of all the products in the stock")
    print("4. Remove a product")
    print("5. Exit")
    
    choice = input("Choose an option (1, 2, 3, 4, 5): ")
    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        manager.adauga_produs(name, price, quantity)
    elif choice == "2":
        manager.afisare_toate_produsele()
    elif choice == "3":
        manager.afisare_valoare_totala()
    elif choice == "4":
        name = input("Enter the name of the product to remove: ")
        manager.sterge_produs(name)
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")
        
        
cart.add_to_cart(manager.products[0])  # Add Laptop
cart.add_to_cart(manager.products[1])  # Add Smartphone
cart.add_to_cart(manager.products[2])  # Add Headphones

# Display the cart contents
cart.display_cart()

# Display the total value of the cart
total = cart.calculate_total()
print(f"\nTotal value of the cart: {total:.2f}")