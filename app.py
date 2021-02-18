import sys
import os
import pymysql
import proj_fun
def clear():
    os.system( 'cls' )
    
print('Welcome to the app!\n')

while True:
    print("Press... \n 0 to exit the app \n 1 to show Product Menu \n 2 to show Courier Menu \n 3 to show Order Menu")
    str_value = (input("Select a Main Menu option "))
    clear()
    if str_value.isdigit():
        value = int(str_value)
        if value == 0:
            print("Thank you for using the app!")
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
                str_product_value = (input("Select a Product Menu option: "))
                clear()
                if str_product_value.isdigit():
                    product_value = int(str_product_value)
                    if product_value == 0:
                        print("Thank you for using the app!")
                        sys.exit(0)
                    elif product_value == 1:
                        proj_fun.show_products()
                    elif product_value == 2:
                        proj_fun.add_product()
                    elif product_value == 3:
                        proj_fun.update_product()
                    elif product_value == 4:
                        proj_fun.delete_product()
                    elif product_value == 5:
                        # Exits the products menu and returns the user to the main menu
                        product_menu = False
                    else:
                        print("\nSorry, this is not an option.\n")
                else:
                    print("\n Sorry, input needs to be an integer\n")
        elif value == 2:
            courier_menu = True
            while courier_menu == True:
                print("Press... \n 0 to exit the app"
                    + "\n 1 to see couriers" 
                    + "\n 2 to add a new courier" 
                    + "\n 3 to update an existing courier"
                    + "\n 4 to delete a courier"
                    + "\n 5 to return to Main Menu\n")
                str_courier_value = (input("Select a Courier Menu option: "))
                clear()
                if str_courier_value.isdigit():
                    courier_value = int(str_courier_value)
                    if courier_value == 0:
                        print("Thank you for using the app!")
                        sys.exit(0)
                    elif courier_value == 1:
                        proj_fun.show_couriers()
                    elif courier_value == 2:
                        proj_fun.add_courier()
                    elif courier_value == 3:
                        proj_fun.update_courier()
                    elif courier_value == 4:
                        proj_fun.delete_courier()
                    elif courier_value == 5:
                        # Exits the Courier Menu and returns user to the Main Menu
                        courier_menu = False
                    else:
                        print("\nSorry, this is not an option.\n")
                else:
                    print("\nSorry, input needs to be an integer\n")
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
                str_order_value = (input("Select an Order Menu option: "))
                clear()
                if str_order_value.isdigit():
                    order_value = int(str_order_value)
                    if order_value == 0:
                        print("Thank you for using the app!")
                        sys.exit(0)
                    elif order_value ==1:
                        proj_fun.show_orders()
                    elif order_value == 2:
                        proj_fun.create_new_order()
                    elif order_value == 3:
                        proj_fun.update_order_status()
                    elif order_value == 4:
                        proj_fun.update_order()
                    elif order_value == 5:
                        proj_fun.delete_order()
                    elif order_value == 6:
                        order_menu = False
                    else:
                        print("\nSorry this is not an option.\n")
                else:
                    print("\nSorry, input needs to be an integer\n")
    else:
        print("\nSorry, input needs to be an integer\n")
