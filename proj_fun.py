import csv

######### Product functions ###########

def add_product(product_list):
    new_product_entry = {}
    new_product = input("What product are you adding? Press 0 to cancel. ")
    product_price = float(input(f"What is the price of {new_product.title().strip()}? "))
    if new_product.strip() == "0":
        return
    else:
        new_product_entry["Product"] = new_product.title().strip()
        new_product_entry["Price"] = product_price
        product_list.append(new_product_entry)
        print("Products:\n")
        print(product_list)
        print("\n")
        return product_list


def update_product(product_list):
    product_update = input("Which product would you like to update? Press 0 to cancel. ")
    if product_update.strip() == "0":
        return
    else:
        for product in product_list:
            if product["Product"] == product_update.title().strip():
                new_product = input("What would you like to update the product to? Leave blank to skip. ")
                if new_product != "":
                    product["Product"] = new_product.title().strip()
                new_price = float(input("What would you like to update the price to? Leave blank to skip. "))
                if new_price != "":
                    product["Price"] = new_price
                print("Products:\n")
                print(product_list)
                print("\n")
                return product_list
            else:
                continue
        print("Sorry, we do not have this product in stock")


def delete_product(product_list):
        del_product = input("Which product would you like to delete? Press 0 to cancel. ")
        if del_product.strip() == "0":
            return
        else:
            for product in product_list:
                if product["Product"] == del_product.title().strip():
                    product_index = product_list.index(product)
                    product_list.pop(product_index)
                    print("Products:\n")
                    print(product_list)
                    print("\n")
                    return product_list
                else:
                    continue
            print("Sorry, we do not have this product in stock")


########## Courier functions ##########


def add_courier(courier_list):
    new_courier_entry = {}
    new_courier = input("Which courier are you adding? Press 0 to cancel. ")
    courier_number = input(f"What is the {new_courier.title().strip()}'s phone number? ")
    if new_courier.strip() == "0":
        return
    else:
        new_courier_entry["Courier"] = new_courier.title().strip()
        new_courier_entry["Phone Number"] = courier_number.strip()
        courier_list.append(new_courier_entry)
        print("Couriers:\n")
        print(courier_list)
        print("\n")
        return courier_list


def update_courier(courier_list):
    courier_update = input("Which courier would you like to update? Press 0 to cancel. ")
    if courier.strip() == "0":
        return
    else:
        for courier in courier_list:
            if courier["Courier"] == courier_update.title().strip():
                updated_courier = input(f"Who would you like to update {courier_update.title().strip()} to? Leave blank to skip. ")
                if updated_courier != "":
                    courier["Courier"] = updated_courier.title().strrip()
                new_number = input("What would you like to update their phone number to? Leave blank to skip. ")
                if new_number != "":
                    courier["Phone Number"] = new_number.strip()
                print("Couriers:\n")
                print(courier_list)
                print("\n")
                return courier_list
            else:
                continue
        print("Sorry, we do not have this courier in our database")


def delete_courier(courier_list):
    courier_name = input("Which courier would you like to delete? Press 0 to cancel. ")
    if courier.strip() == "0":
        return
    else:
        for courier in courier_list:
            if courier["Courier"] == courier_name.title().strip():
                courier_index = courier_list.index(courier)
                courier_list.pop(courier_index)
                print("Couriers:\n")
                print(courier_list)
                print("\n")
                return courier_list
            else:
                continue
        print("Sorry, we do not have this courier in our database")


########## Order functions ###########


def create_new_order(order_list, courier_list):
    new_order = {}
    name = input("What is the name of the customer? ")
    address = input("What is the customers address? ")
    phone = input("What is the customers phone number? ")
    status = "Preparing"
    print("Couriers:\n")
    print(courier_list)
    print("\n")
    courier_for_order = input("Which courier would you like? ")
    for courier in courier_list:
        if courier["Courier"] == courier_for_order.title().strip():
            new_order["Name"] = name.title().strip()
            new_order["Address"] = address.title().strip()
            new_order["Phone Number"] = phone.strip()
            new_order["Status"] = status
            order_list.append(new_order)
            return order_list
        else:
            continue
    print("Sorry, we do not have this courier in our database")


def update_order_status(order_list):
    order_name = input("Whose order would you like to update the status of? Press 0 to cancel. ")
    if order_name.strip() == "0":
        return
    else:
        for order in order_list:
            if order["Name"] == order_name.title().strip():
                new_status = input("What is the new order status? ")
                order["Status"] = new_status.title().strip()
                print(order)
                return order_list
            else:
                continue
        print("Sorry, we do not have an order under this name.\n")


def update_order(order_list):
    order_name = input("Whose order would you like to update? Press 0 to cancel. ")
    if order_name.strip() == "0":
        return
    else:
        for order in order_list:
            if order["Name"] == order_name.title().strip():
                new_name = input("What would you like to update the name to? Leave blank to skip. ")
                if new_name != "":
                    order.update({"Name": new_name.title().strip()})
                new_address = input("What would you like to update the address to? Leave blank to skip. ")
                if new_address != "":
                    order.update({"Address": new_address.title().strip()})
                new_number = input("What would you like to update phone number to? Leave blank to skip. ")
                if new_number != "":
                    order.update({"Phone Number": new_number.strip()})
                return order_list
            else:
                continue
        print("Sorry, we do not have an order under this name.\n")


def delete_order(order_list):
    order_name = input("Whose order would you like to delete? Press 0 to cancel. ")
    if order_name.strip() == "0":
        return
    else:
        for order in order_list:
            if order["Name"] == order_name.title().strip():
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

def read_products(product_list):
    with open("products.csv", 'r') as products_file:
        products_csv = csv.DictReader(products_file)
        for row in products_csv:
            product_list.append(row)


def read_couriers(courier_list):
    with open("couriers.csv", "r") as couriers_file:
        couriers_csv = csv.DictReader(couriers_file)
        for row in couriers_csv:
            courier_list.append(row)


def read_orders(order_list):
    with open ("orders.csv", "r") as orders_file:
        orders_csv = csv.DictReader(orders_file)
        for row in orders_csv:
            order_list.append(row)


def save_products(product_list):
    with open('products.csv', 'w') as products_file:
        fieldnames = product_list[0].keys()
        writer = csv.DictWriter(products_file, fieldnames)
        writer.writeheader()
        writer.writerows(product_list)


def save_couriers(courier_list):
    with open('couriers.csv', 'w') as couriers_file:
        fieldnames = courier_list[0].keys()
        writer = csv.DictWriter(couriers_file, fieldnames)
        writer.writeheader()
        writer.writerows(courier_list)


def save_orders(order_list):
    with open('orders.csv', 'w') as orders_file:
        fieldnames = order_list[0].keys()
        writer = csv.DictWriter(orders_file, fieldnames)
        writer.writeheader()
        writer.writerows(order_list)