# List created that has our menu items defined
menu = ["Tea", "Coffee", "Burger", "Kebab"]  

# Dictionary created that stores the quantity for each menu item
stock = {"Tea": 1334, 
         "Coffee": 1434, 
         "Burger": 1000, 
         "Kebab": 1423}

# Dictionary created that stores the price for each menu item
price = {"Tea": 2.55, 
         "Coffee": 3.49, 
         "Burger": 5.99, 
         "Kebab": 8.50}

# Initialising a variable to keep track of the total stock value 
total_stock = 0

# The 'for' loop iterates through each menu item
for key in menu:
    # By multiplying each item's stock quantity by the item's price we get the total value of the items we have in our menu
    item_value = stock[key] * price[key]
    # Adds the value of the current menu item to the total stock value 
    total_stock += item_value 

# Displays the total value of all the items that are in the menu
print (f"The total stock value in the cafe is: £{total_stock:.2f}")