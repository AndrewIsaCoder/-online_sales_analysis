from product_manager import ProductManager

manager = ProductManager()

manager.adauga_produs("Laptop", 1500.99, 28)  # Use adauga_produs
manager.adauga_produs("Smartphone", 800.0, 10)
manager.adauga_produs("Headphones", 150.0, 20)

print("\nProducts in the inventory:")
manager.afisare_toate_produsele()

manager.afisare_valoare_totala()