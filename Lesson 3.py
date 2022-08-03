list1 = [1,2,3,4,5,6,7]

type(list1)

dir(list)
help(list.append)

list1.append(100)

list1[0]

list1[-1]

list1[0] = 11
#list can be modified
#list are mutable

#[11,22, 2, 3, 4, 5, 6, 7, 100]

list1.insert(1,22)

list1.remove(5)

list1 = [10,5,2,5,6,20]

list1.count(5)

list1.remove(5)
list1.remove(5)

list1 = [10,5,2,5,6,20]

while(5 in list1):
    list1.remove(5)
    
    
list1 = ['Amar','Akbar','Anthony']    

list1[0]
list1[1]
list1[2]

list1 = ['Amar','Akbar','Anthony']    

for name in list1:
    print(name)
    
for x in list1:
    print(x)
    
list1 = [1,2,3,4,5]
list2 = []

for item in list1:
    list2.append(item*item)
    
#[1, 4, 9, 16, 25]

#list comprehension
[item*item for item in list1]

list1 = ['Amar','Akbar','Anthony']

list2 = []

for item in list1:
    list2.append(len(item))
    
[len(item) for item in list1]

list3 = [len(item) for item in list1]

"""
Name - Krish
class - 9
ssc - 89
Math - 78

"""

student = {
    'name': 'Krish',
    'class': 9,
    'ssc':89,
    'math':78
    
    }

student['ssc']

student['name'] = 'Krish Sharma'

student['city'] = 'Agra'


#Version 4


datastore = {}
import math

while(True):
    X = input("Enter the number:")
    
    #check if X is blank
    if (not X):
        print("Invalid input.. try next")
        break
        
    if (X.isdigit()):
        
        X = int(X)
        datastore[X] = math.sqrt(X)
    else:
        datastore[X] = (len(X))
        
print(datastore)
   





    
    
    
    
    


    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    