def add_product(product_list):
    new_product_entry = {}
    new_product = input("What product are you adding? Press 0 to cancel. ")
    product_price = float(input(f"What is the price of {new_product}? "))
    if new_product.strip() == "0":
        return
    else:
        new_product_entry["Product"] = new_product.title().strip()
        new_product_entry["Price"] = product_price
        product_list.append(new_product_entry)
        print("Products:\n")
        print(product_list)
        print("\n")


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

def delete_product(product_list):
        product = input("Which product would you like to delete? Press 0 to cancel. ")
        if product.title().strip() in product_list:
            product_index = product_list.index(product.title().strip())
            product_list.pop(product_index)
            print("Products:\n")
            print(product_list)
            print("\n")
            return product_list
        elif product.strip() == "0":
            return
        else:
            print("Sorry, we do not have this product in stock")


def add_courier(courier_list):
    new_courier = input("Which courier are you adding? Press 0 to cancel. ")
    if new_courier.strip() == "0":
        return
    else:
        courier_list.append(new_courier.title().strip())
        print("Couriers:\n")
        print(courier_list)
        print("\n")
        return courier_list


def update_courier(courier_list):
    courier = input("Which courier would you like to update? Press 0 to cancel. ")
    if courier.title().strip() in courier_list:
        updated_courier = input("What would you like to update it to? ")
        courier_index = courier_list.index(courier.title().strip())
        courier_list[courier_index] = updated_courier.title().strip()
        print("Couriers:\n")
        print(courier_list)
        print("\n")
        return courier_list
    elif courier.strip() == "0":
        return
    else:
        print("Sorry, we do not have this courier in our database")


def delete_courier(courier_list):
    courier = input("Which courier would you like to delete? Press 0 to cancel. ")
    if courier.title().strip() in courier_list:
        courier_index = courier_list.index(courier.title().strip())
        courier_list.pop(courier_index)
        print("Couriers:\n")
        print(courier_list)
        print("\n")
        return courier_list
    elif courier.strip() == "0":
        return
    else:
        print("Sorry, we do not have this courier in our database")


def create_new_order(order_list, courier_list):
    new_order = {}
    name = input("What is the name of the customer? ")
    address = input("What is the customers address? ")
    phone = input("What is the customers phone number? ")
    status = "Preparing"
    print("Couriers:\n")
    print(courier_list)
    print("\n")
    courier = input("Which courier would you like? ")
    if courier.title().strip() in courier_list:
        new_order["Name"] = name.title().strip()
        new_order["Address"] = address.title().strip()
        new_order["Phone Number"] = phone.strip()
        new_order["Status"] = status
        order_list.append(new_order)
        return order_list
    else:
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




def delete_order(order_list):
    order_name = input("Whose order would you like to delete? Press 0 to cancel. ")
    if order_name.strip() == "0":
        return
    else:
        for order in order_list:
            if order["Name"] == order_name.title().strip():
                order_index = order_list.index(order)
                order_list.pop(order_index)
                return order_list
            else:
                continue
        print("Sorry, we do not have an order under this name.\n")