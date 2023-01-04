from products_crud_functions import update_product, create_new_product, delete_product

def test_create_complete_new_product():
    stub_product_list_of_dicts = [{
        'name':'coke', 'price':'1.0'
        },{
        'name':'diet coke', 'price':'0.8'
        }]
    stub_new_product_name = 'fanta'
    stub_new_product_price = '1.2'
    create_new_product(product_list_of_dicts=stub_product_list_of_dicts, new_product_name=stub_new_product_name, new_product_price=stub_new_product_price)
    assert stub_product_list_of_dicts == [{
        'name':'coke', 'price':'1.0'
        },{
        'name':'diet coke', 'price':'0.8'
        },{
        'name':'fanta', 'price':'1.2'
        }]


def test_update_product():
    stub_product_list = [{
        'name':'coke', 'price':'1.0'
        },{
        'name':'diet coke', 'price':'0.8'
        }]
    assert stub_product_list[0]["name"] == "coke"
    update_product(product_list_of_dicts=stub_product_list, product_index=0, name_or_price="name", product_replace_value="carrot cake")
    assert stub_product_list[0]["name"] == "carrot cake"


def test_delete_product():
    stub_product_list_of_dicts = [{
        'name':'coke', 'price':'1.0'
        },{
        'name':'diet coke', 'price':'0.8'
        }]
    delete_product(product_list_of_dicts=stub_product_list_of_dicts, delete_index=1)
    assert stub_product_list_of_dicts == [{
        'name':'coke', 'price':'1.0'
        }]
    delete_product(product_list_of_dicts=stub_product_list_of_dicts, delete_index=0)
    assert stub_product_list_of_dicts == []