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
    courier_file_list.append(new_courier)
    print(f"New courier, {new_courier}, has been added to the courier list\n")
    print(courier_file_list)
    courier_menu()

def enumerate_courier_list():
    # uses input to update courier. returns to c menu
    for (i, item) in enumerate(courier_file_list):
        print(i, item, "\n")

def update_courier():
    enumerate_courier_list()
    index_to_update = int(input("index value of courier to update: "))
    courier_replace_key_input = input("enter name or number: ")
    courier_replace_value_input = input("enter new info: ")
    courier_file_list[index_to_update][courier_replace_key_input] = courier_replace_value_input
    courier_menu()

def delete_courier():
    # uses input to delete courier from list. returns to c menu
    enumerate_courier_list()
    delete_input = int((input("Please enter the index of the courier you wish to delete\n")))
    print(f"You have removed {courier_file_list[delete_input]} from the courier list\n")
    del courier_file_list[delete_input]
    print(courier_file_list)
    courier_menu()

def open_couriers():
    with open('data/couriers.txt', 'r') as cf:
        courier_contents = cf.read()
        print(courier_contents)