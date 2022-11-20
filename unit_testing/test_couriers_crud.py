from couriers_crud_functions import update_courier, create_new_courier, delete_courier

def test_create_complete_new_courier():
    stub_courier_list_of_dicts = [{
        'name':'Arjan Codes', 'phone':'07500500500'
        },{
        'name':'Rambo', 'phone':'07666777888'
        }]
    stub_new_courier_name = 'Lucifer'
    stub_new_courier_price = '07666666666'
    create_new_courier(courier_list_of_dicts=stub_courier_list_of_dicts, new_courier_name=stub_new_courier_name, new_courier_phone=stub_new_courier_price)
    assert stub_courier_list_of_dicts == [{
        'name':'Arjan Codes', 'phone':'07500500500'
        },{
        'name':'Rambo', 'phone':'07666777888'
        },{
        'name':'Lucifer', 'phone':'07666666666'
        }]


def test_update_courier():
    stub_courier_list = [{
        'name':'Arjan Codes', 'phone':'07500500500'
        },{
        'name':'Rambo', 'phone':'07666777888'
        }]
    assert stub_courier_list[0]["name"] == "Arjan Codes"
    update_courier(courier_list_of_dicts=stub_courier_list, update_courier_index=0, name_or_phone="name", new_courier_information="Aang")
    assert stub_courier_list[0]["name"] == "Aang"


def test_delete_courier():
    stub_courier_list_of_dicts = [{
        'name':'Arjan Codes', 'phone':'07500500500'
        },{
        'name':'Rambo', 'phone':'07666777888'
        }]
    delete_courier(courier_list_of_dicts=stub_courier_list_of_dicts, delete_index_value=1)
    assert stub_courier_list_of_dicts == [{
        'name':'Arjan Codes', 'phone':'07500500500'
        }]
    delete_courier(courier_list_of_dicts=stub_courier_list_of_dicts, delete_index_value=0)
    assert stub_courier_list_of_dicts == []