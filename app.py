import sys
import os
import proj_fun
def clear():
    os.system( 'cls' )


print('Welcome to the app!\n')
products = []
couriers = []
orders = [
    {
        "Name": "Tom",
        "Address": "123 Random Rd",
        "Phone Number": "12345678901",
        "Status": "Preparing"
    },
    {
        "Name": "Ella",
        "Address": "134 Normal Rd",
        "Phone Number": "12565754678901",
        "Status": "Preparing"
    },
    {
        "Name": "Jack",
        "Address": "1 Strange Street",
        "Phone Number": "123128901",
        "Status": "Preparing"
    }
]
# Opens products file and appends stored product names to empty product list above.
with open("products.txt", "r") as products_file:
    for product in products_file.readlines():
        products.append(product.strip())
# Opens couriers file and appends stored courier names to empty courier list above.
with open("couriers.txt", "r") as couriers_file:
    for courier in couriers_file.readlines():
        couriers.append(courier.strip())
while True:
    print("Press... \n 0 to exit the app \n 1 to show Product Menu \n 2 to show Courier Menu \n 3 to show Order Menu")
    value = int(input("Select a Main Menu option "))
    clear()
    if value == 0:
        print("Thank you for using the app!")
        with open("products.txt", "w") as product_file:
            for product in products:
                product_file.write(product + "\n")
        with open("couriers.txt", "w") as couriers_file:
            for courier in couriers:
                couriers_file.write(courier + "\n")
        sys.exit(0)
    elif value == 1:
        product_menu = True
        # This keeps the user in the products menu until they choose to leave.
        while product_menu == True:
            print("Press... \n 0 to exit the app"
                  + "\n 1 to see products" 
                  + "\n 2 to add a new product" 
                  + "\n 3 to update an existing product"
                  + "\n 4 to delete a product"
                  + "\n 5 to return to Main Menu\n")
            product_value = int(input("Select a Product Menu option: "))
            clear()
            if product_value == 0:
                print("Thank you for using the app!")
                with open("products.txt", "w") as product_file:
                    for product in products:
                        product_file.write(product + "\n")
                with open("couriers.txt", "w") as couriers_file:
                    for courier in couriers:
                        couriers_file.write(courier + "\n")
                sys.exit(0)
            elif product_value == 1:
                print("Products:\n")
                print(products)
                print("\n")
            elif product_value == 2:
                proj_fun.add_product(products)
            elif product_value == 3:
                proj_fun.update_product(products)
            elif product_value == 4:
                proj_fun.delete_product(products)
            elif product_value == 5:
                # Exits the products menu and returns the user to the main menu
                product_menu = False
            else:
                print("Sorry, this is not an option.\n")
    elif value == 2:
        courier_menu = True
        while courier_menu == True:
            print("Press... \n 0 to exit the app"
                  + "\n 1 to see couriers" 
                  + "\n 2 to add a new courier" 
                  + "\n 3 to update an existing courier"
                  + "\n 4 to delete a courier"
                  + "\n 5 to return to Main Menu\n")
            courier_value = int(input("Select a Courier Menu option: "))
            clear()
            if courier_value == 0:
                print("Thank you for using the app!")
                with open("products.txt", "w") as product_file:
                    for product in products:
                        product_file.write(product + "\n")
                with open("couriers.txt", "w") as couriers_file:
                    for courier in couriers:
                        couriers_file.write(courier + "\n")
                sys.exit(0)
            elif courier_value == 1:
                print("Couriers:\n")
                print(couriers)
                print("\n")
            elif courier_value == 2:
                proj_fun.add_courier(couriers)
            elif courier_value == 3:
                proj_fun.update_courier(couriers)
            elif courier_value == 4:
                proj_fun.delete_courier(couriers)
            elif courier_value == 5:
                # Exits the Courier Menu and returns user to the Main Menu
                courier_menu = False
            else:
                print("Sorry, this is not an option.\n")
    elif value == 3:
        order_menu = True
        while order_menu == True:
            print("Press... \n 0 to exit the app"
                  + "\n 1 to see orders"
                  + "\n 2 to create new order"
                  + "\n 3 to update order status"
                  + "\n 4 to update order"
                  + "\n 5 to delete order"
                  + "\n 6 to return to Main Menu\n")
            order_value = int(input("Select an Order Menu option: "))
            clear()
            if order_value == 0:
                print("Thank you for using the app!")
                with open("products.txt", "w") as product_file:
                    for product in products:
                        product_file.write(product + "\n")
                with open("couriers.txt", "w") as couriers_file:
                    for courier in couriers:
                        couriers_file.write(courier + "\n")
                        sys.exit(0)
            elif order_value ==1:
                print("Orders:\n")
                print(orders)
                print("\n")
            elif order_value == 2:
                proj_fun.create_new_order(orders, couriers)
            elif order_value == 3:
                proj_fun.update_order_status(orders)
            elif order_value == 4:
                proj_fun.update_order(orders)
            elif order_value == 5:
                proj_fun.delete_order(orders)
            elif order_value == 6:
                order_menu = False
            else:
                print("Sorry this is not an option.\n")



#When exiting the app from the orders menu, couriers list is reduced to only the first entry