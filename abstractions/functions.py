def product_menu():
    p_command = int(input("""
Product Menu:\n
Please select from the options below:\n\n
0) Exit.\n
1) Product list.\n
2) Create new product.\n
3) Update exsiting product.\n
4) Remove product.\n"""))


    while True:
        if p_command == 0:
            break
        if p_command == 1:
            print(product_list)
        if p_command == 2:
            print("Create new product:\n")
            new_item = input("Please enter the name of the new product:\n")
            product_list.append(new_item)
            print(f"New item {new_item} has been added to the product list\n")
            print(product_list)


def orders_menu():
    pass

def courier_menu():
    pass

def main_menu():
    print("Howdy Partner, welcome to your custom cafe management app.\n")
    print("Please select an option from the menu below\n")
    command = int(input)("""
0) Exit.\n
1) Product menu.\n
2) Orders menu.\n""")


    while True:
        if command == 0:
            exit()
        if command == 1:
            product_menu()
        if command == 2:
            orders_menu()
        if command == 3:
            courier_menu()