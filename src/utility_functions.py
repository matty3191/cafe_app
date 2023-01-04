from csv import DictReader
from csv import DictWriter

## File handling ##
def convert_products_file_to_list():
    with open('data/products.csv', 'r') as pf:
        product_contents = DictReader(pf)
        product_list = list(product_contents)
        
    return product_list

def save_product_files():
    field_names = ['name','price']
    with open('data/products.csv', 'w' ,newline='') as psf:
        product_writer = DictWriter(psf, fieldnames = field_names)
        product_writer.writeheader()
        for product in product_list_of_dicts:
            product_writer.writerow(dict(product))

def convert_couriers_file_to_dict_list():
    with open('data/couriers.csv', 'r') as cf:
        courier_contents = DictReader(cf)
        courier_list = list(courier_contents)
    return courier_list

def save_courier_files():
    field_names = ['name','phone']
    with open('data/couriers.csv', 'w' ,newline='') as csf:
        courier_writer = DictWriter(csf, fieldnames = field_names)
        courier_writer.writeheader()
        for courier in courier_list_of_dicts:
            courier_writer.writerow(dict(courier))

def convert_orders_file_to_list():
    with open('data/orders.csv', 'r') as o_f:
        order_contents = o_f = DictReader(o_f)
        order_list = list(order_contents)
        
    return order_list

def save_orders_files():
    field_names = ['customer_name','customer_address','customer_phone','assigned_courier','status','items']
    with open('data/orders.csv', 'w' ,newline='') as osf:
        order_writer = DictWriter(osf, fieldnames = field_names)
        order_writer.writeheader()
        for order in order_list_of_dicts:
            order_writer.writerow(dict(order))

product_list_of_dicts = convert_products_file_to_list()
courier_list_of_dicts = convert_couriers_file_to_dict_list()
order_list_of_dicts = convert_orders_file_to_list()