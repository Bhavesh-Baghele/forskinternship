shopping_list = []

print("Enter the items in the list")
print("Enter DONE once item adding is completed")

while(True):
    new_item = input("Enter the item:")
    if(new_item == 'DONE'):
       break
   
    shopping_list.append(new_item)
    
print("Here is your list items")

for item in shopping_list:
    print(item)
    
    

    
    
    
