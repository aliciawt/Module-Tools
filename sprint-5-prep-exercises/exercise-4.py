class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
print(imran.address) # Error: "Person" has no attribute "address"

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
print(eliza.address) # Error: "Person" has no attribute "address"

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))

# Another example of accessing a non-existent property
def get_person_phone(person: Person) -> str:
    return person.phone_number  # Error: 'phone_number' does not exist in Person class