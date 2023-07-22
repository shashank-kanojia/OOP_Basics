import datetime


class Shift:
    """Output the shift time for each employee"""

    def get_shift_info(self) -> str:
        return f'{self.start_time:%H:%M} to {self.end_time:%H:%M}'


# Inheritance
class MorningShift(Shift):
    # Polymorphism
    start_time: datetime.time = datetime.time(8, 00)
    end_time: datetime.time = datetime.time(16, 00)


# Inheritance
class AfternoonShift(Shift):
    # Polymorphism
    start_time: datetime.time = datetime.time(12, 00)
    end_time: datetime.time = datetime.time(20, 00)


# Inheritance
class NightShift(Shift):
    # Polymorphism
    start_time: datetime.time = datetime.time(18, 00)
    end_time: datetime.time = datetime.time(2, 00)
