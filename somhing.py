courier_list_of_dicts = [{'name':'ben','phone':'23456543'},{'name':'tom','phone':'765434567'}]

new_courier_name = input("input name: \n")
new_courier_phone = input("input phone: \n")

def create_new_courier(courier_list_of_dicts, new_courier_name, new_courier_phone):
    courier_list_of_dicts.append({'name' : new_courier_name, 'phone' : new_courier_phone})
    return courier_list_of_dicts
print(create_new_courier(courier_list_of_dicts, new_courier_name, new_courier_phone))
