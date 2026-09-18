inv = 0
mistake = 0

while True:
    stock = input("Enter Stock Quantity or 'Quit': ")
    if stock.isdigit() == True:
         if inv < 500:
              inv = inv + int(stock)
              print("Current Inventory: " + str(inv))
         else:
              print("Alert! Inventory exceeds 500!")  
              break
    elif stock.lower() == "quit":
         print("Total Units Processed: " + str(inv) + " Numnber of failed Entries: " +  str(mistake) + ".")
         break
    else:
         mistake += 1 
         print("Error, input is not a number not 'Quit'. Please try again.")



    
    

