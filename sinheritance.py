class company:
    def __init__(self,name,city,mobileno):
        self.name=name
        self.city=city
        self.mobileno=mobileno
    
class employee(company):
    
    def __init__(self,name,city,mobileno,desig,salary):
        self.name=name
        self.city=city
        self.mobileno=mobileno
        self.desig=desig
        self.salary=salary
     
e=employee("kalpesh zapadiya","Rajkot",7600682860,"developer",40000)
print("Name:",e.name) 
print("City:",e.city)
print("Mobile No:",e.mobileno)
print("Designation:",e.desig)
print("Salary:",e.salary)
   
        