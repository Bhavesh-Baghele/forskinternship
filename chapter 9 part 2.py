class Employee:
    #class variable
    num_of_emps = 0
    
    def __init__(self,first_name,last_name,salary):         #dunder methods
        
        #instance variable
       self.first = first_name
       self.last = last_name
       self.pay = salary
       self.email = first_name.lower()+ "." +last_name.lower() + "@forsk.in"
      
       #print("inside Employee Constructor")
       Employee.num_of_emps += 1
        

#instance methods
    def fullname (self):
        return self.first + " " + self.last
        
    
    
    


        
    
    
                 
            
          
          
          
          
          
          
          
emp_1 = Employee("Sylvester","Fernandes",50000)  #constructor
#print(emp_1)


emp_2 = Employee("Yogendra","Singh",70000)    #constructor
#print(emp_2)

print(Employee.num_of_emps)


print(emp_1.email)

print(emp_2.email)


print(emp_1.fullname())
print(emp_2.fullname())

#emp_1 and emp_2 are known as reference variable
#emp_1 is pointing towards Sylvester object
#emp_2 is pointing towards Yogendra object

print(Employee.fullname(emp_1))




#Manager Developer

class Developer (Employee):                  #developer - sub class ,, Employee - super class
    pass

class Manager(Employee):
    pass


print(issubclass(Developer, Employee))

print(issubclass(Manager,Employee))

print(issubclass(Employee,Developer))


emp_1 = Employee("Sylvester","Fernandes",50000)
dev_1 = Developer("Sylvester","Fernandes",50000)
mgr_1 = Manager("Sylvester","Fernandes",50000)

print(isinstance(dev_1,Developer))
print(isinstance(emp_1,Employee))
print(isinstance(mgr_1,Manager))

















