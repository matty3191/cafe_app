def create_new_courier(courier_list_of_dicts, new_courier_name, new_courier_phone):
    courier_list_of_dicts = courier_list_of_dicts.append({'name':new_courier_name, 'phone':new_courier_phone})

def update_courier(courier_list_of_dicts, update_courier_index, name_or_phone, new_courier_information):
    courier_list_of_dicts[update_courier_index][name_or_phone] = new_courier_information

def delete_courier(courier_list_of_dicts, delete_index_value):
    del courier_list_of_dicts[delete_index_value]
    