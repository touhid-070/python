class Employee:
    company="Google"

    def get_salary(self):
        return 1000
    
e = Employee()
print(e.get_salary()) 

e2=Employee()
print(e2.get_salary())
print(e2.company) 