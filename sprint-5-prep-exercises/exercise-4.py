import datetime

class Person:
    def __init__(self, name: str, date_of_birth: datetime.date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", datetime.date(2004, 5, 15), "Ubuntu")
print(imran.name)
print(imran.address) # Error: "Person" has no attribute "address"

eliza = Person("Eliza", datetime.date(1992, 4, 26), "Arch Linux")
print(eliza.name)
print(eliza.address) # Error: "Person" has no attribute "address"

def is_adult(person: Person) -> bool:
    today = datetime.date.today()
    age = today.year - person.date_of_birth.year
    if (today.month, today.day) < (person.date_of_birth.month, person.date_of_birth.day):
        age -= 1
    return age >= 18

print(is_adult(imran))

# Another example of accessing a non-existent property
def get_person_phone(person: Person) -> str:
    return person.phone_number  # Error: 'phone_number' does not exist in Person class