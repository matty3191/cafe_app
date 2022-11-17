def create_new_order(order_list_of_dicts, new_order):
    order_list_of_dicts.append(new_order)

def update_order_status(order_list_of_dicts, order_status_index_update, new_order_status_value):
    order_list_of_dicts[order_status_index_update]['status'] = new_order_status_value

def update_order(order_list_of_dicts, order_index, order_key, new_order_value):
    order_list_of_dicts[order_index][order_key] = new_order_value

def delete_order(order_list_of_dicts, delete_order_index):
    del order_list_of_dicts[delete_order_index]
