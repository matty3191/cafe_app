class Person:
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.lastname = last_name
        self.catch_phrase = catch_phrase

    def walk(self):
        print("walking...")

    def run(self):
        print("running...")


user = Person(31, 85, 178, "matty", "percival", "chuffin eck")

user.walk()

print(user.catch_phrase)