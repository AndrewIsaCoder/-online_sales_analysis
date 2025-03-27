class Product():
    def __init__ (self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def afisare_informatii_produs(self): #afisare informatii produs
        print(f"Product name: {self.name}\nProduct price: {self.price}\n Product quantity {self.quantity}")
        
    def actualizare_cantitate_produs(self):
        a = input("Do you want to update the product quantity? (yes/no):")
        if a == "yes":
            self.quantity = int(input("Enter the new quantity:"))
            print(f"Procut quantity is updated to {self.quantity} products")
        else:
            print("Product quantity remains the same.")
