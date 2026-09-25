def load_inventory():
     with open("inventory.txt", "w+") as file:
          inventory = file.readlines()
     return inventory

def process_delivery(current_total,new_value):
          current_total = current_total + new_value
          print("Current Inventory: " + str(current_total))
          return current_total

def calculate_tax(amount):
     amount = amount * 0.1
     print("You are taxed $" + str(round(amount,2)) + ".")

def generate_report(total_units, failed_attempts):
     print("Total Units Processed: " + str(total_units) + " Numnber of failed Entries: " +  str(failed_attempts) + ".")

def save_inventory(inventory):
     with open("inventory.txt", "w") as file:
          file.writelines(inventory)

def get_valid_input():
     failed_attempts = 0
     total = 0
     transaction = load_inventory()
     UID = 1000
     while True:
          stock = str(input("Enter Stock Quantity or 'Quit': "))
          if stock.isdigit() == True:
               if total < 500:
                    UID += 1
                    transaction.append(f"{UID}, 1{stock}\n")
                    total = process_delivery(total, int(stock))
                    calculate_tax(int(total))
                    save_inventory(transaction)
               else:
                    print("Alert! Inventory exceeds 500!")
               continue
          elif stock.lower() != "quit":
               failed_attempts += 1
               print("Error, input is not a number not 'Quit'. Please try again.")
               continue
          else:
               generate_report(total, failed_attempts)
               break

get_valid_input()