class Employee:

    def __init__(self, name, position, salary):
        self.name= name
        self.position=position
        self.salary=salary

    def __str__(self):
        return "{} works as a {} and has a salary of {} USD".format(self.name,self.position,self.salary) 


listEmployee= [ 
    Employee("John", "Director", 7500),
    Employee("Sarah", "President", 6500),
    Employee("Anthony", "Accountant", 5500),
    Employee("Natalie", "Secretary", 4500),
    Employee("Kevin", "Seller", 3500)
]


def calculate_comission(employee):

    if (employee.salary<=5500):

        employee.salary=employee.salary * 1.03

    return employee


listEmployeeCommission= map( calculate_comission, listEmployee)


for employee in listEmployeeCommission:

    print(employee)

