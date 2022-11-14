import os
import time
from csv import DictReader
from csv import DictWriter
###################################### move this into .txt to persist
items_list = [{
        "name" : "apple",
        "price" : 0.5
    },{
        "name" : "coffee", 
        "price" : 7.00
    },{
        "name" : "sandwich", 
        "price" : 3.00
    }]
deliver_driver_names = [{
        "name" : "Postman Patrick",
        "phone" : "0987654345"
    },{
        "name" : "Ramona Flowers",
        "numer" : "094567834578""Rocinante"
    }]
pre_pop_orders = [{
        "customer_name": "John",
        "customer_address": "Unit 2, 12 Main Street, London, WH1 2ER",
        "customer_phone": "0789887334",
        "assign_courier":"",
        "status": "preparing",
        "items": ""
    },{
        "customer_name": "Philip J. Fry",
        "customer_address": "Planet Express, West 57th Street, Manhatten New New York, United States",
        "customer_phone": "07300030001",
        "assigne_courier":"",
        "status": "half the world away",
        "items" : ""
    }
    ]

product_list = [item for item in items_list]
order_list = [order for order in pre_pop_orders]
courier_list = [name for name in deliver_driver_names]

def convert_couriers_file_to_list():
## returns a list of the .txt file specified with the \n character truncated ##
    with open('data/couriers.csv', 'r') as cf:
        courier_contents = cf.read().splitlines()
        
    return courier_contents

def save_courier_files():
    # opens file, uses for loop to add uodated list to file. saves and closes file.
    with open('data/couriers.csv', 'w+') as csf:
        for name in courier_file_list:
            csf.write(name + "\n")

def convert_products_file_to_list():
## returns a list of the .txt file specified with the \n character truncated ##
    with open('data/products.csv', 'r') as cf:
        product_contents = cf.read().splitlines()
        
    return product_contents

def save_product_files():
    # opens file, uses for loop to add uodated list to file. saves and closes file.
    with open('data/products.csv', 'w+') as csf:
        for name in product_file_list:
            csf.write(name + "\n")

def convert_orders_file_to_list():
## returns a list of the .txt file specified with the \n character truncated ##
    with open('data/orders.csv', 'r') as cf:
        product_contents = cf.read().splitlines()
        
    return product_contents

def save_orders_files():
    # opens file, uses for loop to add uodated list to file. saves and closes file.
    with open('data/orders.csv', 'w+') as csf:
        for name in product_file_list:
            csf.write(name + "\n")

product_file_list = convert_products_file_to_list()
courier_file_list = convert_couriers_file_to_list()
order_file_list = convert_orders_file_to_list()

print(product_file_list, "\n", courier_file_list, "\n", order_file_list)

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
    print("Saving data")
    save_courier_files()
    save_product_files()
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
    print(product_file_list)
    product_menu()

def create_new_product():
    # uses input to create list item. returns to p menu
    new_item = input("Please enter the name of the new product:\n")
    product_file_list.append(new_item)
    print(f"New item {new_item} has been added to the product list\n")
    print(product_file_list)
    product_menu()

def update_product():
    # uses input to update list item. returns to p menu
    for (i, item) in enumerate(product_file_list):
        print(i, item, "\n")
    index_input = int((input("Please enter the index of the product you wish to update\n")))
    print(f"You have selected {product_file_list[index_input]} to replace\n")
    replace_input = input("\nPlease enter the new product you wish to replace an old product with.\n")
    product_file_list[index_input] = replace_input
    print(f"product list has been updated{product_file_list}\n")
    product_menu()

def delete_product():
    # uses input to delete list item. returns to p menu
    for (i, item) in enumerate(product_file_list):
        print(i, item, "\n")
    delete_input = int((input("Please enter the index of the product you wish to delete\n")))
    print(f"You have removed {product_file_list[delete_input]} from the product list\n")
    del product_file_list[delete_input]
    print(product_file_list)
    product_menu()

## orders menu ##
def orders_menu():
    # displays o menu, uses input to return selected menu
    order_command = int(input("""
Orders menu:\n
0) Exit to main menu.\n
1) View list of orders.\n
2) Create a new order.\n
3) Update order status.\n
4) Update existing order.\n
5) Remove existing order.\n"""))
    while order_command != 0:
        if order_command >5 or order_command <0:
            print("Error")
            time.sleep(2)
            orders_menu()
        if order_command == 1:
            view_orders()
        if order_command == 2:
            create_new_order()
        if order_command == 3:
            update_order_status()
        if order_command == 4:
            update_product()
        if order_command == 5:
            delete_product()
            
    print("Exiting to main menu")
    main_menu()

def view_orders():
    # prints the orders list
    print(*order_list, sep = "\n")
    orders_menu()

def create_new_order():
    print("Create New Order")
    new_order = {
                    "customer_name":"",
                    "customer_address":"",
                    "customer_phone":"",
                    "assigned_courier":"",
                    "status":""}
    new_order["customer_name"] = input("Enter Customer name: ")
    new_order["customer_address"] = input("Enter customer address: ")
    new_order["customer_phone"] = input("Enter customer phone number: ")
    for (index, name) in enumerate(courier_file_list):
        print(index, name, sep = " ",)
    new_order["assigned_courier"] = int(input("Please select the index of a courier to assign to this order\n"))
    new_order["status"] = "Preparing"
    order_list.append(new_order)
    print("New order has been added\n")
    orders_menu()

def enumerate_order_list():
    # enumerates and prints orders list
    for (iteration, item) in enumerate(order_list):
        print(iteration, item, sep = " ")

def update_order_status():
    # uses user inputs to update order status
    enumerate_order_list()
    order_list_status_update_index_input = int((input("Please enter the index of the order to update the status of\n")))
    order_list["status"] = input("Please enter the status update i.e 'out for delivery' \n")
    print(f"You have succesfully updated the order to '{order_list_status_update_index_input}'")
    orders_menu()

def update_order():
    # calls function to display enumerated order list
    enumerate_order_list()
    order_list_index_input = int((input("Please enter the index of the order you wish to update\n")))
    order_replace_key_input = input("\nPlease enter the part of the order you wish to update e.g. customer_name.\n")
    order_replace_value_input = input("Now enter the updated information\n")
    order_list[order_list_index_input][order_replace_key_input] = order_replace_value_input
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
    enumerate_courier_list()
    courier_menu()

def create_new_courier():
    # uses input to create new courier. returns to c menu
    new_courier = input("Please enter the name of the new courier:\n")
    courier_file_list.append(new_courier)
    print(f"New courier, {new_courier}, has been added to the courier list\n")
    print(courier_file_list)
    courier_menu()

def enumerate_courier_list():
    # uses input to update courier. returns to c menu
    for (i, item) in enumerate(courier_file_list):
        print(i, item, "\n")

def update_courier():
    enumerate_courier_list()
    index_to_update = int(input("index value of courier to update: "))
    courier_replace_key_input = input("enter name or number: ")
    courier_file_list[index_to_update][courier_replace_key_input] = input("enter new info: ")
    courier_menu()

def delete_courier():
    # uses input to delete courier from list. returns to c menu
    enumerate_courier_list()
    delete_input = int((input("Please enter the index of the courier you wish to delete\n")))
    print(f"You have removed {courier_file_list[delete_input]} from the courier list\n")
    del courier_file_list[delete_input]
    print(courier_file_list)
    courier_menu()

def open_couriers():
    with open('data/couriers.txt', 'r') as cf:
        courier_contents = cf.read()
        print(courier_contents)

main_menu ()