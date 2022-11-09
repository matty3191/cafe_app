# f = "Postman Patrick"
# g = "Ramona Flowers"
# h = "Rocinante"

# courier_list = []

# courier_list.append(f)
# courier_list.append(g)
# courier_list.append(h)

# def open_in_list():
#     cf = open('data/couriers.txt', 'a+')
        
#     print(cf.readlines())
#     cf.close()


def convert_couriers_file_to_list():
## returns a list of the .txt file specified with the \n character truncated ##
    with open('data/couriers.txt', 'r') as cf:
        courier_contents = cf.read().splitlines()
        
    return courier_contents

# def write_couriers():
#     with open('data/couriers.txt', 'a+') as cf:
#         for name in courier_list:
#             cf.writelines(name)


x = convert_couriers_file_to_list()

#now i have the list available to me,
# edit it in the same way i did before,
#then find a way to save the changes ive made
print(x)
# write_couriers()
# open_in_list()
