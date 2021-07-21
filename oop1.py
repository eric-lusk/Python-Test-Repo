# Python Object-Oriented Programming


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("Eric", "Lusk", 50000)
emp_2 = Employee("Test", "User", 60000)

# print(emp_1)
# print(emp_2)

# emp_1.first = "Eric"
# emp_1.last = "Lusk"
# emp_1.email = "Eric.Lusk@company.com"
# emp_1.pay = "50000"
#
# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = "Test.User@company.com"
# emp_2.pay = "60000"

print(emp_1.email)
print(emp_2.email)

# Manual method for printing full name
# print('{} {}'.format(emp_1.first, emp_1.last))

# Calls method from Employee class
print(emp_1.fullname())
print(Employee.fullname(emp_2))
