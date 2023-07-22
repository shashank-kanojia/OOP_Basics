from employee import Mechanic, Attendant, Cook, Manager
from reporting import AccountingReport, StaffingReport, ScheduleReport
from shift import MorningShift, AfternoonShift, NightShift

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    employees: list = [
        Manager('Shashank', 'Kanojia', 333333, MorningShift()),
        Manager('Vera', 'Schmidt', 2000, MorningShift()),
        Attendant('Chuck', 'Norris', 1800, MorningShift()),
        Attendant('Samantha', 'Carrington', 1800, AfternoonShift()),
        Cook('Roberto', 'Jacketti', 2100, AfternoonShift()),
        Mechanic('Dave', 'Dreibig', 2200, AfternoonShift()),
        Mechanic('Tina', 'Rivers', 2300, NightShift()),
        Mechanic('Ringo', 'Rama', 1900, NightShift()),
        Cook('Chuck', 'Rainey', 2200, NightShift())
    ]

    reports: list = [
        AccountingReport(employees),
        StaffingReport(employees),
        ScheduleReport(employees)
    ]

    for obj in reports:
        print()
        obj.print_report()
