from orders_crud_functions import update_order, create_new_order, update_order_status, delete_order

def test_create_complete_new_order():
    stub_order_list_of_dicts = [{
        'customer_name': 'Philip J. Fry', 
        'customer_address': 'Planet Express West 57th Street Manhatten New New York United States', 
        'customer_phone': '07300030001', 
        'assigned_courier': '18', 
        'status': 'preparing',
        'items' : '1,2,15'
        }]
    stub_new_order = {'customer_name': 'Charles Montgomery Burns', 
        'customer_address': 'Powerplant, springfield, United States', 
        'customer_phone': '09885255354', 
        'assigned_courier': '2', 
        'status': 'preparing',
        'items' : '3,5,17,14'}
    create_new_order(order_list_of_dicts=stub_order_list_of_dicts, new_order=stub_new_order)
    assert stub_order_list_of_dicts == [{
        'customer_name': 'Philip J. Fry', 
        'customer_address': 'Planet Express West 57th Street Manhatten New New York United States', 
        'customer_phone': '07300030001', 
        'assigned_courier': '18', 
        'status': 'preparing',
        'items' : '1,2,15'
        },{
        'customer_name': 'Charles Montgomery Burns', 
        'customer_address': 'Powerplant, springfield, United States', 
        'customer_phone': '09885255354', 
        'assigned_courier': '2', 
        'status': 'preparing',
        'items' : '3,5,17,14'   
        }]

def test_update_order_status():
    stub_order_list_of_dicts = [{
        'customer_name': 'Philip J. Fry', 
        'customer_address': 'Planet Express West 57th Street Manhatten New New York United States', 
        'customer_phone': '07300030001', 
        'assigned_courier': '18', 
        'status': 'preparing',
        'items' : '1,2,15'
        }]
    update_order_status(stub_order_list_of_dicts, order_status_index_update=0, new_order_status_value="out for delivery")
    assert stub_order_list_of_dicts[0]["status"] == 'out for delivery'
    update_order_status(stub_order_list_of_dicts, order_status_index_update=0, new_order_status_value="delivered")
    assert stub_order_list_of_dicts[0]['status'] == 'delivered'
    update_order_status(stub_order_list_of_dicts, order_status_index_update=0, new_order_status_value="preparing")
    assert stub_order_list_of_dicts[0]["status"] == 'preparing'


def test_update_order():
    stub_order_list = [{
        'customer_name': 'Philip J. Fry', 
        'customer_address': 'Planet Express West 57th Street Manhatten New New York United States', 
        'customer_phone': '07300030001', 
        'assigned_courier': '', 
        'status': 'preparing',
        'items' : ''
        }]

    assert stub_order_list[0]["customer_name"] == "Philip J. Fry"
    update_order(stub_order_list, order_index=0, order_key="customer_name", new_order_value="Zap Brannigan")
    assert stub_order_list[0]["customer_name"] == "Zap Brannigan"

def test_delete_order():
    stub_order_list_of_dicts = [{
    'customer_name': 'Philip J. Fry', 
    'customer_address': 'Planet Express West 57th Street Manhatten New New York United States', 
    'customer_phone': '07300030001', 
    'assigned_courier': '18', 
    'status': 'preparing',
    'items' : '1,2,15'
    },{
    'entry 2':'to test delete func'
    }]
    delete_order(order_list_of_dicts=stub_order_list_of_dicts, delete_order_index=0)
    assert stub_order_list_of_dicts == [{'entry 2':'to test delete func'}]
    delete_order(order_list_of_dicts=stub_order_list_of_dicts, delete_order_index=0)
    assert stub_order_list_of_dicts == []