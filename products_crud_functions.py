def create_new_product(product_list_of_dicts, new_product_name, new_product_price):
    product_list_of_dicts.append({'name': new_product_name, 'price': new_product_price})

def update_product(product_list_of_dicts, product_index, name_or_price, product_replace_value):
    product_list_of_dicts[product_index][name_or_price] = product_replace_value

def delete_product(product_list_of_dicts, delete_index):
    del product_list_of_dicts[delete_index]