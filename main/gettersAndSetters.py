class Employee:
    def __init__(self,name ,salary):
        self.name=name
        self.salary=salary
    def first_name(self):
        l=self.name.split(" ")
        print(l)
        return l[0]
    def set_first_name(self):
        l=self.name.split(" ")
        l[0]=input("Enter new first name: ")
        self.name=" ".join(l)

e=Employee("John Doe", 50000)
print(e.first_name()) # Output: John
print(e.set_first_name())
print(e.first_name()) 


# static and class methods
class Employee:
    company="Google" # class variable
    def __init__(self,name ,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def get_company(cls):
        return cls.company
    @staticmethod
    def get_salary():
        return 50000
    
e=Employee("John Doe", 50000)
print(e.get_company()) # Output: Google
print(e.get_salary()) # Output: 50000
