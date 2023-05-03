class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class House:
    def __init__(self, address, num_rooms):
        self.address = address
        self.num_rooms = num_rooms
        self.residents = []

    def add_resident(self, person):
        self.residents.append(person)

    def remove_resident(self, person):
        self.residents.remove(person)

    def print_residents(self):
        print(f"Residents of {self.address}:")
        for person in self.residents:
            print(f"{person.name}, {person.age}")
