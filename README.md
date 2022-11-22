# Solo mini project for generation # 


## Project background ##

Your client has launched a pop-up café in a busy business district. They
are offering home-made lunches and refreshments to the surrounding
offices. As such, they require a software application which helps them to
log and track orders.
The client wants us to create a command line interface based application to help wiht the running of their business. The application is help keep track of the available products, the orders and the couriers. The client needs to be able to perform basic CRUD functionality on their data with the potential scope for improvements as their use case matures.

## week 1 ##

This week was about creating a basic user interface focusing on user inputs and basic list data structures.

**Goals:**

* create a product and add it to a list
* view all products
* STRETCH update or delete a product

**Retro:**

For this week I set about setting up the basic structure of the application. The client requirements were basic so I chose to keep my solution simple utilising lists as instructed and incorporating simple user input based create, read, update and delete methods to edit the data.
My code intially ran sequentially without functions or loops, using if statements to navigate around. I kept the solution simple as to match the requirements of the client.


## week 2 ##

This week the client wanted to create more menus and provide CRUD options within those menus.
* create a product or courier and add it to a list
* view all products or couriers
* persist my data
* STRETCH I want to be able to update or delete a product or courier

**Specification:**

* A product should just be a string containing its name, i.e: "Coke Zero"
* A list of products should be a list of strings , i.e: ["Coke Zero"]
* A courier should just be a string containing its name, i.e: "John"
* A list of couriers should be a list of strings , i.e: ["John"]
* Data should be persisted to a .txt file on a new line for each courier or product

**Retro:**

For week two, the client increased the requirements of the app. I introduced while loops to keep the user in a menu until using an input to navigate out of it. I also introduced many sleep and screen clear functions to tidy up the terminal display. This version also saw some basic 'if' statement input validation to ensure the app didn't crash with acciendtal erroneous input when moving between menus. i used many iterations of list and dictionary methods to manipulate the data entered.


## week 3 ##

as the code base became more complex with client requirements, this week I focussed on utilising functions to decrease repeated code blocks while implementing the new changes as requested by the client.

**Goals:**

* create a product, courier, or order and add it to a list
* view all products, couriers, or orders
* update the status of an order
* persist my data (products and couriers)
* STRETCH update or delete a product, order, or courier

**Specification:**

* A product should just be a string containing its name, i.e: "Coke Zero"
* A list of products should be a list of strings, i.e: ["Coke Zero"]
* A courier should just be a string containing its name, i.e: "John"
* A list of couriers should be a list of strings, i.e: ["John"]
* An order should be a dict, i.e:

-Retro:**

In week 3, I noticed that I was re-using a lot of code between different menu options, as a result I began implementing funcitons in my code. The purpose was to begin grouping similiar blocks of code together for clarities sake when reading. This also removed the dependency of the application to run on 'if' statements as python read the code line by line. This meant I could introduce an entry point to the app by calling a function after defining everything. While this did improve the efficiency under the hood, I did also start down a path of nesting function calls and recursive function calling. As the code became more complex I also removed the screen clear and time functions from most of my code for the sake of clarity/ readabliity. I also implemented code to save data to .txt files. This meant I had to begin resturcturing my directory to better suit the needs of the application.

## Week 4 ##

**goals:**

• create a product, courier, or order dictionary and add it to a list
• view all products, couriers, or orders
• update the status of an order
• persist my data
• STRETCH update or delete a product, order, or courier
• BONUS list orders by status or courier

**Specificaiton:**

* convert all extising lists into list of dictionaries i.e
    * {
"name": "Coke Zero",
"price": 0.8 // Float
}
* data should be persisted in .csv files, to a new line for each courier, order, or product.

## New for version 4: ##
- converted lists into lists of  dictionaries i.e. {"name" : "coke zero", "price" : 0.8}, {"name" : "Patrick", "phone" : "0798776887"}
- added assigned courier and item keys to the order dictionary
- started using .csv files in place of .txt and moidifed the file handlers as such
- restructured directory and modules
    - set up new files and folders which:
        - have separated out the main app anf functions from unit testing
        - sequestered away gitignore files
        - moved the data files to a separate location
- restructured my core functions to be as slimline as possible to increase testability and increase longeivty of the application.
- created this READ-ME file to retroactively reflect on my jounrey through making this app.
- written unit tests for PyTest for all core CRUD and data peresistence functionality. 
- broken down core functions without changing app functionality to aid testing core funcitonality.


**include here a basic draw.io of the flow / structure of my app**

### - How did your design meet the requirements? ###
how does each section of code enure i've met the client requirements? what are the pros and cons of each section?
By separating out my functions into 3 different layers (user inferface layer, utility functions, crud functions), I was able to organise my code in sections which allowed me to go through each user requirment and see if my code met it. So my application diplays a main menu, product menu, courier menu and orders menu; accepts user input to navigate through the menus; uses user input to perform CRUD in each sub menu and persists data when the apllication closes.


### - How did you guarantee the project requirements? ### 
how did i test? what did i test and why? how didmy testing ensure the robustness of the app?
I applied unit testing to each element of core functionality. So as per the client requirements the application must read and write data to CSV files, perform C.R.U.D on each product, order and courier, so after purifying the functions and abstracting them away I wrote unit tests on each to ensure that they performed without returning any unexpected results.


### - If you had more time, what is one thing you would improve on? ###
what other tehniques and software deisgn ideas are there that you know, what are the pros and cons and how would you implement them? 
what about your existing code would you change? 
what about utilising design based methodologies like agile? or being a little more focussed on working witht eh client to better understand their needs from the offset rather than adapting to changes each week as their needs became more apparent?

If I had more time I would have used classes to group things together and allow for further abstraction making the application even more lightweight. Furthermore I would have persisted the data in a dtabase an accessed it via an API to give some secrurity to the data and easier manipulation through my local machine. Furthermore, I would like to inclulde the facility to add the sum of the toatl prices of items to each order and add a field that displatyed the total price in the order list. In order to do this I would have to enure that the "price" key value pair is converted into a float upon retreival from the CSV file.


### - what did you most enjoy about implementing the project? ###
which parts did you find particularly enjoyable / difficult / challenging and why?
the thing i enjoyed implementing the most was abstracting all my core functionality away from the main application and reducing those functions down to as pure as i could make them while still retaining the main functionality. This process made clear to me how best to structure a function to make it easier to test. This really cleared up my code and made it much easier for me to read 

## Installation instructions using Git clone ##
