# Exception Handling


try:
    my_age = int(input("Enter your age>"))
    
except Exception:
    print("Non Integer value, try giving the age again")
    
else:
    print("Your age is:", my_age)
    
finally:
    print("Program ended")