
def convert_couriers_file_to_list():
## returns a list of the .txt file specified with the \n character truncated ##
    with open('data/couriers.txt', 'r') as cf:
        courier_contents = cf.read().splitlines()
        
    return courier_contents

def convert_products_file_to_list():
## returns a list of the .txt file specified with the \n character truncated ##
    with open('data/products.txt', 'r') as cf:
        product_contents = cf.read().splitlines()
        
    return product_contents

# assigns the returned values to a variable so the global scope code can use it
product_file_list = convert_products_file_to_list()
courier_file_list = convert_couriers_file_to_list()

# test print #
print(product_file_list, courier_file_list)

# test appending#
new_item = "water"
product_file_list.append(new_item)
# test append #
new_courier = "Sister Maria Julie Andrews"
courier_file_list.append(new_courier)
# test print #
print(product_file_list, "\n", courier_file_list)

def save_courier_files():
    # opens file, uses for loop to add uodated list to file. saves and closes file.
    with open('data/couriers.txt', 'w+') as csf:
        for name in courier_file_list:
            csf.write(name + "\n")

def save_product_files():
    # opens file, uses for loop to add uodated list to file. saves and closes file.
    with open('data/products.txt', 'w+') as csf:
        for name in product_file_list:
            csf.write(name + "\n")

save_courier_files()
save_product_files()