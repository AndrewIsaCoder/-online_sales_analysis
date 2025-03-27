from product_manager import ProductManager

manager = ProductManager()

manager.add_product("Laptop", 1500.99 , 28)
manager.add_product("Smartphone", 800.0, 10)
manager.add_product("Headphones", 150.0, 20)

print("\n Products in the inventory:")
manager.afisareZ_toate_produsele()

print("\n Total value of the products in stock:")
manager.afisare_valoare_totala()
