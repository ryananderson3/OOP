#creates an employee

from re import S


class employee():

    def __init__(self,n,idn,dep,t,sal):
        self.name = n
        self.idNum = idn
        self.department = dep
        self.title = t
        self.salary = sal

    def get_Name(self):
        return self.name
    
    def get_idNum(self):
        return self.idNum
    
    def get_Department(self):
        return self.department
    
    def get_Title(self):
        return self.title
    
    def get_salary(self):
        return self.salary

