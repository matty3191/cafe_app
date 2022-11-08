import os
import time
###################################### move this into .txt to persist
a = "apple"
b = "coffee"
c = "sandwich"

d = {
        "customer_name": "John",
        "customer_address": "Unit 2, 12 Main Street, London, WH1 2ER",
        "customer_phone": "0789887334",
        "status": "preparing"
    }

e = {
        "customer_name": "Philip J. Fry",
        "customer_address": "Planet Express, West 57th Street, Manhatten New New York, United States",
        "customer_phone": "07300030001",
        "status": "half the world away"
    }

f = "Postman Patrick"
g = "Ramona Flowers"
h = "Rocinante"

product_list = []
order_list = [] ########## do not persist this yet
courier_list = []

product_list.append(a)
product_list.append(b)
product_list.append(c)

order_list.append(d)
order_list.append(e)

courier_list.append(f)
courier_list.append(g)
courier_list.append(h)
######################################
print("Howdy Partner, welcome to your custom cafe management app.\n")
time.sleep(1)

## Main Menu ##
def main_menu():
    # displays main menu, uses input to return selected menu
    command = int(input("""Please type the number for the menu option below\n\n
0) Exit.\n
1) Product menu.\n
2) Orders menu.\n
3) Courier menu\n"""))
    while command != 0:
        if command >3 or command <0:
            print("Error")
            time.sleep(2)
            main_menu()
        if command == 1:
            product_menu()
        if command == 2:
            orders_menu()
        if command == 3:
            courier_menu()        
    # persist everythin but orders then exit  
    # save data, close files
    time.sleep(2)
    os.system('cls')
    print("Thank you for using Percival's Ugly Novel Kreation: PUNK")
    exit()

## Product menu ##
def product_menu():
    # displays p menu, uses input to return selected menu
    p_command = int(input("""
Product Menu:\n
Please select from the options below:\n\n
0) Exit.\n
1) Product list.\n
2) Create new product.\n
3) Update exsiting product.\n
4) Remove product.\n"""))
    while p_command != 0:
        if p_command >4 or p_command <0:
            print("Error")
            time.sleep(2)
            product_menu()
        if p_command == 1:
            view_products()
        if p_command == 2:
            create_new_product()
        if p_command == 3:
            update_product()
        if p_command == 4:
            delete_product()
            
    print("Exiting to main menu")
    main_menu()

def view_products():
    print(product_list)
    product_menu()

def create_new_product():
    # uses input to create list item. returns to p menu
    new_item = input("Please enter the name of the new product:\n")
    product_list.append(new_item)
    print(f"New item {new_item} has been added to the product list\n")
    print(product_list)
    product_menu()

def update_product():
    # uses input to update list item. returns to p menu
    for (i, item) in enumerate(product_list):
        print(i, item, "\n")
    index_input = int((input("Please enter the index of the product you wish to update\n")))
    print(f"You have selected {product_list[index_input]} to replace\n")
    replace_input = input("\nPlease enter the new product you wish to replace an old product with.\n")
    product_list[index_input] = replace_input
    print(f"product list has been updated{product_list}\n")
    product_menu()

def delete_product():
    # uses input to delete list item. returns to p menu
    for (i, item) in enumerate(product_list):
        print(i, item, "\n")
    delete_input = int((input("Please enter the index of the product you wish to delete\n")))
    print(f"You have removed {product_list[delete_input]} from the product list\n")
    del product_list[delete_input]
    print(product_list)
    product_menu()

## orders menu ##
def orders_menu():
    # displays o menu, uses input to return selected menu
    o_command = int(input("""
Orders menu:\n
0) Exit to main menu.\n
1) View list of orders.\n
2) Create a new order.\n
3) Update order status.\n
4) Update existing order.\n
5) Remove existing order.\n"""))
    while o_command != 0:
        if o_command >5 or o_command <0:
            print("Error")
            time.sleep(2)
            orders_menu()
        if o_command == 1:
            view_orders()
        if o_command == 2:
            create_new_order()
        if o_command == 3:
            update_order_status()
        if o_command == 4:
            update_product()
        if o_command == 5:
            delete_product()
            
    print("Exiting to main menu")
    main_menu()

def view_orders():
    print(*order_list, sep = "\n")
    orders_menu()

def create_new_order():
    print("Create New Order")
    new_order = {
                    "customer_name":"",
                    "customer_address":"",
                    "customer_phone":"",
                    "status":""}
    a = "customer_name"
    b = "customer_address"
    c = "customer_phone"
    d = "status"
    name_input = input("Enter Customer name: ")
    address_input = input("Enter customer address: ")
    phone_input = input("Enter customer phone number: ")
    status_input = "Preparing"
    new_order[a] = name_input
    new_order[b] = address_input
    new_order[c] = phone_input
    new_order[d] = status_input
    order_list.append(new_order)
    print(f"New order for {name_input} has been added\n")
    orders_menu()

def update_order_status():
    for (iteration, item) in enumerate(order_list):
        print(iteration, item, sep = " ")
    order_list_update_index_input = int((input("Please enter the index of the order to update the status of\n")))
    print(f"You have selected {order_list[order_list_update_index_input]} to update\n")
    to_update_status_dict = {}
    to_update_status_dict.update(order_list[order_list_update_index_input])
    status_update_input = input("Please enter the status update i.e 'out for delivery' \n")
    to_update_status_dict["status"] = status_update_input
    order_list[order_list_update_index_input] = to_update_status_dict
    print(f"You have succesfully updated the order to '{status_update_input}'")
    print(order_list[order_list_update_index_input])
    orders_menu()

def update_order():
    for (iteration, item) in enumerate(order_list):
        print(iteration, item, sep = " ")
    order_list_index_input = int((input("Please enter the index of the order you wish to update\n")))
    print(f"You have selected {order_list[order_list_index_input]} to update\n")
    to_update_dictionary = {}
    to_update_dictionary.update(order_list[order_list_index_input])
    order_replace_key_input = input("\nPlease enter the part of the order you wish to update e.g. customer_name.\n")
    order_replace_value_input = input("Now enter the updated information\n")
    to_update_dictionary[order_replace_key_input] = order_replace_value_input
    order_list[order_list_index_input] = to_update_dictionary
    print(f"order list has been updated{order_list}\n")
    orders_menu()

def remove_order():
    for (iteration, item) in enumerate(order_list):
        print(iteration, item, "\n")
    orders_menu_delete_input = int(input("Please enter the number of the order you would like to delete from the list\n"))
    print(f"You have selected {order_list[orders_menu_delete_input]} to delete\n")
    del order_list[orders_menu_delete_input]
    print("The updated order list is as follows:\n", order_list)
    orders_menu()

## courier menu ##
def courier_menu():
    # displays c menu, uses input to return selected menu
    c_command = int(input("""
Courier Menu:\n
Please select from the options below:\n\n
0) Exit.\n
1) Courier list.\n
2) Create new courier.\n
3) Update exsiting courier.\n
4) Remove courier.\n"""))
    while c_command != 0:
        if c_command >4 or c_command <0:
            print("Error")
            time.sleep(2)
            courier_menu()
        if c_command == 1:
            view_couriers()
        if c_command == 2:
            create_new_courier()
        if c_command == 3:
            update_courier()
        if c_command == 4:
            delete_courier()
            
    print("Exiting to main menu")
    main_menu()

def view_couriers():
    print(courier_list)
    courier_menu()

def create_new_courier():
    # uses input to create new courier. returns to c menu
    new_courier = input("Please enter the name of the new courier:\n")
    courier_list.append(new_courier)
    print(f"New courier, {new_courier}, has been added to the courier list\n")
    print(courier_list)
    courier_menu()

def update_courier():
    # uses input to update courier. returns to c menu
    for (i, item) in enumerate(courier_list):
        print(i, item, "\n")
    index_input = int((input("Please enter the index of the courier you wish to update\n")))
    print(f"You have selected {courier_list[index_input]} to replace\n")
    replace_input = input("\nPlease enter the new details of the courier.\n")
    courier_list[index_input] = replace_input
    print(f"Courier has been updated{courier_list}\n")
    courier_menu()

def delete_courier():
    # uses input to delete courier from list. returns to c menu
    for (i, item) in enumerate(courier_list):
        print(i, item, "\n")
    delete_input = int((input("Please enter the index of the courier you wish to delete\n")))
    print(f"You have removed {courier_list[delete_input]} from the courier list\n")
    del courier_list[delete_input]
    print(courier_list)
    courier_menu()

def open_couriers():
    with open('data/couriers.txt', 'r') as cf:
        courier_contents = cf.read()
        print(courier_contents)
        
def open_products():
    pass

main_menu ()







