import product as p

class ProductManager:
    def __init__(self):
        self.products = []  # List to store products

    def adauga_produs(self, name, price, quantity):  # Correctly indented
        produs = p.Product(name, price, quantity)
        self.products.append(produs)
        print(f"Product '{name}' added successfully.")

    def afisare_toate_produsele(self):  # Correctly indented
        if not self.products:
            print("No products available.")
        else:
            for produs in self.products:
                produs.afisare_informatii_produs()

    def afisare_valoare_totala(self):  # Correctly indented
        total_value = sum(produs.price * produs.quantity for produs in self.products)
        print(f"TOTAL VALUE OF THE PRODUCTS IN STOCK: {total_value}")
                
if __name__ == "__main__":
    manager = ProductManager()
    
    while True:
        print("\nOptions:")
        print("1. Add product")
        print("2. Display all products")
        print("3. Display the total value of all the products in the stock")
        print("4. Exit")
        
        choice = input("Choose an option (1, 2, 3, 4): ")
        if choice ==  "1":
            name = input("Enter product name:")
            price = float(input("Enter product price:"))
            quantity = int(input("Enter product quantity:"))
            manager.add_product(name , price , quantity)
        elif choice == "2":
            manager.afisare_toate_produsele()
        elif choice == "3":
            manager.afisare_valoare_totala()
        elif choice == "4":
            print("Cloing the program...")
            break
        else:
            print("Invalid option . Please try again.")