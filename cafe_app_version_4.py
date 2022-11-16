import os
import time

from orders_crud_functions import (create_new_order, delete_order,
                                   update_order, update_order_status)
from orders_user_interface_layer import enumerate_order_list, view_orders
from utility_functions import (courier_list_of_dicts, order_list_of_dicts,
                               product_list_of_dicts, save_courier_files,
                               save_product_files)

order_status_list = ["preparing", "out for delivery", "delivered"]
###################################### application start ##############################################
print("Howdy Partner, welcome to your custom cafe management app.\n")
time.sleep(1)

## Main Menu ##
def main_menu():
    # displays main menu, uses input to return selected menu
    command = int(input("""Please type the number for the menu option below\n\n
0) Exit.\n
1) Product menu.\n
2) Courier menu.\n
3) Orders menu\n"""))
    while command != 0:
        if command >3 or command <0:
            print("Error")
            time.sleep(2)
            main_menu()
        if command == 1:
            product_menu()
        if command == 2:
            courier_menu()
        if command == 3:
            orders_menu()        
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

def enumerate_products():
    for (i, item) in enumerate(product_list_of_dicts):
        print(i, item, "\n")

def view_products():
    enumerate_products()
    product_menu()

def create_new_product():
    # uses input to create list item. returns to p menu
    product_list_of_dicts.append({'name':input("Please enter the name of the new product:\n"), 'price':input("please enter the price of the product\n")})
    print("New item has been added to the product list\n")
    print(product_list_of_dicts)
    product_menu()

def update_product():
    # uses input to update list item. returns to p menu
    enumerate_products(product_list_of_dicts, order_status_list, enumerate_order_list, orders_menu)
    product_list_of_dicts[int(input("Please enter the index of the product you wish to update\n"))][input("Enter either name or price\n")] = input("\nPlease enter the new information.\n")
    print(f"product list has been updated\n")
    product_menu()

def delete_product():
    # uses input to delete list item. returns to p menu
    enumerate_products()
    del product_list_of_dicts[int(input("Please enter the index of the product you wish to delete\n"))]
    print(f"Product removed from list\n{product_list_of_dicts}\n")
    product_menu()

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
    courier_list_of_dicts.append({'name':input("Please enter the name of the new courier:\n"), 'phone':input("please enter the couriers contact number:\n")})
    print(f"New courier has been added to the courier list\n")
    courier_menu()

def enumerate_courier_list():
    # loops through and enumerates courier list - does however include the headings which ill have to exclude.
    for (iteration, item) in enumerate(courier_list_of_dicts):
        print(iteration, item, sep = " ")

def update_courier():
    # uses 3 separate inputs to navigate to a key value in a list and replaces the value with the input
    enumerate_courier_list()
    courier_list_of_dicts[int(input("Index value of courier to update: "))][input("Enter name or phone: ")] = input("Enter new information: ")
    courier_menu()

def delete_courier():
    # uses input to delete courier from list. returns to c menu
    enumerate_courier_list()
    del courier_list_of_dicts[int(input("Please enter the index of the courier you wish to delete\n"))]
    courier_menu()

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
            view_orders(orders_menu, order_list_of_dicts)
        if order_command == 2:
            create_new_order(order_list_of_dicts, courier_list_of_dicts, orders_menu)
        if order_command == 3:
            update_order_status(enumerate_order_list, order_status_list, orders_menu)
        if order_command == 4:
            enumerate_order_list(order_list_of_dicts)
            order_index = int(input("Enter the index of the order you wish to update\n"))
            order_key = input("\nEnter the part of the order you wish to update e.g. customer_name.\n")
            new_order_value = input("Enter the updated information\n")
            update_order(order_list_of_dicts, order_index, order_key, new_order_value)
            print(f"order list has been updated{order_list_of_dicts}\n")
            orders_menu()

        if order_command == 5:
            delete_order()
            
    print("Exiting to main menu")
    main_menu()

main_menu ()