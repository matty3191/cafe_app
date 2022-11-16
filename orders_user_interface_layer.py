def enumerate_order_list(order_list_of_dicts):
    # enumerates and prints orders list
    for (iteration, item) in enumerate(order_list_of_dicts):
        print(iteration, item, sep = " ")

def view_orders(orders_menu, order_list_of_dicts):
    # prints the orders list
    enumerate_order_list(order_list_of_dicts)
    orders_menu()