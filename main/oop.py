# class Employee:
#     company="Google"

#     def get_salary(self):
#         return 1000
    
# e = Employee()
# print(e.get_salary()) 

# e2=Employee()
# print(e2.get_salary())
# print(e2.company) 


# learning constructors
# class Employee:
#     def __init__(self,salaey,name,bond):
#         self.salary=salaey
#         self.name=name
#         self.bond=bond

#     def get_salary(self):
#         return self.salary
    
#     def get_info(self):
#         print(f"Name: {self.name}, Salary: {self.salary}, Bond: {self.bond}")
    
# e1 = Employee(34000,"John",2)
# print(e1.get_salary())
# e1.get_info()

# e2=Employee(50000,"Doe",3)
# e2.get_info()


# instance and class attributes

class Employee:
    company="Asus"

    def __init__(self,salaey,name,bond,company):
        self.salary=salaey
        self.name=name
        self.bond=bond
        self.company=company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Bond: {self.bond}")

e1 = Employee(34000,"John",2,"tesla")
print(e1.company)
print(Employee.company)

e2 =Employee(50000,"Doe",3,"Google")
print(e2.company)
print(e2.get_salary())