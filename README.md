# Online Sales Analysis

## Overview
The **Online Sales Analysis** program is a Python-based application designed to manage an inventory of products and simulate a shopping cart system. It allows users to add, display, and remove products from the inventory, calculate the total value of the inventory, and manage a customer's shopping cart. This program is ideal for learning and practicing object-oriented programming concepts in Python.

---

## Features
### 1. **Product Management**
- Add new products to the inventory.
- Display all available products with their details (name, price, quantity).
- Remove products from the inventory by name.
- Calculate the total value of all products in the inventory.

### 2. **Shopping Cart Management**
- Add products from the inventory to the shopping cart.
- Display the contents of the shopping cart.
- Calculate the total value of the shopping cart.

---

## Classes and Their Responsibilities

### 1. **`Product` Class**
Represents a single product in the inventory.
- **Attributes**:
  - `name`: The name of the product.
  - `price`: The price of the product.
  - `quantity`: The quantity of the product in stock.
- **Methods**:
  - `afisare_informatii_produs`: Displays the product's details.
  - `actualizare_cantitate_produs`: Updates the quantity of the product.

### 2. **`ProductManager` Class**
Manages the inventory of products.
- **Attributes**:
  - `products`: A list of all products in the inventory.
- **Methods**:
  - `adauga_produs`: Adds a new product to the inventory.
  - `afisare_toate_produsele`: Displays all products in the inventory.
  - `sterge_produs`: Removes a product from the inventory by name.
  - `afisare_valoare_totala`: Calculates and displays the total value of all products in the inventory.

### 3. **`Cart` Class**
Manages the customer's shopping cart.
- **Attributes**:
  - `cart_items`: A list of products added to the cart.
- **Methods**:
  - `add_to_cart`: Adds a product to the cart.
  - `calculate_total`: Calculates the total value of the cart.
  - `display_cart`: Displays the contents of the cart.

---

## How to Use

### 1. **Run the Program**
To run the program, execute the `main.py` file:
```bash
python [main.py](http://_vscodecontentref_/1)