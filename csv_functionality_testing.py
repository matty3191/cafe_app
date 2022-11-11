import csv
from csv import DictReader

def convert_couriers_file_to_dict_list():
## returns a list of dicts from the .csv file specified ##
    with open('data/couriers.csv', 'r') as cf:
        courier_contents = DictReader(cf)
        courier_list = list(courier_contents)

    return courier_list

def save_courier_files():
    # opens file, uses for loop to add uodated list to file. saves and closes file.
    with open('data/couriers.csv', 'w+') as csf:
        for row in courier_file_list:
            csf.write(row + "\n")

courier_file_list = convert_couriers_file_to_dict_list()

print(courier_file_list)