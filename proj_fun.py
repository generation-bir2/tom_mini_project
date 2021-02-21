import csv
import os
import pymysql
import mysql.connector

def clear():
    os.system( 'cls' )
######### Database Connection ###########


mydb = pymysql.connect(
  user="root",
  password="password",
  database="Mini_Project"
)

cursor = mydb.cursor()




######### Product functions ###########

def show_products():
    clear()
    cursor.execute("SELECT * FROM Products")
    stock = cursor.fetchall()
    for item in stock:
        print(f"\nProduct: {item[1]}\nPrice: £{item[2]}\n")

def add_product():
    clear()
    new_product = input("What product are you adding? Press 0 to cancel. ").title().strip()
    if new_product.strip() == "0":
        return
    else:
        product_price = float(input(f"What is the price of {new_product}? "))
        cursor.execute(f"INSERT INTO Products(Product, Price) VALUES ('{new_product}', {product_price})")
        cursor.execute("SELECT * FROM Products")
        stock = cursor.fetchall()
        for item in stock:
            print(f"\nProduct: {item[1]}\nPrice: £{item[2]}\n")
        mydb.commit()


def update_product():
    clear()
    product_update = input("Which product would you like to update? Press 0 to cancel. ").title().strip()
    if product_update == "0":
        return
    else:
        cursor.execute("SELECT * FROM Products")
        stock = cursor.fetchall()
        for item in stock:
            if item[1] == product_update:
                new_product = input("What would you like to update the product to? Leave blank to skip. ").title().strip()
                if new_product != "":
                    cursor.execute(f"UPDATE Products SET Product = '{new_product}' WHERE Product = '{product_update}'")
                else:
                    new_product = product_update
                new_price = (input("What would you like to update the price to? Leave blank to skip. "))
                if new_price != "":
                    updated_price = float(new_price)
                    cursor.execute(f"UPDATE Products SET Price = {updated_price} WHERE Product = '{new_product}'")
                mydb.commit()
                cursor.execute("SELECT * FROM Products")
                new_stock = cursor.fetchall()
                for item in new_stock:
                    print(f"\nProduct: {item[1]}\nPrice: £{item[2]}\n")
                mydb.commit()
                return
            else:
                continue
        print("\nSorry, we do not have this product in our database\n")


def delete_product():
    clear()
    del_product = input("Which product would you like to delete? Press 0 to cancel. ").title().strip()
    if del_product == "0":
        return
    else:
        cursor.execute("SELECT * FROM Products")
        stock = cursor.fetchall()
        for item in stock:
            if item[1] == del_product:
                cursor.execute(f"DELETE FROM Products WHERE Product = '{del_product}'")
                mydb.commit()
                cursor.execute("SELECT * FROM Products")
                new_stock = cursor.fetchall()
                for item in new_stock:
                    print(f"\nProduct: {item[1]}\nPrice: £{item[2]}\n")
                mydb.commit()
                return
            else:
                continue
        print("\nSorry, we do not have this product in our database\n")


########## Courier functions ##########

def show_couriers():
    clear()
    cursor.execute("SELECT * FROM Couriers")
    available_couriers = cursor.fetchall()
    for courier in available_couriers:
        print(f"\nCourier: {courier[1]}\nCourier Number: {courier[2]}\n")

def add_courier():
    clear()
    new_courier = input("Which courier are you adding? Press 0 to cancel. ").title().strip()
    if new_courier == "0":
        return
    else:
        courier_number = input(f"What is {new_courier}'s number? ").strip()
        cursor.execute(f"INSERT INTO Couriers(Courier, Courier_Number) VALUES ('{new_courier}', '{courier_number}')")
        cursor.execute("SELECT * FROM Couriers")
        available_couriers = cursor.fetchall()
        for courier in available_couriers:
            print(f"\nCourier: {courier[1]}\nCourier Number: {courier[2]}\n")
        mydb.commit()



def update_courier():
    clear()
    courier_update = input("Which courier would you like to update? Press 0 to cancel. ").title().strip()
    if courier_update == "0":
        return
    else:
        cursor.execute("SELECT * FROM Couriers")
        available_couriers = cursor.fetchall()
        for courier in available_couriers:
            if courier[1] == courier_update:
                updated_courier = input(f"Who would you like to update {courier_update} to? Leave blank to skip. ").title().strip()
                if updated_courier != "":
                    cursor.execute(f"UPDATE Couriers SET Courier = '{updated_courier}' WHERE Courier = '{courier_update}'")
                else:
                    updated_courier = courier_update
                new_number = input("What would you like to update their phone number to? Leave blank to skip. ").strip()
                if new_number != "":
                    cursor.execute(f"UPDATE Couriers SET Courier_Number = '{new_number}' WHERE Courier = '{updated_courier}'")
                mydb.commit()
                cursor.execute("SELECT * FROM Couriers")
                new_available_couriers = cursor.fetchall()
                for courier in new_available_couriers:
                    print(f"\nCourier: {courier[1]}\nCourier Number: {courier[2]}\n")
                mydb.commit()
                return
            else:
                continue
        print("\nSorry, we do not have this courier in our databse\n")



def delete_courier():
    clear()
    courier_name = input("Which courier would you like to delete? Press 0 to cancel. ").title().strip()
    if courier_name == "0":
        return
    else:
        cursor.execute("SELECT * FROM Couriers")
        available_couriers = cursor.fetchall()
        for courier in available_couriers:
            if courier[1] == courier_name:
                cursor.execute(f"DELETE FROM Couriers WHERE Courier = '{courier_name}'")
                mydb.commit()
                cursor.execute("SELECT * FROM Couriers")
                new_available_couriers = cursor.fetchall()
                for courier in new_available_couriers:
                    print(f"\nCourier: {courier[1]}\nCourier Number: £{courier[2]}\n")
                mydb.commit()
                return
            else:
                continue
        print("\nSorry we do not have this courier in our database\n")   


########## Order functions #########


def show_orders():
    clear()
    cursor.execute("SELECT * FROM Orders")
    my_orders = cursor.fetchall()
    for order in my_orders:
        ordered_product_ids = []
        cursor.execute(f"SELECT Product_id FROM Order_products WHERE Order_id = '{order[0]}'")
        product_orders = cursor.fetchall()
        for products in product_orders:
            ordered_product_ids.append(products[0])
        print(f"\nCustomer Name: {order[1]}\nCustomer Address: {order[2]}\nCustomer Number: {order[3]}\nCourier ID: {order[4]}\nStatus: {order[5]}\nProduct IDs: {ordered_product_ids}\n")


def create_new_order():
    clear()
    name = input("What is the name of the customer? Press 0 to cancel. ").title().strip()
    if name == "0":
        return
    else:
        address = input("What is the customers address? ").title().strip()
        phone = input("What is the customers phone number? ").strip()
        status = "Preparing"
        cursor.execute("SELECT * FROM Couriers")
        available_couriers = cursor.fetchall()
        for courier in available_couriers:
            print(courier[1])
        courier_option = True
        while courier_option == True:
            courier_order = input("Which courier would you like? ").title().strip()
            for courier in available_couriers:
                if courier[1] == courier_order:
                    courier_id = courier[0]
                    cursor.execute("INSERT INTO Orders(Customer_name, Customer_address, Customer_phone, Courier_id, Status)"
                                + f"values('{name}', '{address}', '{phone}', {courier_id}, '{status}')")
                    mydb.commit()
                    courier_option = False
                else:
                    continue
            print("Sorry, we do not have this courier in our database")        
        clear()
        cursor.execute("SELECT * FROM Products")
        stock = cursor.fetchall()
        for product in stock:
            print(product[1])
        products_order = ""
        while products_order != "0":
            products_order = input("Which products would you like to add to the order? Press 0 to end selection.\n ").title().strip()
            for product in stock:
                if product[1] == products_order:
                    cursor.execute("INSERT INTO Order_products(Order_id, Customer_name, Product_id, Product)"
                                   + f"VALUES((SELECT Order_id FROM Orders WHERE Customer_address = '{address}'), '{name}', (SELECT Product_id FROM Products WHERE Product = '{product[1]}'), '{product[1]}')")
                    mydb.commit()
                else:
                    continue




def update_order_status():
    clear()
    order_name = input("Whose order would you like to update the status of? Press 0 to cancel. ").title().strip()
    if order_name == "0":
        return
    else:
        cursor.execute("SELECT * FROM Orders")
        my_orders = cursor.fetchall()
        for order in my_orders:
            if order[1] == order_name:
                statuses = ["Preparing", "Ready For Delivery", "Out For Delivery", "Delivered"]
                for status in statuses:
                    print(status)
                new_status = input("What would you like to update the order status to? ").title().strip()
                if new_status in statuses:
                    cursor.execute(f"UPDATE Orders SET Status = '{new_status}' WHERE Customer_name = '{order_name}'")
                    mydb.commit()
                    return
                else:
                    print("Sorry, that isn't an available status")
            else:
                continue
        print("Sorry, we do not have an order under this name.\n")


def update_order():
    clear()
    order_name = input("Whose order would you like to update? Press 0 to cancel. ").title().strip()
    if order_name == "0":
        return
    else:
        cursor.execute("SELECT * FROM Orders")
        current_orders = cursor.fetchall()
        for order in current_orders:
            if order[1] == order_name:
                new_name = input(f"Who would you like to update {order_name} to? Leave blank to skip. ").title().strip()
                if new_name != "":
                    cursor.execute(f"UPDATE Orders SET Customer_name = '{new_name}' WHERE Order_id = '{order[0]}'")
                    cursor.execute(f"UPDATE Order_products SET Customer_name = '{new_name}' WHERE Order_id = '{order[0]}'")
                new_address = input("What would you like to update the address to? Leave blank to skip ").title().strip()
                if new_address != "":
                    cursor.execute(f"UPDATE Orders SET Customer_address = '{new_address}' WHERE Order_id = '{order[0]}'")
                new_number = input("What would you like to update their phone number to? Leave blank to skip. ").strip()
                if new_number != "":
                    cursor.execute(f"UPDATE Orders SET Customer_phone = '{new_number}' WHERE Order_id = '{order[0]}'")
                mydb.commit()
                products_update = input("Would you like to update the ordered products? [Y/N]").title().strip()
                if products_update == "Y":
                    cursor.execute(f"DELETE FROM Order_products WHERE Order_id = '{order[0]}'")
                    cursor.execute("SELECT * FROM Products")
                    stock = cursor.fetchall()
                    for product in stock:
                        print(product[1])
                    new_products_order = ""
                    while new_products_order != "0":
                        new_products_order = input("Which products would you like to add to the order? Press 0 to end selection.\n ").title().strip()
                        for product in stock:
                            if product[1] == new_products_order:
                                cursor.execute("INSERT INTO Order_products(Order_id, Customer_name, Product_id, Product)"
                                    + f"VALUES((SELECT Order_id FROM Orders WHERE Order_id = '{order[0]}'), '{order[1]}', (SELECT Product_id FROM Products WHERE Product = '{product[1]}'), '{product[1]}')")
                                mydb.commit()
                                break
                            else:
                                continue
                cursor.execute("SELECT * FROM Couriers")
                new_available_couriers = cursor.fetchall()
                for courier in new_available_couriers:
                    print(courier[1])
                courier_option = True
                while courier_option == True:
                    courier_order = input("Which courier would you like? ").title().strip()
                    for courier in new_available_couriers:
                        if courier[1] == courier_order:
                            new_courier_id = courier[0]
                            cursor.execute(f"UPDATE Orders SET Courier_id = '{new_courier_id}' WHERE Order_id = '{order[0]}'")
                            mydb.commit()
                            courier_option = False
                            return
                        else:
                            continue
                    print("\nSorry, we do not have this courier in our databse\n")
            else:
                continue
        print("\nSorry, we don't have an order under this name in our database\n")


        
def delete_order():
    clear()
    order_name = input("Whose order would you like to delete? Press 0 to cancel. ").title().strip()
    if order_name == "0":
        return
    else:
        cursor.execute("SELECT * FROM Orders")
        current_orders = cursor.fetchall()
        for order in current_orders:
            if order[1] == order_name:
                cursor.execute(f"DELETE FROM Order_products WHERE Order_id = '{order[0]}'")
                cursor.execute(f"DELETE FROM Orders WHERE Customer_name = '{order_name}'")
                mydb.commit()
                cursor.execute("SELECT * FROM Orders")
                new_current_orders = cursor.fetchall()
                for order in new_current_orders:
                    print(f"\nCustomer_name: {order[1]}\nCustomer Address: £{order[2]}\nCustomer Number: {order[3]}\nCouier Id: {order[4]}\nStatus: {order[5]}")
                mydb.commit()
                return
            else:
                continue
        print("\nSorry we do not have this person's order in our database\n")   