from user_interface_layer import enumerate_courier_list, enumerate_order_list, enumerate_order_status_list, enumerate_products_list, main_menu_options, products_menu_interface, courier_menu_interface, order_menu_interface

def test_main_menu(capsys):
    main_menu_options()
    captured_main_print = capsys.readouterr()
    assert captured_main_print.out == ("""Main Menu\n
0) Exit.\n
1) Product menu.\n
2) Courier menu.\n
3) Orders menu\n
""")

def test_products_menu(capsys):
    products_menu_interface()
    captured_product_print = capsys.readouterr()
    assert captured_product_print.out == ("""Product Menu:\n
0) Exit.\n
1) Product list.\n
2) Create new product.\n
3) Update existing product.\n
4) Remove product.\n\n""")

def test_courier_menu(capsys):
    courier_menu_interface()
    captured_print = capsys.readouterr()
    assert captured_print.out == ("""Courier Menu:\n
0) Exit.\n
1) Courier list.\n
2) Create new courier.\n
3) Update existing courier.\n
4) Remove courier.\n\n""")

def test_order_menu_interface(capsys):
    order_menu_interface()
    captured_print = capsys.readouterr()
    assert captured_print.out == ("""Orders menu:\n
0) Exit to main menu.\n
1) View list of orders.\n
2) Create a new order.\n
3) Update order status.\n
4) Update existing order.\n
5) Remove existing order.\n\n""")

def test_enumerate_products(capsys):
    stub_products_list_of_dicts = [{
        'name':'coke', 'price':'1.0'
        },{
        'name':'diet coke', 'price':'0.8'
        },{
        'name':'fanta', 'price':'1.2'
        }]
    enumerate_products_list(stub_products_list_of_dicts)
    captured_print, err = capsys.readouterr()
    assert captured_print == "0 {'name': 'coke', 'price': '1.0'} \n\n1 {'name': 'diet coke', 'price': '0.8'} \n\n2 {'name': 'fanta', 'price': '1.2'} \n\n"

def test_enumerate_couriers(capsys):
    stub_courier_list_of_dicts = [{
        'name':'Ron Swanson', 'phone':'65432165'
        },{
        'name':'Ann Perkins', 'phone':'651351613'
        },{
        'name':'Andy Dwire', 'phone':'3216356496'
        }]
    enumerate_courier_list(stub_courier_list_of_dicts)
    captured_print, err = capsys.readouterr()
    assert captured_print == "0 {'name': 'Ron Swanson', 'phone': '65432165'}\n1 {'name': 'Ann Perkins', 'phone': '651351613'}\n2 {'name': 'Andy Dwire', 'phone': '3216356496'}\n"

def test_enumerate_order_status_list(capsys):
    stub_order_status_list = ["preparing", "out for delivery", "delivered"]
    enumerate_order_status_list(stub_order_status_list)
    captured_print, err = capsys.readouterr()
    assert captured_print == '0 preparing\n1 out for delivery\n2 delivered\n'


def test_enumerate_orders(capsys):
    stub_order_list_of_dicts = [{
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
    enumerate_order_list(stub_order_list_of_dicts)
    captured_print, err = capsys.readouterr()
    assert captured_print == "0 {'customer_name': 'Philip J. Fry', 'customer_address': 'Planet Express West 57th Street Manhatten New New York United States', 'customer_phone': '07300030001', 'assigned_courier': '18', 'status': 'preparing', 'items': '1,2,15'}\n1 {'customer_name': 'Charles Montgomery Burns', 'customer_address': 'Powerplant, springfield, United States', 'customer_phone': '09885255354', 'assigned_courier': '2', 'status': 'preparing', 'items': '3,5,17,14'}\n"