class university:
    def __init__(self,uname,city):
        self.uname=uname
        self.city=city
    
class tnrao:
    def __init__(self,stream,fees):
        self.stream=stream
        self.fees=fees
    
class student(university,tnrao):
    def __init__(self,uname,city,stream,fees,sname,EnrollNo):
        self.uname=uname
        self.city=city
        self.stream=stream
        self.fees=fees
        self.sname=sname
        self.EnrollNo=EnrollNo
s1=student("saurashtra University","Rajkot","BCA",30000,"Kalpesh Zapadiya",15448522621)
print("university name::",s1.uname) 
print("City::",s1.city) 
print("Stream::",s1.stream) 
print("fees::",s1.fees) 
print("Student's name::",s1.sname) 
print("Enrollment No::",s1.EnrollNo)            