"""
list1 = [1,2,3,4,5]

#[1,4,9,16,25]

list2 = []

for item in list1:
    list2.append(item*item)
    
print(list2)

#shortcut 
#list comprehension
#  **  means power

[item**3 for item in list1]
print([item*item for item in list1])

list1 = ["Amar","Akbar","Anthony"]
#length of each words in a list
#[4,5,7]
print([len(item) for item in list1])

"""

list1 = [10,20,30,40]

#[100,400,900,1600]
def squarevalue(x):
    return(x*x)

print(list(map(squarevalue,list1)))



list1 = [1,2,3,4,5]

"""
def iseven(x):
    if(x%2 == 0):
        return True
    else:
        return False
    """
    
    
    
    #OR
    
list1 = [1,2,3,4,5]
def iseven(x):
    return(x%2 == 0)
    
# % means divide
    
print(list(map(iseven,list1)))

for item in list1:
    print(iseven(item))
 
    """
import math
dir(math)    
help(iseven)
"""
print(list(filter(iseven,list1)))

# use of lamda

print   (list(map(lambda x:x % 2 == 0,list1)))

print(list(filter(lambda x:x % 2 == 0,list1)))


list1 = [1,2,3,4,5]

def fadd(x,y):
    return(x+y)
    return(x+y)

import functools

print  (functools.reduce(fadd, [1,2,3,4,5]))

"""
iter1: fadd(1,2) -> 3
iter2: fadd(3,3) -> 6
iter3: fadd(6,4) -> 10
iter4: fadd(10,5) -> 15
"""


def fadd(x,y):
    return(x*y)
    

import functools

print  (functools.reduce(fadd, [1,2,3,4,5]))


print  (functools.reduce(lambda x,y: x*y, [1,2,3,4,5]))

