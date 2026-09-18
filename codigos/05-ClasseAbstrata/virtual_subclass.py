from abc import ABCMeta

class Person(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee():
    def __init__(self, salary):
        self.salary = salary

if __name__ == "__main__":
    print(issubclass(Employee, Person))  # This will return True
    Person.register(Employee)  # Register Employee as a virtual subclass of Person
    print(issubclass(Employee, Person))  # This will return True
    emp = Employee(50000)
    print(isinstance(emp, Person))  # This will return True