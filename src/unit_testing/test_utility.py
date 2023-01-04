from utility_functions import *

### test file reading ###
def reading_test_csv():
    with open('src/unit_testing/empty_test_csv.csv', 'r') as file:
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
    with open('src/unit_testing/empty_test_csv.csv', 'w' ,newline='') as file:
        csv_writer = DictWriter(file, fieldnames = field_names)
        csv_writer.writeheader()
        for item in workable_csv_list:
            csv_writer.writerow(dict(item))

    reading_test_csv()
    assert workable_csv_list == [{'name':'bob', 'phone':'0987656789'},{'name':'bill','phone':'32165484654'}]

    with open('src/unit_testing/empty_test_csv.csv', 'w') as file:
        print("file emptied for test repeatabliity")