##basic list of products to start with

a = "apple"
b = "coffee"
c = "sandwich"
# list of couriers
d = "dpd"
e = "evri"
f = "parcel force"
#create an empty list that we can append
product_list = []
#create a list of couriers
courier_list = []
#adding each element to the end of the list
product_list.append(a)
product_list.append(b)
product_list.append(c)
#adding couriers to the list
courier_list.append(d)
courier_list.append(e)
courier_list.append(f)

print(
    product_list, courier_list
    )
# ##while loop counter to stop the program crashing
while_counter = 0

#opening menu. show the user a welcome message then display the options frrom whic the user can choose. 

print(
    "Welcome user.\n Please select an option from the menu below\n\nMain Menu\n0) Exit.\n1) Product menu."
    )
main_menu_input = int(input())
#if the option chosen is not there then an error is returned and the main menu is offered up again.
if main_menu_input >1 or main_menu_input <0:
    print(
        "Error: please make a selection from the available options"
        )
    print(
        "Please select an option from the menu below\n\nMain Menu\n0) Exit\n1) Product menu:"
        )
    main_menu_input = int(input())

#start of if statements which dictate what happens when the user input is given
# if the user inputs 0, the program exits with keyword
if main_menu_input == 0:
    exit


if main_menu_input == 1: #here the if statement displays the submenu "product menu", and allows user input to navigate the menu.
    print(
        "Product Menu:\n0) Exit.\n1) Product list.\n2) Create new product.\n3) Update exsiting product.\n4) Remove product\n5) View list of couriers."
        )
    product_menu = int(input())


    # if the input isnt in the available options, then return an error message, offer up the menu again - the menu doesnt work as the if block isnt looped.
    if product_menu >5 or product_menu <0:
        print(
            "Error: please make a selection from the available options\nProduct Menu:\n0) Exit.\n1) Product list.\n2) Create new product.\n3) Update exsiting product.\n4) Remove product\n5) View couriers."
            )
        product_menu = int(input())


    elif product_menu == 1: # print the product list, then display product menu again, and ask for user input to re-navigate around the menu.
        print(
            product_list, "\nProduct Menu:\n0) Exit.\n1) Product list.\n2) Create new product.\n3) Update exsiting product.\n4) Remove product."
            )
        product_menu = int(input())


    elif product_menu == 2: # else if user input = 2, display create new product and ask for a new user input
        print(
            "Create new product:\nPlease enter the name of the new product"
            )
        new_item = input()
        product_list.append(new_item)
        print(
            f"New item {new_item} has been added to the product list\n", product_list, "\nProduct Menu:\n0) Exit.\n1) Product list.\n2) Create new product.\n3) Update exsiting product.\n4) Remove product."
            )


    elif product_menu == 3:
        for (i, item) in enumerate(product_list):
            print(
                i, item
                )
        print(
            "Please enter the index of the product you wish to update\n"
            )
        index_input = int((input()))
        print(
            f"You have selected {product_list[index_input]} to replace"
            )
        print(
            "\nPlease enter the new product you wish to replace an old product with."
            )
        replace_input = input()
        product_list[index_input] = replace_input
        print(
            f"product list has been updated{product_list}"
            )


    elif product_menu == 4: # if input is 4, display remove product and the product list. Then ask for user input of which item to delete
        for (i, item) in enumerate(product_list):
            print(
                i, item
                )
        print(
            "Please enter the index of the product you wish to delete\n"
            )
        delete_input = int((input()))
        print(
            f"You have removed {product_list[delete_input]} from the product list"
            )
        del product_list[delete_input]
        print(
            product_list
            )
        




