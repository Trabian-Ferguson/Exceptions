# Program Name: Lab10.py 
# Course: IT1114/Section 01
# Student Name: Trabian Ferguson
# Assignment Number: Lab10.py
# Due Date: 10/12/2023
# Purpose: This program encapsulates data about an office worker, but with newly added features.

class Worker:
    def __init__(self):
        #attr. or variables (features of object)
        self.employee_number = 0
        self.office_number = 0
        self.name = " "
        self.birthday = " "
        self.hoursworked = 0
        self.overtimehours = 0
        self.hourly_salary = 0
        self.overtime_salary = 0
        self.pay = 0

    # Custom Class for (AddHours)
    class AddHoursError(Exception):
        pass

     # Custom Class for (EmployeeNum)
    class EmployeeNumError(Exception):
        pass

     # Custom Class for (OfficeNum)
    class OfficeNumError(Exception):
        pass

     # Custom Class for (Name)
    class NameError(Exception):
        pass

    # Custom Class for (BirthM)
    class BirthMError(Exception):
        pass

     # Custom Class for (BirthD)
    class BirthDError(Exception):
        pass

    def get_employee_number(self):
        #method (behaviors of object)
        return self.employee_number
    
    def set_employee_number(self,x):
        if  not str(x).isnumeric():
            raise EmployeeNumError
        else:
            self.employee_number = x

    
    def get_office_number(self):
        return self.office_number
    
    
    def set_office_number(self,x):
        if x < 100 or x > 500:
        
            raise OfficeNumError
        else:
            self.office_number = x
        


    def get_name(self):
        return self.name

    def set_name(self,x):
        if x == "":
            raise NameError
        else:
            y = x.replace('_',"")
            z = y.replace('.',"")
            w = z.replace('-',"")
            self.name = w
            
# figure out how to replace things in one line
        
    
    def set_birthdate(self,d,m,y):
        if m < 1 or m > 12:
            raise BirthMError
        elif d < 1 or d > 31:
            raise BirthDError
        else:
            if d < 32 and d > 0:
                if m < 13 and m > 0:
                    self.birthday=str(m)+"/"+str(d)+"/"+str(y)
                    


    def get_hours_worked(self):
        return self.hoursworked 

    def add_hours(self,x):
        if x < 0:
            raise AddHoursError("You entered the wrong value!")

        else:
            if x > 9:
                self.hoursworked = self.hoursworked + 9 
                self.overtimehours = self.overtimehours + x-9

            else:
                self.hoursworked = self.hoursworked = x
    
    def get_hours_overtime(self):
        return self.overtimehours
    

    
    def set_hourly_salary(self,x):
        if x < 0:
            return False
        else:
            self.hourly_salary = x
            return True
        
    def set_overtime_salary(self,x):
        if x < 0:
            return False
        else:
            self.overtime_salary = x
            return True   
        
    def get_hourly_salary(self):
        return self.hourly_salary
    def get_overtime_salary(self):
        return self.overtime_salary
    
    def get_pay(self):
        self.pay = (self.hoursworked * self.hourly_salary) + (self.overtimehours * self.overtime_salary)
        return self.pay

