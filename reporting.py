class Report:
    """Superclass for the reporting subclasses"""

    def __init__(self, emp_list: list) -> None:
        self._emp_list = emp_list


# Inheritance
class AccountingReport(Report):
    """Print the salaries of the employees"""

    # Polymorphism
    def print_report(self) -> None:
        print('Accounting')
        print('==========')
        for e in self._emp_list:
            print(f'{e.get_full_name()}, ${e.salary}')


# Inheritance
class StaffingReport(Report):
    """Print the designation of the employees"""

    # Polymorphism
    def print_report(self) -> None:
        print('Staffing')
        print('========')
        for e in self._emp_list:
            print(f'{e.get_full_name()}, {e.job_title}')


class ScheduleReport(Report):
    """Print the schedule of the employees"""

    # Polymorphism
    def print_report(self) -> None:
        print('Schedule')
        print('========')
        for e in self._emp_list:
            print(f'{e.get_full_name()}, {e.shift.get_shift_info()}')
