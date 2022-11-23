# Solo mini project # 

## Project background ##

Your client has launched a pop-up café in a busy business district. They are offering home-made lunches and refreshments to the surrounding
offices. As such, they require a software application which helps them to log and track orders.

The client fed us updated requirements week by week but it culminated in the client wanting us to create a command line interface based application to help with the running of their business. The application will be used to help keep track of the available products, the orders and the couriers. The client needs to be able to perform basic create, read, update and delete (CRUD) functionality on their data and persist that data to .csv files.

## Week 1 ##
The starting requirements required that the applicaiton could create, add, delete and udate a product to a list and the option to view a  complete product list.

For this week I set about setting up the basic structure of the application. The client requirements were basic, so I chose to keep my solution simple utilising lists as instructed and incorporating simple user input based create, read, update and delete methods to edit the data.
My code initially ran sequentially without functions or loops, using if statements to navigate around. I kept the solution simple as to match the requirements of the client.

## Week 2 ##
The client's requirements were added to and this week included creating, updating, deleting a courier with the option of viewing all couriers. The products and couriers lists should be a list of strings.

To meet this, I introduced while loops to keep the user in a menu until using an input to navigate out of it. I also introduced many sleep and screen clear functions to tidy up the terminal display. This version also saw some basic 'if' statement input validation to ensure the app didn't crash with accidental erroneous input when moving between menus. I used many iterations of list and dictionary methods to manipulate the data entered. Data was still only stored in RAM memory at this point and not persisted.

## Week 3 ##
The client now wanted to inlude the CRUD functionality for a list of orders, however this was to be a list of dictionaries. Couriers and products should still be a list of strings, containing just the name of the product and name of the courier. Data should also be persisted into .txt files.

I noticed that I was re-using a lot of code between different menu options, as a result I began implementing functions in my code. The purpose was to begin grouping similar blocks of code together for clarities sake when reading. This also removed the dependency of the application to run on 'if' statements as python read the code line by line. This meant I could introduce an entry point to the app by calling a function after defining everything. This also made it more simple to implement the additional requirements set by the client. While this did improve the efficiency under the hood, I did also start down a path of nesting function calls and recursive function calling. As the code became more complex, I also removed the screen clear and time functions from most of my code for the sake of clarity/ readability. I also implemented code to save data to .txt files. This meant I had to begin restructuring my directory to better suit the needs of the application.

## Week 4 ##
The requirements evolved again, this time every list (couriers, orders and products) should now be a list of dictionaries. the products should have name and price keys, the couriers should have name and phone number keys and an orders dictionary should have name, address, phone, assigned courier, order status and items ordered keys with the optino to set a courier and items ordered when creating a new order. data should now be persisted into .csv files. Furthermore, the client specified that they would now like unit test performed on the application.

## Week 5 + 6 ## 
The client now wants to persist data in a database and the option to list orders by the order status and courier.
These requirements will be introduced in the future.

## Where the application is at now ##

**Requirements for this week:**
* create a product, courier, or order dictionary and add it to a list
* view all products, couriers, or orders
* update the status of an order
* persist my data
* STRETCH update or delete a product, order, or courier
* convert all extising lists into list of dictionaries
* data should be persisted in .csv files, to a new line for each courier, order, or product.
* BONUS list orders by status or courier

## In order to meet the requirements for this week, I have ##
- converted lists into lists of  dictionaries i.e. {"name" : "coke zero", "price" : 0.8}, {"name" : "Patrick", "phone" : "0798776887"}
- added assigned courier and item keys to the order dictionary
- started using .csv files in place of .txt and modified the file handlers as such
- restructured directory and modules
    - set up new files and folders which:
        - have separated out the main app and functions from unit testing
        - sequestered away gitignore files
        - moved the data files to a separate location     
- restructured my core functions to be as slimline as possible to increase testability and increase longevity of the application.
- created this READ-ME file.
- written unit tests for PyTest for all core CRUD and data persistence functionality.

### Demo CRUD function ###
``` Python
def create_new_product(product_list_of_dicts, new_product_name, new_product_price):
    product_list_of_dicts.append({'name': new_product_name, 'price': new_product_price})

def update_product(product_list_of_dicts, product_index, name_or_price, product_replace_value):
    product_list_of_dicts[product_index][name_or_price] = product_replace_value

def delete_product(product_list_of_dicts, delete_index):
    del product_list_of_dicts[delete_index]
```
### Demo testing: read/Write ###
``` Python
def reading_test_csv():
    with open('unit_testing/empty_test_csv.csv', 'r') as file:
        csv_contents = DictReader(file)
        csv_list = list(csv_contents)
    return csv_list

workable_csv_list = reading_test_csv()
new_data = ({'name':'bob', 'phone':'0987656789'},{'name':'bill','phone':'32165484654'})
### test file writing ###
def create_new_data_for_test_csv(workable_csv_list, new_data):
    workable_csv_list = workable_csv_list.extend(new_data)


def test_reading_and_writing_to_csv():
    assert reading_test_csv() == []
    create_new_data_for_test_csv(workable_csv_list, new_data)
    assert workable_csv_list == [{'name':'bob', 'phone':'0987656789'},{'name':'bill','phone':'32165484654'}]
    field_names = ['name','phone']
    with open('unit_testing/empty_test_csv.csv', 'w' ,newline='') as file:
        csv_writer = DictWriter(file, fieldnames = field_names)
        csv_writer.writeheader()
        for item in workable_csv_list:
            csv_writer.writerow(dict(item))

    reading_test_csv()
    assert workable_csv_list == [{'name':'bob', 'phone':'0987656789'},{'name':'bill','phone':'32165484654'}]

    with open('unit_testing/empty_test_csv.csv', 'w') as file:
        print("file emptied for test repeatabliity")
```

### Demo testing: update function ###

``` Python
def test_update_product():
    stub_product_list = [{
        'name':'coke', 'price':'1.0'
        },{
        'name':'diet coke', 'price':'0.8'
        }]
    assert stub_product_list[0]["name"] == "coke"
    update_product(product_list_of_dicts=stub_product_list, product_index=0, name_or_price="name", product_replace_value="carrot cake")
    assert stub_product_list[0]["name"] == "carrot cake"
```

#### This is the structure of the application. ####
The arrows show which layers communicate and the largest area is the testing layer which indicates what is covered by testing.
![image](https://user-images.githubusercontent.com/115237595/203532632-425f3506-323e-42ed-80ab-d137bd69832b.png)

### - How did your design meet the requirements? ###
By separating out my functions into 3 different layers (user interface layer, utility functions, crud functions), I was able to organise my code in sections which allowed me to go through each user requirement and see if my code met it. So my application displays a main menu, product menu, courier menu and orders menu; accepts user input to navigate through the menus; uses user input to perform CRUD in each sub menu and persists data when the application closes.


### - How did you guarantee the project requirements? ### 
The method of testing I chose was unit testing using PyTest. From my research it appeared that PyTest is used in the majority of real-world python based scenarios, offers faster testing and clearer more concise results as well as needing to write less code in turn increases readablity.

I applied unit testing to each element of core functionality. So as per the client requirements the application must read and write data to CSV files, perform C.R.U.D on each product, order, and courier, so after purifying the functions and abstracting them away I wrote unit tests on each to ensure that they performed without returning any unexpected results. I made each core function as simple as possible, making each perform just a single behaviour i.e. updating an entry. This meant that the testing was simple to as I only had to ensure 1 behaviour was operational. As a result I was able to provide coverage for most of the applications core behaviours in just a few test cases. Furthermore I late stage included some input validations to create a more robust application that should not crash in case of use input error.

In an ideal world, I would put more time into providing more thoughrough testing for all functionalities and not just core functions to create a more robust application that will have a longer shelf life. For example, I did not have enouogh ime to implement unit tests for the main application where the functions are less pure and where the input validations are too. It has been manually tested but this was time costly and could be improved on with more rigorous unit testing / TDD mindset.

### - If you had more time, what is one thing you would improve on? ###
If I could start this project again, I would have a more in depth discussion with the client from week 1, try to discuss fully the needs of the business and what I/my team are capabale of realistically delivering in the given time frame. I would also make a README from the start and make it much more concise!

If I had more time, I would have implemented a more rigorous functional programming mindset to group things together and allow for further abstraction making the application even more lightweight. This would have further allowed me to remove things like messy input validations into a separate file and make the base code more readable for future developers and more easily testable. In addition, I would have implemented test driven development (TDD) from the beginning. It rapidly became apparent as the clients requirements changed week by week that testing additions to the code after it has been written is difficult and takes a long time. 

Another thing I would improve with time would be to persist the data in a database as they are a more reliable method of storage and can be edited outside of the main application if for example, using MySQL or seomthing similar. Currently this solution is not a priorty as the cafe only uses a small amount of data, but this is a future consideration if the busniess increases in size. IT would however, greatly help with data organisation and data types. for example, we could create a relational database that allows the client to view the history of orders by a particular customer_id.

### - what did you most enjoy about implementing the project? ###
The thing I enjoyed implementing the most was abstracting all my core functionality away from the main application and reducing those functions down to as pure as I could make them while still retaining the main functionality. This process made clear to me how best to structure a function to make it easier to test. This really cleared up my code and made it much easier for me to read. It also took the pressure away from implementing object orientated programming which I don't fully understand at this point in time.
