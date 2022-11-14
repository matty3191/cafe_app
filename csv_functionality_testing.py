from csv import DictReader
from csv import DictWriter

def convert_couriers_file_to_dict_list():
## returns a list of dicts from the .csv file specified ##
    with open('data/couriers.csv', 'r') as cf:
        courier_contents = DictReader(cf)
        courier_list = list(courier_contents)
    return courier_list

def save_courier_files():
    # opens file, uses for loop to add updated list to file. saves and closes file.
    field_names = ['name','phone']
    with open('data/couriers.csv', 'w' ,newline='') as csf:
        courier_writer = DictWriter(csf, fieldnames = field_names)
        courier_writer.writeheader()
        for courier in courier_file_list:
            courier_writer.writerow(dict(courier))

courier_file_list = convert_couriers_file_to_dict_list()
print(courier_file_list)

def delete_courier(): 
    for (index, name) in enumerate(courier_file_list):
        print(index, name, sep = " ")   
    to_del = int(input("index of courier you wish to remove: "))
    del courier_file_list[to_del]

def enumerate_courier_list():
    for (iteration, item) in enumerate(courier_file_list):
        print(iteration, item, sep = " ")

def update_courier():
    enumerate_courier_list()
    index_to_update = int(input("index value of courier to update: "))
    courier_replace_key_input = input("enter name or number: ")
    courier_file_list[index_to_update][courier_replace_key_input] = input("enter new info: ")


delete_courier()
update_courier()
save_courier_files()
