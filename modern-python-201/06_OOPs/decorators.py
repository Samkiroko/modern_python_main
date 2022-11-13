"""
Decorators:
-----------
They are used to implement particular behavior for our classes.

Summary:
--------
1. property - Acts like a instance variable, no need to call like function.
2. static method - Directly called from the class.
3. class method - Returns a new instance of the class.
4. getter & setter - Used for `Data Encapsulation`.

Info:
-----
We can mark the class as `final` so that no other class can subclass it.

"""

from __future__ import annotations

from datetime import datetime
from enum import Enum, auto
from typing import final


# ____________________________________________________________________________


class Role(Enum):
    """Roles for staff members"""

    ASSOCIATE = auto()
    SUPERVISOR = auto()
    MANAGER = auto()


# ____________________________________________________________________________


class Person:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return f"Person: {self.fname} {self.lname}"

    @property
    def fullname(self) -> str:
        return f"{self.fname} {self.lname}"


# ____________________________________________________________________________


class Staff(Person):
    def __init__(self, fname: str, lname: str, staff_id: int, role: Role) -> None:
        super().__init__(fname, lname)

        self.staff_id = staff_id
        self.is_staff = True
        self.role = role
        # private member
        self._date_joined = datetime.now()
        # Dynamically create & assign variables

        match role:
            case Role.ASSOCIATE:
                self.__salary: float = 15
            case Role.SUPERVISOR:
                self.__salary: float = 20
            case Role.MANAGER:
                self.__salary: float = 25

    def __str__(self) -> str:
        return f"staff => Name: {self.fullname}, ID: {self.staff_id}"

    @classmethod
    def new(cls, person: Person, staff_id: int, role: Role) -> Staff:
        """
        Create a new `staff` instance

        NOTE: it takes `class` as the first argument and return a instance
        of that class
        """
        return cls(person.fname, person.lname, staff_id, role)

    @property
    def joined_on(self) -> str:
        """Joining date of staff member."""
        return f"{self._date_joined.strftime('%B %d, %Y')}"

    @property
    def salary(self) -> float:
        """`GETTER` return the salary"""
        return self.__salary

    @salary.setter
    def salary(self, amt: float) -> None:
        """`SETTER` set salary after validation."""
        if self.role == Role.ASSOCIATE and amt < 15:
            print("Erro! Associate connot have salary less than $15/hr")
        elif self.role == Role.SUPERVISOR and amt < 20:
            print("Erro! Associate connot have salary less than $20/hr")
        elif self.role == Role.MANAGER and amt < 25:
            print("Erro! Associate connot have salary less than $25/hr")
        else:
            self.__salary = amt
            print(f"{self.fullname} now has a salary of ${self.salary}")


# ____________________________________________________________________________


p1 = Person("Louis", "Zappa")

print(p1)

print(p1.fullname)


s = Staff("Chiko", "Jonas", 3245, Role.MANAGER)
print(s)

s1 = Staff.new(p1, 1234, Role.SUPERVISOR)
print(s1)

print(s1.joined_on)
print(s1.salary)

s1.salary = 28
