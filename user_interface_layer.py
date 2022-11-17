"""products interface"""


"""couriers interface"""
def enumerate_courier_list(courier_list_of_dicts):
    for (iteration, courier) in enumerate(courier_list_of_dicts):
        print(iteration, courier, sep = " ")

"""orders interface"""
def enumerate_order_list(order_list_of_dicts):
    for (iteration, order) in enumerate(order_list_of_dicts):
        print(iteration, order, sep = " ")

def enumerate_order_status_list(order_Status_list):
    for (iteration, status) in enumerate(order_Status_list):
        print(iteration, status, sep = " ")




