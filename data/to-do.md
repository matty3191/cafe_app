-move the poducts list to products.txt
-create a list of couriers in the couriers.txt file
-write code to load both at the start of the app
-condense current repetitive if/else statements into pre-defined functions.
-write code that will persist data after being updated (maybe a save button, maybe autosave)
-remove some sleep  and clear functions.
-maybe make a secodary abstraction file to hide the functions from the main app.

create functions to break up code and this will help you reduce code repeating , for example we have made a main_menu function
do not time.sleep on every part of the code for example not at the start of the app



def main_menu():
   
   print("Howdy Partner, welcome to your custom  cafe management app.\n")
   print("Please select an option from the menu    below\n")

    command = int(input)("
       0) Exit.\n
       1) Product menu.\n
       2) Orders menu.\n"))

    while True:
          if command == 0:
              exit()
          if command == 1:
              product_menu() --> create products menu function 
          if command == 2:
              orders_menu() --> create orders menu function