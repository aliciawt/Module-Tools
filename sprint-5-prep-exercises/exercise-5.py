import datetime
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    date_of_birth: datetime.date
    preferred_operating_system: str
    
    def is_adult(self) -> bool:
        today = datetime.date.today()
        age = today.year - self.date_of_birth.year
        
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        
        return age >= 18

imran = Person("Imran", datetime.date(2004, 5, 15), "Ubuntu")
eliza = Person("Eliza", datetime.date(1992, 4, 26), "Arch Linux")

print(f"{imran.name} is adult? {imran.is_adult()}")
print(f"{eliza.name} is adult? {eliza.is_adult()}")
print(f"{imran.name} prefers {imran.preferred_operating_system}")