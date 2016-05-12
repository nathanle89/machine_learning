__author__ = 'nguyenle'

class Employee:

  employee_count = 0

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.employee_count += 1

  def display_count(self):
    print("Total Employee %d" % Employee.employee_count)

  def display_employee(self):
    print("Name: ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.display_employee()
emp2.display_employee()

print(Employee.employee_count)