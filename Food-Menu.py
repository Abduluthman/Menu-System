# A menu that uses lists to take users inputs for their orders and totals the amount and presents a reciept for them
print("Welcome to Meusse De Restaurant")
print("This is our Menu: ")
# Creating a dictionary that stores our menu, it uses a key:value combo that stores a menu-item:price
print("-----Meusse De Restaurant-----")
Menu = {
    'Water': 10.00, 
    'Sparkling Water': 12.00, 
    'Red Bull': 7.99, 
    'Coke-Cola': 9.99,
    'Beef Cheese Sandwich': 15.00, 
    'Grilled Chicken Sandwich': 16.00, 
    'Egg Salad Sandwich': 18.00,
    'Orange Juice': 6.99,
    'Fresh Lemonade': 7.50,
    'French Fries': 4.50,
    'Calamari': 9.99,
    'Fish & Chips': 12.00,
}
# This is a for loop that loops through the Menu dictionary and prints out every key:value element
for item in Menu:
    print(item, Menu[item])
print("-------------------------")
# An empty list that stores the users order
userOrderList = []

# Asking the user if they are ready to order, if they enter yes it proceedes to the while loop
userChoice = input("Would you like to order(YES/NO): ").upper()
# Creating a variable that keeps track of what item in the dictionary the user orders, and uses it to access the dictionary and retrieve the price
userOrder = None

# A while loop that would continue to iterate as long as the user wants to order (userChoice == "YES")
while(userChoice == "YES"):
    # Taking input of what the user would want to order and the quanitity of that item the user would like to order
    userOrder = input("What would you like to order: ") 
    quantity = int(input("How many would you like to order: "))

    # UserMenuPrice saves the price of the item the user has chosen on the menu
    userMenuPrice = Menu[userOrder] 
    # This creates a list with the 0th item being what the user ordered, the 1st item being the price of the item they ordered, 2nd item being the quantity of that item that they ordered
    userMenuList = [userOrder, userMenuPrice, quantity]

    # The item the user ordered is added to the list userOrderList
    userOrderList.append(userMenuList)

    # This prints a running sum of the your total
    print("This is what your current total: ", userMenuList[1] * userMenuList[2])

    # This asks if the user would like to order anything else, if the user inputs yes the loop continues, if no the loop breaks and prints the next line 
    userChoice = input("Would you like to order anything else(YES/NO): ")

#We find the sum of the product of index 1, which is the price of what the user ordered and index 2 which is the quantity of what the user ordered. 
totalAmount = sum(item[1] * item[2] for item in userOrderList)


print("-----Reciept-----") 
for item in userOrderList: #This is a for loop that goes through items stored in userOrderList, index 0 is what the user ordered, index 1 is the price of the item the user ordered, index 2 is the quantity the user ordered.
    print(f"{item[0]} x{item[2]}: £{item[1] * item[2]}") #Using output formatter we arrange our outputs to look like that of a menu
# This prints the total
print("Your total is: ", totalAmount)
