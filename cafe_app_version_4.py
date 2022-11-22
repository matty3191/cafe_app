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
        command = input('Enter number to navigate menu:\n')
        try:
            command = int(command)
        except ValueError:
            print("Error: Please enter a valid command")
            continue
        if command >3 or command <0:
            print("\nError: Please enter a valid command: \n")
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
        p_command = input('\nEnter number to navigate menu: \n')
        try:
            p_command = int(p_command)
        except ValueError:
            print("Error: Please enter a valid command")
            continue
        if p_command >4 or p_command <0:
            print("\nError: Enter a valid command: \n")
            time.sleep(2)
        elif p_command == 1: #view products
            enumerate_products_list(product_list_of_dicts)
        elif p_command == 2: #add new product
            while True:
                new_product_name = input("Please enter the name of the new product:\n")
                if new_product_name == "" or len(new_product_name) > 25:
                    print("Error, field cannont be blank or exceed 25 characters\n")
                    continue
                new_product_price = input("please enter the price of the product\n")
                try:
                    new_product_price = float(new_product_price)
                except ValueError:
                    print("Error, please enter a decimal point number\n")
                    continue
                else:
                    break
            create_new_product(product_list_of_dicts, new_product_name, new_product_price)
            print("New item has been added to the product list\n")
            enumerate(product_list_of_dicts)
        elif p_command == 3: #update existing product
            while True:
                enumerate_products_list(product_list_of_dicts)
                product_index = input("Please enter the index of the product you wish to update\n")
                try:
                    product_index = int(product_index)
                except ValueError:
                    print("Error: Index must be a whole number\n")
                    continue
                if product_index not in range(len(product_list_of_dicts)):
                    print ("Error: Entered index value out of range\n")  
                    continue
                name_or_price = input("Enter either name or price\n")
                if name_or_price.lower() == "name" or name_or_price.lower() == "price": 
                    pass
                else:
                    print("Error: Please enter \'name\' or \'price\'")
                    continue                    
                product_replace_value = input("\nPlease enter the new information.\n")
                if name_or_price.lower() == "price":
                    try:
                        product_replace_value = float(product_replace_value)
                    except ValueError:
                        print("Error: When selecting price, input must be a decimal number\n")
                        continue
                update_product(product_list_of_dicts, product_index, name_or_price, product_replace_value)
                print("\nproduct list has been updated\n")
                break
        elif p_command == 4: # delete product
            enumerate_products_list(product_list_of_dicts)
            delete_index = input("Please enter the index of the product you wish to delete\n")
            try:
                delete_index = int(delete_index)
            except ValueError:
                print("Error: Index must be a whole number\n")
                continue
            if delete_index not in range(len(product_list_of_dicts)):
                print ("Error: Entered index value out of range\n")  
                continue
            delete_product(product_list_of_dicts, delete_index)
            print(f"Product removed from list\n{enumerate_products_list(product_list_of_dicts)}\n")
        else:
            print("Exiting to main menu")
            break


## courier menu ##
def courier_menu():
    while True:
        courier_menu_interface()
        c_command = input("\nEnter number to navigate menu: \n")
        try:
            c_command = int(c_command)
        except ValueError:
            print("Error: Please enter a valid command\n")
            continue
        if c_command >4 or c_command <0:
            print("\nError: Enter a valid command: \n")
            time.sleep(2)
        elif c_command == 1: # view list of couriers
            enumerate_courier_list(courier_list_of_dicts)
        elif c_command == 2: # add new courier
            new_courier_name = input("Please enter the name of the new courier:\n")
            if new_courier_name == "" or len(new_courier_name) >= 50:
                print("Error: field cannont be blank or exceed 50 characters\n")
                continue
            new_courier_phone = input("Please enter the couriers contact number:\n")
            try:
                new_courier_phone = int(new_courier_phone)
            except ValueError:
                print("Error, Field cannot be blank and ust be 11 numbers long\n")
                continue
            if new_courier_phone == "" or len(str(new_courier_phone)) != 10:
                print("Error, field cannont be blank and must be 11 numbers long\n")
                continue
            create_new_courier(courier_list_of_dicts, new_courier_name, new_courier_phone)
            print("New courier succesfully added\n")
        elif c_command == 3: # update existing courier
            enumerate_courier_list(courier_list_of_dicts)
            update_courier_index = input("Index value of courier to update:\n")
            try:
                update_courier_index = int(update_courier_index)
            except ValueError:
                print("Error: Field cannot be blank and must be a whole number\n")
                continue
            if update_courier_index not in range(len(courier_list_of_dicts)):
                print ("Error: The index value entere is out of range\n")  
                continue
            name_or_phone = input("Enter name or phone: \n")
            if name_or_phone.lower() == "name" or name_or_phone.lower() == "phone": 
                pass
            else:
                print("Error: Please enter 'name' or 'phone'\n")
                continue
            new_courier_information = input("Enter new information:\n")
            if new_courier_information == '':
                print("Error: Field cannot be blank\n")
                continue
            if name_or_phone.lower() == "phone":
                if len(new_courier_information) != 11: #must be str as int starting with 0 drops the 0 
                    print("Error: Input cannot be blank must be an 11 digit long whole number1\n")
                    continue
            if name_or_phone.lower() == "name":
                if len(new_courier_information) >=50:
                    print("Error: Name cannont be blank or exceed 50 characters\n")
                    continue
            update_courier(courier_list_of_dicts, update_courier_index, name_or_phone, new_courier_information)
            print("Courier succesfuly updated\n")
        elif c_command == 4: # delete courier
            enumerate_courier_list(courier_list_of_dicts)
            delete_index_value = input("Please enter the index of the courier you wish to delete\n")
            try:
                delete_index_value = int(delete_index_value)
            except ValueError:
                print("Error: Index cannot be blank and must be a whole number\n")
                continue
            if delete_index_value not in range(len(courier_list_of_dicts)):
                print ("Error: Entered index value out of range\n")  
                continue
            delete_courier(courier_list_of_dicts, delete_index_value)
            print("Succesfully deleted courier.\n")
        else:
            print("Exiting to main menu")
            break



## orders menu ##
def orders_menu():
    while True:
        order_menu_interface()
        order_command = int(input("\nEnter number to navigate menu:\n"))
        try:
            order_command = int(order_command)
        except ValueError:
            print("Error: Please enter a valid command\n")
            continue
        if order_command >5 or order_command <0:
            print("\nError: Please enter a valid command: \n")
            time.sleep(2)
        elif order_command == 1: # view list of orders
            enumerate_order_list(order_list_of_dicts) 
        elif order_command == 2: # add new order
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
            if new_order["customer_phone"] == '' or len(new_order["customer_phone"]) != 11: #same issue as above having to be an str
                print("Error: Field cannot be blank and must contain 11 numbers\n")
                continue
            enumerate_courier_list(courier_list_of_dicts)
            new_order["assigned_courier"] = input("Please select the index of a courier to assign to this order\n")
            try:
                new_order["assigned_courier"] = int(new_order["assigned_courier"])
            except ValueError:
                print("Error: Index cannot be blank and must be a whole number\n")
                continue
            if new_order["assigned_courier"] not in range(len(courier_list_of_dicts)):
                print ("Error: Entered index value out of range\n")  
                continue
            new_order["status"] = "Preparing"
            enumerate_products_list(product_list_of_dicts)
            new_order["items"] = input("Select the items to add to the order, mulitple items are comma separated:\n")
            create_new_order(order_list_of_dicts, new_order)
            print("New order has been added\n")
        elif order_command == 3: # update existing order status
            enumerate_order_list(order_list_of_dicts)
            order_status_index_update = input("Please enter the index of the order to update the status of\n")
            try:
                order_status_index_update = int(order_status_index_update)
            except ValueError:
                print("Error: Index cannot be blank and must be a whole number\n")
                continue
            if order_status_index_update not in range(len(order_list_of_dicts)):
                print ("Error: Entered index value out of range\n")  
                continue
            enumerate_order_status_list(order_status_list)
            try:
                new_order_status_value = order_status_list[int(input("Choose the index of the new order status:\n"))]
            except ValueError:
                print("Error: Index cannot be blank and must be a whole number\n")
                try:
                    new_order_status_value not in range(len(new_order_status_value))
                except IndexError:
                    print ("Error: Entered index value out of range\n")  
                    continue
            update_order_status(order_list_of_dicts, order_status_index_update, new_order_status_value)
            print(f"You have succesfully updated the order status")
        elif order_command == 4: # update existing order
            enumerate_order_list(order_list_of_dicts)
            order_index = int(input("Enter the index of the order you wish to update\n"))
            try:
                order_index = int(order_index)
            except ValueError:
                print("Error: Index cannot be blank and must be a whole number\n")
                continue
            if order_index not in range(len(order_list_of_dicts)):
                print ("Error: Entered index value out of range\n")  
                continue
            order_key = input("\nEnter the part of the order you wish to update e.g. customer_name.\n")
            if order_key not in order_list_of_dicts[0:-1]:
                print ("Error: Entered value not in list of options\n")  
                continue
            new_order_value = input("Enter the updated information\n")
            # if order_key == customer_name
            # if order_key == customer_phone
            # if order_key == 
            # if order_key ==
            update_order(order_list_of_dicts, order_index, order_key, new_order_value)
            print(f"order list has been updated{order_list_of_dicts}\n")
        elif order_command == 5: # delete order
            enumerate_order_list(order_list_of_dicts)
            delete_order_index = input("Please enter the number of the order you would like to delete from the list:\n")
            try:
                delete_order_index = int(delete_order_index)
            except ValueError:
                print("Error: Index cannot be blank and must be a whole number\n")
                continue
            if delete_order_index not in range(len(order_list_of_dicts)):
                print ("Error: Entered index value out of range\n")  
                continue
            delete_order(order_list_of_dicts, delete_order_index)
            print("Order succesfully deleted\n")
        else:
            print("Exiting to main menu")
            break

main_menu ()
