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
                
    def sterge_produs(self, name):
        for produs in self.products:
            if produs.name == name:
                self.products.remove(produs)
                print(f"Product '{name}' has been removed.")
                return
        print(f"Product {name}not found.")

    def afisare_valoare_totala(self):  # Correctly indented
        total_value = sum(produs.price * produs.quantity for produs in self.products)
        print(f"TOTAL VALUE OF THE PRODUCTS IN STOCK: {total_value}")
                
