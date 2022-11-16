import os
import time
from csv import DictReader
from csv import DictWriter


def convert_couriers_file_to_dict_list():
    # returns a list of dicts from the .csv file specified ##
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


## courier menu ##
def courier_menu():
    # displays c menu, uses input to return selected menu
    c_command = int(input("""
Courier Menu:\n
Please select from the options below:\n\n
0) Exit.\n
1) Courier list.\n
2) Create new courier.\n
3) Update exsiting courier.\n
4) Remove courier.\n"""))
    while c_command != 0:
        if c_command >4 or c_command <0:
            print("Error")
            time.sleep(2)
            courier_menu()
        if c_command == 1:
            view_couriers()
        if c_command == 2:
            create_new_courier()
        if c_command == 3:
            update_courier()
        if c_command == 4:
            delete_courier()
            
    print("Exiting to main menu")
    main_menu()

def view_couriers():
    enumerate_courier_list()
    courier_menu()

def create_new_courier():
    # uses input to create new courier. returns to c menu
    new_courier = input("Please enter the name of the new courier:\n")
    new_courier_number = input("please enter the couriers contact number:\n")
    courier_file_list.append(new_courier)
    courier_file_list.append(new_courier_number)
    print(f"New courier, {new_courier}, has been added to the courier list\n")
    courier_menu()

def enumerate_courier_list():
    # loops through and enumerates courier list - does however include the headings which ill have to exclude.
    for (iteration, item) in enumerate(courier_file_list):
        print(iteration, item, sep = " ")

def update_courier():
    enumerate_courier_list()
    index_to_update = int(input("index value of courier to update: "))
    courier_replace_key_input = input("enter name or number: ")
    courier_file_list[index_to_update][courier_replace_key_input] = input("enter new info: ")
    courier_menu()

def delete_courier():
    # uses input to delete courier from list. returns to c menu
    enumerate_courier_list()
    delete_input = int((input("Please enter the index of the courier you wish to delete\n")))
    print(f"You have removed {courier_file_list[delete_input]} from the courier list\n")
    del courier_file_list[delete_input]
    print(courier_file_list)
    courier_menu()