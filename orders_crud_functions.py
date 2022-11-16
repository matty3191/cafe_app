def create_new_order(order_list_of_dicts, courier_list_of_dicts, orders_menu):
    print("Create New Order")
    new_order = {
                    "customer_name":"",
                    "customer_address":"",
                    "customer_phone":"",
                    "assigned_courier":"",
                    "status":""
                }
    new_order["customer_name"] = input("Enter Customer name: ")
    new_order["customer_address"] = input("Enter customer address: ")
    new_order["customer_phone"] = input("Enter customer phone number: ")
    for (index, name) in enumerate(courier_list_of_dicts):
        print(index, name, sep = " ",)
    new_order["assigned_courier"] = int(input("Please select the index of a courier to assign to this order\n"))
    new_order["status"] = "Preparing"
    order_list_of_dicts.append(new_order)
    print("New order has been added\n")
    orders_menu()



def update_order_status(enumerate_order_list, order_status_list, orders_menu):
    enumerate_order_list()
    print(order_status_list, "\n", )
    [int(input("Please enter the index of the order to update the status of\n"))]["status"] = order_status_list (int(input("Choose the index of the new order status:\n")))
    print(f"You have succesfully updated the order status")
    orders_menu()

def update_order(order_list_of_dicts, order_index, order_key, new_order_value):
    order_list_of_dicts[order_index][order_key] = new_order_value


def delete_order(enumerate_order_list, order_list_of_dicts, orders_menu):
    enumerate_order_list()
    del order_list_of_dicts[int(input("Please enter the number of the order you would like to delete from the list:\n"))]
    print("Order succesfully deleted\n")
    orders_menu()