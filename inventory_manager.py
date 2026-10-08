__MAINLINE__ = "=" * 20
__SUBLINE__ = "-" * 6

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            print("inventory.json found.\nInventory loaded successfully.")
            inventory = file.readlines()
            return inventory
    except FileNotFoundError:
        inventory = open("inventory.txt", "x")
        return inventory

def add_product():
    newProduct = [{}]
    while True:
        newProduct[{"ID"}] = input("Add New Product\nProduct ID: ")
        newProduct[{"Name"}] = input("Product Name: ")
        newProduct[{"Price"}] = float(input("Price: $"))
        newProduct[{"Stock"}] = int(input("Stock Quantity: "))
        break
    with open("inventory.json", "w") as file:
        return

def update_stock():
    return

def search_product():
    return

def display_all():
    return

def save_inventory():
    with open("inventory.json", "w") as file:
            file.writelines()
            print("Transaction succesfully saved to inventory.json.")

def menu():
    print(__MAINLINE__+"\nINVENTORY MANAGEMENT SYSTEM\n"+__MAINLINE__+"\n")
    load_inventory()
    while True:
        choice = input("\n"+__SUBLINE__+"MENU"+__SUBLINE__+"\n1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit\n"+__SUBLINE__*3+"\n\nEnter Option:")
        if choice == "1":
            display_all()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            search_product()
        elif choice == "5":
            save_inventory()
        else:
            print("Exiting... Thank you.")
            break

menu()