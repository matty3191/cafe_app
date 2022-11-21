New to version 4:

- converted lists into dictionaries i.e. {"name" : "coke zero", "price" : 0.8}, {"name" : "Patrick", "phone" : "0798776887"}
- added assigned courier and items to the order dict
- started using .csv files in place of .txt
- restructured directory and modules
    - set up new files and folders which will:
        - eventually house the abstracted functions / classes
        - have a separate unit testing file
- implemented some abstraction to take some functions away from the main application
- created this READ-ME file
- written unit tests
- broken down core functions without changing app functionality to aid testing core funcitonality.




Project background
Your client has launched a pop-up café in a busy business district. They
are offering home-made lunches and refreshments to the surrounding
offices. As such, they require a software application which helps them to
log and track orders.

Week 4 Brief:

Now that we’ve learned how to work with two-dimensional data, let’s refactor
our app to use dictionaries for both product and courier.
Building upon our use of a courier index within our order, let’s create a list of
product indexes now for order items.
We’ll also need to refactor our storage layer to use .csv files rather than .txt
to bring back our persistence functionality.
To show that our code works, we will also need to write unit tests to prove that
our app works correctly

- client requirements
As a user I want to:
• create a product, courier, or order dictionary and add it to a list
• view all products, couriers, or orders
• update the status of an order
• persist my data
• STRETCH update or delete a product, order, or courier


- How did your design meet the requirements?
By separating out my functions into 3 different layers (user inferface layer, utility functions, crud functions), I was able to organise my code in sections which allowed me to go through each user requirment and see if my code met it. So my application diplays a main menu, product menu, courier menu and orders menu; accepts user input to navigate through the menus; uses user input to perform CRUD in each sub menu and persists data when the apllication closes.


- How did you guarantee the project requirements?
I applied unit testing to each element of core functionality. So as per the client requirements the application must read and write data to CSV files, perform C.R.U.D on each product, order and courier, so after purifying the functions and abstracting them away I wrote unit tests on each to ensure that they performed without returning any unexpected results.

- If you had more time, what is one thing you would improve on?
If I had more time I would have used classes to group things together and allow for further abstraction making the application even more lightweight. Furthermore I would have persisted the data in a dtabase an accessed it via an API to give some secrurity to the data and easier manipulation through my local machine.

- what did you most enjoy about implementing the project?
the thing i enjoyed implementing the most was abstracting all my core functionality away from the main application and reducing those functions down to as pure as i could make them while still retaining the main functionality. This process made clear to me how best to structure a function to make it easier to test. This really cleared up my code and made it much easier for me to read 