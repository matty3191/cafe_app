def create_new_courier():
    # uses input to create new courier. returns to c menu
    courier_list_of_dicts.append({'name':", 'phone':")})
    print(f"New courier has been added to the courier list\n")
    courier_menu()

def update_courier(courier_list_of_dicts, update_courier_index, name_or_phone, new_courier_information):
    courier_list_of_dicts[update_courier_index][name_or_phone] = new_courier_information

def delete_courier(courier_list_of_dicts, delete_index_value):
    del courier_list_of_dicts[delete_index_value]
    