from orders_crud_functions import update_order

def test_update_order():

    stub_order_list = [{
        'customer_name': 'Philip J. Fry', 
        'customer_address': 'Planet Express West 57th Street Manhatten New New York United States', 
        'customer_phone': '07300030001', 
        'assigned_courier': '', 
        'status': 'preparing'
        }]

    assert stub_order_list.get("customer_name") == "Philip J. Fry"

    update_order(stub_order_list, order_index=0, order_key="customer_name", new_order_value="Paddy McPaddy")

    assert stub_order_list.get("customer_name") == "Paddy McPaddy"