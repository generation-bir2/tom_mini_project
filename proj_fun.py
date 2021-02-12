import csv
import pymysql

######### Database Connection ###########

mydb = pymysql.connect(
  user="root",
  password="password",
  database="Mini_Project"
)

cursor = mydb.cursor()




######### Product functions ###########

def show_products():
    cursor.execute("SELECT * FROM products")
    stock = cursor.fetchall()
    for item in stock:
        print(f"\nProduct: {item[1]}\nPrice: £{item[2]}\n")

def add_product():
    new_product = input("What product are you adding? Press 0 to cancel. ").title().strip()
    if new_product.strip() == "0":
        return
    else:
        product_price = float(input(f"What is the price of {new_product}? "))
        cursor.execute(f"INSERT INTO products(Product, Price) VALUES ('{new_product}', {product_price})")
        cursor.execute("SELECT * FROM products")
        stock = cursor.fetchall()
        for item in stock:
            print(f"\nProduct: {item[1]}\nPrice: £{item[2]}\n")
        mydb.commit()


def update_product():
    product_update = input("Which product would you like to update? Press 0 to cancel. ").title().strip()
    if product_update == "0":
        return
    else:
        cursor.execute("SELECT * FROM products")
        stock = cursor.fetchall()
        for item in stock:
            if item[1] == product_update:
                new_product = input("What would you like to update the product to? Leave blank to skip. ").title().strip()
                if new_product != "":
                    cursor.execute(f"UPDATE products SET Product = '{new_product}' WHERE Product = '{product_update}'")
                else:
                    new_product = product_update
                new_price = (input("What would you like to update the price to? Leave blank to skip. "))
                if new_price != "":
                    updated_price = float(new_price)
                    cursor.execute(f"UPDATE products SET Price = {updated_price} WHERE Product = '{new_product}'")
                mydb.commit()
                cursor.execute("SELECT * FROM products")
                new_stock = cursor.fetchall()
                for item in new_stock:
                    print(f"\nProduct: {item[1]}\nPrice: £{item[2]}\n")
                mydb.commit()
                return
            else:
                continue
        print("\nSorry, we do not have this product in our database\n")


def delete_product():
        del_product = input("Which product would you like to delete? Press 0 to cancel. ").title().strip()
        if del_product == "0":
            return
        else:
            cursor.execute("SELECT * FROM products")
            stock = cursor.fetchall()
            for item in stock:
                if item[1] == del_product:
                    cursor.execute(f"DELETE FROM products WHERE Product = '{del_product}'")
                    mydb.commit()
                    cursor.execute("SELECT * FROM products")
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
    cursor.execute("SELECT * FROM couriers")
    available_couriers = cursor.fetchall()
    for courier in available_couriers:
        print(f"\nCourier: {courier[1]}\nCourier Number: {courier[2]}\n")

def add_courier():
    new_courier = input("Which courier are you adding? Press 0 to cancel. ").title().strip()
    if new_courier == "0":
        return
    else:
        courier_number = input(f"What is {new_courier}'s number? ").strip()
        cursor.execute(f"INSERT INTO couriers(Courier, Courier_Number) VALUES ('{new_courier}', '{courier_number}')")
        cursor.execute("SELECT * FROM couriers")
        available_couriers = cursor.fetchall()
        for courier in available_couriers:
            print(f"\nCourier: {courier[1]}\nCourier Number: {courier[2]}\n")
        mydb.commit()



def update_courier():
    courier_update = input("Which courier would you like to update? Press 0 to cancel. ").title().strip()
    if courier_update == "0":
        return
    else:
        cursor.execute("SELECT * FROM couriers")
        available_couriers = cursor.fetchall()
        for courier in available_couriers:
            if courier[1] == courier_update:
                updated_courier = input(f"Who would you like to update {courier_update} to? Leave blank to skip. ").title().strip()
                if updated_courier != "":
                    cursor.execute(f"UPDATE couriers SET Courier = '{updated_courier}' WHERE Courier = '{courier_update}'")
                new_number = input("What would you like to update their phone number to? Leave blank to skip. ").strip()
                if new_number != "":
                    cursor.execute(f"UPDATE couriers SET Courier_Number = '{new_number}' WHERE Courier = '{updated_courier}'")
                mydb.commit()
                cursor.execute("SELECT * FROM couriers")
                new_available_couriers = cursor.fetchall()
                for courier in new_available_couriers:
                    print(f"\nCourier: {courier[1]}\nCourier Number: £{courier[2]}\n")
                mydb.commit()
                return
            else:
                continue
        print("\nSorry, we do not have this courier in our databse\n")



def delete_courier():
    courier_name = input("Which courier would you like to delete? Press 0 to cancel. ").title().strip()
    if courier_name == "0":
        return
    else:
        cursor.execute("SELECT * FROM couriers")
        available_couriers = cursor.fetchall()
        for courier in available_couriers:
            if courier[1] == courier_name:
                cursor.execute(f"DELETE FROM couriers WHERE Courier = '{courier_name}'")
                mydb.commit()
                cursor.execute("SELECT * FROM couriers")
                new_available_couriers = cursor.fetchall()
                for courier in new_available_couriers:
                    print(f"\nCourier: {courier[1]}\nCourier Number: £{courier[2]}\n")
                mydb.commit()
                return
            else:
                continue
        print("\nSorry we do not have this courier in our database\n")   


########## Order functions ###########


def create_new_order(order_list, courier_list, product_list):
    new_order = {}
    name = input("What is the name of the customer? Press 0 to cancel. ").title().strip()
    if name == "0":
        return
    else:
        address = input("What is the customers address? ").title().strip()
        phone = input("What is the customers phone number? ").strip()
        status = "Preparing"
        product_selection = []
        print("\n")
        print(product_list)
        print("\n")
        products_order = ""
        while products_order != "0":
            products_order = input("Which products would you like to add to the order? Press 0 to end selection.\n ").title().strip()
            for product in product_list:
                if product["Product"] == products_order:
                    product_index = product_list.index(product)
                    product_selection.append(product_index)
                else:
                    continue
        print("Couriers:\n")
        print(courier_list)
        print("\n")
        courier_order = input("Which courier would you like? ").title().strip()
        for courier in courier_list:
            if courier["Courier"] == courier_order:
                courier_index = courier_list.index(courier)
                new_order["Name"] = name
                new_order["Address"] = address
                new_order["Phone Number"] = phone
                new_order["Order Courier"] = courier_index
                new_order["Status"] = status
                new_order["Order Products"] = product_selection
                order_list.append(new_order)
                print(new_order)
                return order_list
            else:
                continue
        print("Sorry, we do not have this courier in our database")


def update_order_status(order_list):
    order_name = input("Whose order would you like to update the status of? Press 0 to cancel. ").title().strip()
    if order_name == "0":
        return
    else:
        for order in order_list:
            if order["Name"] == order_name:
                statuses = ["Preparing", "Ready For Delivery", "Out For Delivery", "Delivered"]
                print("\n")
                print(statuses)
                print("\n")
                new_status = input("What would you like to update the order status to? ").title().strip()
                if new_status in statuses:
                    order["Status"] = new_status
                    print(order)
                    return order_list
                else:
                    print("Sorry, that isn't an available status")
            else:
                continue
        print("Sorry, we do not have an order under this name.\n")


def update_order(order_list, courier_list, product_list):
    order_name = input("Whose order would you like to update? Press 0 to cancel. ").title().strip()
    if order_name.strip() == "0":
        return
    else:
        for order in order_list:
            if order["Name"] == order_name:
                new_name = input("What would you like to update the name to? Leave blank to skip. ").title().strip()
                if new_name != "":
                    order.update({"Name": new_name})
                new_address = input("What would you like to update the address to? Leave blank to skip. ").title().strip()
                if new_address != "":
                    order.update({"Address": new_address})
                new_number = input("What would you like to update phone number to? Leave blank to skip. ").strip()
                if new_number != "":
                    order.update({"Phone Number": new_number})
                new_selection = input("Would you like to update the product selection? [Y/N]").title().strip()
                if new_selection == "Y":
                    new_product_order = ""
                    new_product_selection = []
                    print("\nThe product selection is now empty\n")
                    while new_product_order != "0":
                        print(product_list)
                        print("\n")
                        new_product_order = input("Which products would you like to add to the order? Press 0 to end selection.\n ").title().strip()
                        for product in product_list:
                            if product["Product"] == new_product_order:
                                product_index = product_list.index(product)
                                new_product_selection.append(product_index)
                            else:
                                continue
                    order.update({"Order Products": new_product_selection})
                print(courier_list)
                new_courier = input("Who would you like to update the courier to? Leave blank to skip. ").title().strip()
                if new_courier != "":
                    for courier in courier_list:
                        if courier["Courier"] == new_courier:
                            courier_index = courier_list.index(courier)
                        else:
                            continue
                    order.update({"Order Courier": courier_index})
                print(order)
                return order_list
            else:
                continue
        print("Sorry, we do not have an order under this name.\n")


def delete_order(order_list):
    order_name = input("Whose order would you like to delete? Press 0 to cancel. ").title().strip()
    if order_name == "0":
        return
    else:
        for order in order_list:
            if order["Name"] == order_name:
                order_index = order_list.index(order)
                order_list.pop(order_index)
                print("Orders:\n")
                print(order_list)
                print("\n")
                return order_list
            else:
                continue
        print("Sorry, we do not have an order under this name.\n")
        
        
########### File functions ############

def read_orders(order_list):
    with open ("orders.csv", "r") as orders_file:
        orders_csv = csv.DictReader(orders_file)
        for row in orders_csv:
            order_list.append(row)


def save_orders(order_list):
    with open('orders.csv', 'w') as orders_file:
        fieldnames = order_list[0].keys()
        writer = csv.DictWriter(orders_file, fieldnames)
        writer.writeheader()
        writer.writerows(order_list)