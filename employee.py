class Employee:
    """Class to create an employee"""

    def __init__(self, first_name: str, last_name: str, salary: int, shift: object) -> None:
        self._first_name: str = first_name
        self._last_name: str = last_name
        self.salary: int = salary
        self.shift: object = shift

    def get_full_name(self) -> str:
        return f'{self._first_name} {self._last_name}'


# Inheritance
class Mechanic(Employee):
    """Class to set the job title for mechanics"""
    # Polymorphism
    job_title: str = 'Mechanic'


# Inheritance
class Attendant(Employee):
    """Class to set the job title for station attendants"""
    # Polymorphism
    job_title: str = 'Station Attendant'


# Inheritance
class Cook(Employee):
    """Class to set the job title for cooks"""
    # Polymorphism
    job_title: str = 'Cook'


# Inheritance
class Manager(Employee):
    """Class to set the job title for managers"""
    # Polymorphism
    job_title: str = 'Manager'
