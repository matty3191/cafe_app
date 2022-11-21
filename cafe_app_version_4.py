import os
import time
from couriers_crud_functions import create_new_courier, delete_courier, update_courier
from orders_crud_functions import create_new_order, delete_order, update_order, update_order_status
from products_crud_functions import create_new_product, delete_product, update_product
from user_interface_layer import (
                                courier_menu_interface, enumerate_courier_list, enumerate_order_list, 
                                enumerate_order_status_list, enumerate_products_list, main_menu_options, 
                                order_menu_interface, products_menu_interface
                                )
from utility_functions import (courier_list_of_dicts, order_list_of_dicts, product_list_of_dicts, 
                                save_courier_files, save_orders_files,save_product_files
                            )
order_status_list = ["preparing", "out for delivery", "delivered"]
###################################### application start ##############################################
print("Howdy Partner, welcome to your custom cafe management app.\n")
time.sleep(1)

## Main Menu ##
def main_menu():
    while True:
        main_menu_options()
        command = int(input('Enter number to navigate menu:\n'))
        if command >3 or command <0:
            print("\nError: Enter a valid command: \n")
            time.sleep(2)
        elif command == 1:
            product_menu()
        elif command == 2:
            courier_menu()
        elif command == 3:
            orders_menu()
        else:
            break        
    print("Saving data")
    save_courier_files()
    save_product_files()
    save_orders_files()
    time.sleep(2)
    os.system('cls')
    print("Thank you for using Percival's Ugly Novel Kreation: PUNK")
    exit()

## Product menu ##
def product_menu():
    while True:
        products_menu_interface()
        p_command = int(input('\nEnter number to navigate menu: \n'))
        if p_command >4 or p_command <0:
            print("\nError: Enter a valid command: \n")
            time.sleep(2)
        elif p_command == 1:
            enumerate_products_list(product_list_of_dicts)
        elif p_command == 2:
            while True:
                new_product_name = input("Please enter the name of the new product:\n")
                if new_product_name == "":
                    print("Error, field cannont be blank\n")
                elif len(new_product_name) > 25:
                    print("Error, name cannot exceed 25 characters\n")
                else:
                    break
            while True:
                new_product_price = (input("please enter the price of the product\n"))
                if new_product_price == "":
                    print("Error, field cannot be blank\n")
                elif type(new_product_name) != float:
                    print("Error, price must take the format of a decimal point number\n")
                else:
                    break
            create_new_product(product_list_of_dicts, new_product_name, new_product_price)
            print("New item has been added to the product list\n")
            print(product_list_of_dicts)
        elif p_command == 3:
            enumerate_products_list(product_list_of_dicts)
            product_index = int(input("Please enter the index of the product you wish to update\n"))
            name_or_price = input("Enter either name or price\n")
            product_replace_value = input("\nPlease enter the new information.\n")
            update_product(product_list_of_dicts, product_index, name_or_price, product_replace_value)
            print(f"product list has been updated\n")
        elif p_command == 4:
            enumerate_products_list(product_list_of_dicts)
            delete_index = int(input("Please enter the index of the product you wish to delete\n"))
            delete_product(product_list_of_dicts, delete_index)
            print(f"Product removed from list\n{product_list_of_dicts}\n")
        else:
            print("Exiting to main menu")
            break


## courier menu ##
def courier_menu():
    while True:
        courier_menu_interface()
        c_command = int(input("\nEnter number to navigate menu: \n"))
        if c_command >4 or c_command <0:
            print("\nError: Enter a valid command: \n")
            time.sleep(2)
        elif c_command == 1:
            enumerate_courier_list(courier_list_of_dicts)
        elif c_command == 2:
            new_courier_name = input("Please enter the name of the new courier:\n")
            new_courier_phone = input("please enter the couriers contact number:\n")
            create_new_courier(courier_list_of_dicts, new_courier_name, new_courier_phone)
            print("New courier succesfully added")
        elif c_command == 3:
            enumerate_courier_list(courier_list_of_dicts)
            update_courier_index = int(input("Index value of courier to update: \n"))
            name_or_phone = input("Enter name or phone: \n")
            new_courier_information = input("Enter new information: ")
            update_courier(courier_list_of_dicts, update_courier_index, name_or_phone, new_courier_information)
        elif c_command == 4:
            enumerate_courier_list(courier_list_of_dicts)
            delete_index_value = int(input("Please enter the index of the courier you wish to delete\n"))
            delete_courier(courier_list_of_dicts, delete_index_value)
        else:
            print("Exiting to main menu")
            break



## orders menu ##
def orders_menu():
    while True:
        order_menu_interface()
        order_command = int(input("\nEnter number to navigate menu:\n"))
        if order_command >5 or order_command <0:
            print("\nError: Enter a valid command: \n")
            time.sleep(2)
        elif order_command == 1: 
            enumerate_order_list(order_list_of_dicts) 
        elif order_command == 2: 
            print("Create New Order")
            new_order = {
                "customer_name":"",
                "customer_address":"",
                "customer_phone":"",
                "assigned_courier":"",
                "status":"",
                "items":""
            }
            new_order["customer_name"] = input("Enter Customer name: ")
            new_order["customer_address"] = input("Enter customer address: ")
            new_order["customer_phone"] = input("Enter customer phone number: ")
            enumerate_courier_list(courier_list_of_dicts)
            new_order["assigned_courier"] = int(input("Please select the index of a courier to assign to this order\n"))
            new_order["status"] = "Preparing"
            enumerate_products_list(product_list_of_dicts)
            new_order["items"] = input("Select the items to add to the order, mulitple items are comma separated:\n")
            create_new_order(order_list_of_dicts, new_order)
            print("New order has been added\n")
        elif order_command == 3:
            enumerate_order_list(order_list_of_dicts)
            order_status_index_update = int(input("Please enter the index of the order to update the status of\n"))
            enumerate_order_status_list(order_status_list)
            new_order_status_value = order_status_list[int(input("Choose the index of the new order status:\n"))]
            update_order_status(order_list_of_dicts, order_status_index_update, new_order_status_value)
            print(f"You have succesfully updated the order status")
        elif order_command == 4:
            enumerate_order_list(order_list_of_dicts)
            order_index = int(input("Enter the index of the order you wish to update\n"))
            order_key = input("\nEnter the part of the order you wish to update e.g. customer_name.\n")
            new_order_value = input("Enter the updated information\n")
            update_order(order_list_of_dicts, order_index, order_key, new_order_value)
            print(f"order list has been updated{order_list_of_dicts}\n")
        elif order_command == 5:
            enumerate_order_list(order_list_of_dicts)
            delete_order_index = int(input("Please enter the number of the order you would like to delete from the list:\n"))
            delete_order(order_list_of_dicts, delete_order_index)
            print("Order succesfully deleted\n")
        else:
            print("Exiting to main menu")
            break

main_menu ()
