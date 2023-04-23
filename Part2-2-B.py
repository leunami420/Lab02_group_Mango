class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [
    Person('Alice', 25),
    Person('Bob', 30),
    Person('Charlie', 20)
]

sorted_people = sorted(people, key = lambda per : per.age)

for person in sorted_people:
    print(person.name, person.age)


