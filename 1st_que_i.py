import json
class Employee:
    def __init__(self,name,dob,height,city,state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
        
with open(r"C:\Users\Hp\OneDrive\Desktop\Edyoda Practice\Edyoda Python Assignment 6\employee.json") as file:
    data = json.load(file)
# file = open(r"C:\Users\Hp\OneDrive\Desktop\Edyoda Practice\Edyoda Python Assignment 6\employee.json")
# data = json.load(file)
employees = []
for i in data["employees"]:
    name = i["name"]
    dob = i["DOB"]
    height = i["Height"]
    city = i["city"]
    state = i["state"]

    employee = Employee(name,dob,height,city,state)
    employees.append(employee)

for i in employees:
    print("Name : ",i.name)
    print("DOB : ",i.dob)
    print("Height : ",i.height)
    print("City : ",i.city)
    print("State : ",i.state)
    print()



    
