############################################################################################
#testing the version control of github

import time
import os

os.system('cls')
time.sleep(1)
print("Welcome to Percival's Portfolio: Cafe Delivery Management System")
time.sleep(3)
os.system('cls')

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

product_list = []
order_list = []

product_list.append(a)
product_list.append(b)
product_list.append(c)

order_list.append(d)
order_list.append(e)

# print(product_list)
# print(*order_list, sep = "\n\n")

    # if main_menu_input == 0:
    #     
    #     exit

## Main menu ##
time.sleep(0.8)
print("Howdy Partner, welcome to your custom cafe management app.\n")
time.sleep(3)
os.system('cls')
print("Please select an option from the menu below\n")
time.sleep(0.8)    


main_menu_input = int(input("""
Main Menu\n
0) Exit.\n
1) Product menu.\n
2) Orders menu.\n"""))
os.system('cls')
while main_menu_input != 0:
    
    while main_menu_input >2 or main_menu_input <0:
        os.system('cls')
        time.sleep(0.8)
        main_menu_input = int(input("""
Error: Selection invalid.\n
Please enter a valid option.\n\n
Main Menu\n
0) Exit.\n
1) Product menu.\n
2) Orders menu.\n"""))

## Product menu ##
    if main_menu_input == 1:
        os.system('cls')
        time.sleep(0.8)
        product_menu_input = int(input("""
Product Menu:\n
Please select from the options below:\n\n
0) Exit.\n
1) Product list.\n
2) Create new product.\n
3) Update exsiting product.\n
4) Remove product.\n"""))

        while product_menu_input != 0:
            while product_menu_input >4 or product_menu_input <0:
                os.system('cls')
                time.sleep(0.8)
                product_menu_input = int(input("""
Error: Selection invalid.\n
Please enter a valid option.\n\n
Product Menu:\n
0) Exit.\n
1) Product list.\n
2) Create new product.\n
3) Update exsiting product.\n
4) Remove product.\n"""))

            if product_menu_input == 1:
                os.system('cls')
                time.sleep(0.8) 
                print(product_list)
                time.sleep(0.8)
                product_menu_input = int(input("""
Product Menu:\n
0) Exit to main menu.\n
1) view product list.\n
2) Create new product.\n
3) Update exsiting product.\n
4) Remove product.\n"""))

            elif product_menu_input == 2: 
                os.system('cls')
                print("Create new product:\n")
                time.sleep(0.8)
                new_item = input("Please enter the name of the new product:\n")
                product_list.append(new_item)
                print(f"New item {new_item} has been added to the product list\n")
                time.sleep(1.2)
                print(product_list)
                time.sleep(1.2)
                product_menu_input = int(input("""
Product Menu:\n
0) Exit to main menu.\n
1) View product list.\n
2) Create new product.\n
3) Update exsiting product.\n
4) Remove product.\n"""))

            elif product_menu_input == 3:
                os.system('cls')
                for (i, item) in enumerate(product_list):
                    print(i, item, "\n")
                time.sleep(0.8)
                index_input = int((input("Please enter the index of the product you wish to update\n")))
                time.sleep(0.8)
                print(f"You have selected {product_list[index_input]} to replace\n")
                replace_input = input("\nPlease enter the new product you wish to replace an old product with.\n")
                product_list[index_input] = replace_input
                time.sleep(0.8)
                print(f"product list has been updated{product_list}\n")
                time.sleep(0.8)
                product_menu_input = int(input("""
Product Menu:\n
0) Exit to main menu.\n
1) View product list.\n
2) Create new product.\n
3) Update exsiting product.\n
4) Remove product.\n"""))

            elif product_menu_input == 4:
                time.sleep(0.8)
                os.system('cls')
                for (i, item) in enumerate(product_list):
                    print(i, item, "\n")
                delete_input = int((input("Please enter the index of the product you wish to delete\n")))
                time.sleep(0.8)
                print(f"You have removed {product_list[delete_input]} from the product list\n")
                del product_list[delete_input]
                time.sleep(0.8)
                print(product_list) 
                product_menu_input = int(input("""
Product Menu:\n
0) Exit to main menu.\n
1) View product list.\n
2) Create new product.\n
3) Update existing product.\n
4) Remove product.\n"""))

            else:
                os.system('cls')
                break

## Orders menu ##
    if main_menu_input == 2:
        os.system('cls')
        orders_menu_input = int(input("""
Orders menu:\n
0) Exit to main menu.\n
1) View list of orders.\n
2) Create a new order.\n
3) Update order status.\n
4) Update existing order.\n
5) Remove existing order.\n"""))

        while orders_menu_input != 0:
            os.system('cls')
            while orders_menu_input >5 or orders_menu_input <0:
                time.sleep(0.8)
                orders_menu_input = int(input("""
Error: Selection invalid.\n
Please enter a valid option.\n\n
Orders menu:\n
0) Exit to main menu.\n
1) View list of orders.\n
2) Create a new order.\n
3) Update order status.\n
4) Update existing order.\n
5) Remove existing order.\n"""))


            if orders_menu_input == 1:
                os.system('cls')
                time.sleep(0.8)
                print(*order_list, sep = "\n\n")
                time.sleep(1.2)
                orders_menu_input = int(input("""
Orders menu:\n
0) Exit to main menu.\n
1) View list of orders.\n
2) Create a new order.\n
3) Update order status.\n
4) Update existing order.\n
5) Remove existing order.\n"""))

            elif orders_menu_input == 2:
                os.system('cls')
                time.sleep(0.8)
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
                time.sleep(1)
                print(f"New order for {name_input} has been added\n")
                time.sleep(5)
                orders_menu_input = int(input("""
Orders menu:\n
0) Exit to main menu.\n
1) View list of orders.\n
2) Create a new order.\n
3) Update order status.\n
4) Update existing order.\n
5) Remove existing order.\n"""))

            elif orders_menu_input == 3:
                os.system('cls')
                time.sleep(0.8)
                for (iteration, item) in enumerate(order_list):
                    print(iteration, item, sep = " ")
                time.sleep(0.8)
                order_list_update_index_input = int((input("Please enter the index of the order to update the status of\n")))
                time.sleep(0.8)
                print(f"You have selected {order_list[order_list_update_index_input]} to update\n")
                to_update_status_dict = {}
                to_update_status_dict.update(order_list[order_list_update_index_input])
                time.sleep(0.8)
                status_update_input = input("Please enter the status update i.e 'out for delivery' \n")
                to_update_status_dict["status"] = status_update_input
                order_list[order_list_update_index_input] = to_update_status_dict
                time.sleep(0.8)
                print(f"You have succesfully updated the order to '{status_update_input}'")
                time.sleep(0.8)
                print(order_list[order_list_update_index_input])
                orders_menu_input = int(input("""
Orders menu:\n
0) Exit to main menu.\n
1) View list of orders.\n
2) Create a new order.\n
3) Update order status.\n
4) Update existing order.\n
5) Remove existing order.\n"""))


            elif orders_menu_input == 4:
                os.system('cls')
                time.sleep(0.8)
                for (iteration, item) in enumerate(order_list):
                    print(iteration, item, sep = " ")
                time.sleep(0.8)
                order_list_index_input = int((input("Please enter the index of the order you wish to update\n")))
                time.sleep(0.8)
                print(f"You have selected {order_list[order_list_index_input]} to update\n")
                to_update_dictionary = {}
                to_update_dictionary.update(order_list[order_list_index_input])
                time.sleep(0.8)
                order_replace_key_input = input("\nPlease enter the part of the order you wish to update e.g. customer_name.\n")
                time.sleep(0.8)
                order_replace_value_input = input("Now enter the updated information\n")
                to_update_dictionary[order_replace_key_input] = order_replace_value_input
                order_list[order_list_index_input] = to_update_dictionary
                print(f"order list has been updated{order_list}\n")
                time.sleep(0.8)
                orders_menu_input = int(input("""
Orders menu:\n
0) Exit to main menu.\n
1) View list of orders.\n
2) Create a new order.\n
3) Update order status.\n
4) Update existing order.\n
5) Remove existing order.\n"""))

            elif orders_menu_input == 5:
                os.system('cls')
                time.sleep(0.8)
                for (iteration, item) in enumerate(order_list):
                    print(iteration, item, "\n")
                orders_menu_delete_input = int(input("Please enter the number of the order you would like to delete from the list\n"))
                print(f"You have selected {order_list[orders_menu_delete_input]} to delete\n")
                del order_list[orders_menu_delete_input]
                os.system('cls')
                print("The updated order list is as follows:\n", order_list)
                orders_menu_input = int(input("""
Orders menu:\n
0) Exit to main menu.\n
1) View list of orders.\n
2) Create a new order.\n
3) Update order status.\n
4) Update existing order.\n
5) Remove existing order.\n"""))

            else:
                os.system('cls')
                break


## keep this section at the end of the sub menu options as this re-displays the main menu for renavigation ##
    main_menu_input = int(input("""
Main Menu\n
0) Exit.\n
1) Product menu.\n
2) Orders menu.\n"""))

print("Thank you for using Percival's Personalised Practical Solutions\n")
time.sleep(0.8)
print("Good bye, have a beautiful day!")
time.sleep(5)
os.system('cls')
exit