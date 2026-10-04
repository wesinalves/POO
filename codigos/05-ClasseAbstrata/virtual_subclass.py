from abc import ABCMeta, abstractmethod, ABC

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_name(self):
        pass

class Employee():
    def __init__(self, salary):
        self.salary = salary

    # def get_name(self):
    #     return super().get_name()

if __name__ == "__main__":
    print(issubclass(Employee, Person))  # This will return True
    Person.register(Employee)  # Register Employee as a virtual subclass of Person
    print(issubclass(Employee, Person))  # This will return True
    emp = Employee(50000)
    print(isinstance(emp, Person))  # This will return True