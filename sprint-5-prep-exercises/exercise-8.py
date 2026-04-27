import sys
from dataclasses import dataclass
from enum import Enum
from typing import List

# OperatingSystem enum
class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"
    WINDOWS = "Windows"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Apple", model="MacBook", screen_size_in_inches=16, operating_system=OperatingSystem.MACOS),
    Laptop(id=6, manufacturer="Lenovo", model="ThinkPad", screen_size_in_inches=14, operating_system=OperatingSystem.WINDOWS),
]

def string_to_operating_system(text: str) -> OperatingSystem:
    text = text.strip().lower()
    
    if text == "macos":
        return OperatingSystem.MACOS
    elif text == "arch linux" or text == "arch":
        return OperatingSystem.ARCH
    elif text == "ubuntu":
        return OperatingSystem.UBUNTU
    elif text == "windows":
        return OperatingSystem.WINDOWS
    else:

        print(f"Error: '{text}' is not a valid operating system", file=sys.stderr)
        print("Valid options: macOS, Arch Linux, Ubuntu, Windows", file=sys.stderr)
        sys.exit(1)


def string_to_age(text: str) -> int:
    try:
        age = int(text)
        if age < 0 or age > 150:
            print("Error: Age must be between 0 and 150", file=sys.stderr)
            sys.exit(1)
        return age
    except ValueError:
        print("Error: Age must be a number", file=sys.stderr)
        sys.exit(1)

def count_laptops_by_os(laptops: List[Laptop]) -> dict:
    counts = {}
    for laptop in laptops:
        os_name = laptop.operating_system.value
        if os_name in counts:
            counts[os_name] += 1
        else:
            counts[os_name] = 1
    return counts

def find_most_common_os(counts: dict) -> str:
    most_common = ""
    highest_count = 0
    for os_name, count in counts.items():
        if count > highest_count:
            highest_count = count
            most_common = os_name
    return most_common

print("=== Library Laptop Checkout System ===")
print()

name = input("Enter your name: ")
if name.strip() == "":
    print("Error: Name cannot be empty", file=sys.stderr)
    sys.exit(1)

age_text = input("Enter your age: ")
age = string_to_age(age_text)

os_text = input("Enter your preferred operating system (macOS, Arch Linux, Ubuntu, Windows): ")
preferred_os = string_to_operating_system(os_text)

person = Person(name=name, age=age, preferred_operating_system=preferred_os)

print()
print(f"Hello {person.name}!")

matching_laptops = find_possible_laptops(laptops, person)
count = len(matching_laptops)

print(f"The library has {count} laptop(s) with {person.preferred_operating_system.value}.")

if count > 0:
    print("Available laptops:")
    for laptop in matching_laptops:
        print(f"  - {laptop.manufacturer} {laptop.model} ({laptop.screen_size_in_inches}\")")
else:
    print("Sorry, no laptops available with that operating system.")


os_counts = count_laptops_by_os(laptops)
most_common = find_most_common_os(os_counts)
most_common_count = os_counts[most_common]

if most_common != person.preferred_operating_system.value and most_common_count > count:
    print()
    print(f"Tip: If you're willing to use {most_common},")
    print(f"     there are {most_common_count} laptop(s) available!")