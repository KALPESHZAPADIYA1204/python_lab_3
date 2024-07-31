name=(input("Enter the name of the Employee::"))
date=(input("Enter the join of the date::"))
designation=(input("Enter the designation::"))
salary=int(input("Enter the salary::"))
class employee:
   def __init__(self,name,date,designation,salary):
       self.name=name
       self.date=date
       self.designation=designation
       self.salary=salary
    
e=employee(name,date,designation,salary)
print("view of the data::")
print("Employee Name:",e.name)
print("date of Join:",e.date)  
print("Designation:",e.designation)
print("salary:",e.salary)  
    