def enumerate_order_list(order_file_list):
    # enumerates and prints orders list
    for index, item in enumerate(order_file_list):
        print(index, item, sep = " ")

def view_orders(orders_menu, order_file_list):
    # prints the orders list
    enumerate_order_list(order_file_list)
    orders_menu()