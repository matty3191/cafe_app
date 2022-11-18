from orders_crud_functions import update_order, create_new_order
# test for happy path, unhappy path, common, edge and corner cases #
# e.g. testing incorrect inputs reutn an error but dont exit the program #
def test_update_order():
    """test for update"""
    stub_order_list = [{
        'customer_name': 'Philip J. Fry', 
        'customer_address': 'Planet Express West 57th Street Manhatten New New York United States', 
        'customer_phone': '07300030001', 
        'assigned_courier': '', 
        'status': 'preparing',
        'items' : ''
        }]

    assert stub_order_list.get("customer_name") == "Philip J. Fry"

    update_order(stub_order_list, order_index=0, order_key="customer_name", new_order_value="Zap Brannigan")

    assert stub_order_list.get("customer_name") == "Zap Brannigan"

def test_create_new_order():

    stub_new_order = [{
        'customer_name': 'Philip J. Fry', 
        'customer_address': 'Planet Express West 57th Street Manhatten New New York United States', 
        'customer_phone': '07300030001', 
        'assigned_courier': '', 
        'status': 'preparing',
        'items' : ''
    }]