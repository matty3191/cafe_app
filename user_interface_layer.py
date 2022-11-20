###"""Main menu interface"""###
def main_menu_options():
    print ("""Main Menu\n
0) Exit.\n
1) Product menu.\n
2) Courier menu.\n
3) Orders menu\n""")

###"""products interface"""###
def products_menu_interface():
    print("""Product Menu:\n
0) Exit.\n
1) Product list.\n
2) Create new product.\n
3) Update existing product.\n
4) Remove product.\n""")

def enumerate_products_list(product_list_of_dicts):
    for (i, item) in enumerate(product_list_of_dicts):
        print(i, item, "\n")

###"""couriers interface"""###
def courier_menu_interface():
    print("""Courier Menu:\n
0) Exit.\n
1) Courier list.\n
2) Create new courier.\n
3) Update existing courier.\n
4) Remove courier.\n""")

def enumerate_courier_list(courier_list_of_dicts):
    for (iteration, courier) in enumerate(courier_list_of_dicts):
        print(iteration, courier, sep = " ")

###"""orders interface"""###
def order_menu_interface():
    print("""Orders menu:\n
0) Exit to main menu.\n
1) View list of orders.\n
2) Create a new order.\n
3) Update order status.\n
4) Update existing order.\n
5) Remove existing order.\n""")

def enumerate_organise_orders_by_list(organise_orders_by_list):
    for (iteration, status) in enumerate(organise_orders_by_list):
        print(iteration, status, sep = " ")

def enumerate_order_list(order_list_of_dicts):
    for (iteration, order) in enumerate(order_list_of_dicts):
        print(iteration, order, sep = " ")

def enumerate_order_status_list(order_Status_list):
    for (iteration, status) in enumerate(order_Status_list):
        print(iteration, status, sep = " ")





