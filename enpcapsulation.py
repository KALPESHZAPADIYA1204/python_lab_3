class calculator:
    def __init__(self):
        self._result=0
    def add(self,value):
        self._result+=value 
    def sub(self,value):
        self._result-=value  
    def get_result(self):
        return self._result
    
c=calculator()
c.add(12)
print("Addition:",c.get_result())
           
c.sub(5)
print("subtraction:",c.get_result())           