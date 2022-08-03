

"""
#File Handling
1. Reading the data from the file
2. Writing the data to file
"""

#Read the fruit name from file

fp = open("Fruits.txt","r")
print (fp.read())
fp.close()

fp.read()


fp = open("Fruits.txt","r")
print (fp.readline())
print (fp.readline())
print (fp.readline())
fp.close()


fp = open("Fruits.txt","r")
print (fp.readlines())
fp.close()

#Write the Data to file

fp = open("Forsk.txt","w")
print (fp.write("Sylvester Fernandes"))
fp.close()



