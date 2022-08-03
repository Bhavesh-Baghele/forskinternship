"""
int i = 6 ;
2 bytes are allocated in the stack area
"""

a = 6

print(id(a))   # shows stack address

print(a)


b = 9

print(id(b))

c = 9
print(id(b))


a = 'bhav'
print(type(a))


a = "sneha"
print(type(a))

a = 6
print(type(a))



