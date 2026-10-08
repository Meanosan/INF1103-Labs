inventory = [{
    "UID": str,
    "Name": str,
    "Price": float,
    "Stock": int
}]

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
    return

def update_stock():
    return

def search_product():
    return

def display_all():
    return

def save_inventory():
    return

def menu():
    __MAINLINE__ = "=" * 12
    __SUBLINE__ = "-" * 4
    print(__MAINLINE__+"\nINVENTORY MANAGEMENT SYSTEM\n"+__MAINLINE__+"\n\n")
    load_inventory()
    while True:
        choice = input(__SUBLINE__+"MENU"+__SUBLINE__+"\n1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit"+__SUBLINE__*2+"\n\nEnter Option:")
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