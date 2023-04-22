class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

people = [
    Person('Alice', 25),
    Person('Bob', 30),
    Person('Charlie', 20)
]

sorted_people = sorted(people)

for person in sorted_people:
    print(person.name, person.age)