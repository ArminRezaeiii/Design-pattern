import copy

class Person:
    def __init__(self, name, age, email=None, phone=None):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    def __str__(self):
        return f'Person(name={self.name}, age={self.age}, email={self.email}, phone={self.phone})'

    def clone(self):
        return copy.deepcopy(self)



original_person = Person(name="Ali", age=30, email="ali@example.com", phone="09121234567")
print("Original:", original_person)


cloned_person = original_person.clone()

cloned_person.name = "Reza"
cloned_person.age = 28
cloned_person.email = "reza@example.com"

print("Cloned:", cloned_person)
