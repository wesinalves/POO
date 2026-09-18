from abc import ABCMeta

class PrinterMixin(metaclass=ABCMeta):
    def print_me(self):
        print(self)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person, PrinterMixin):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

if __name__ == "__main__":
    emp = Employee("John Doe", 30, 50000)
    emp.print_me()  # This will print the Employee object representation