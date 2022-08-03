order = [34587,'Learning Python','Mark Lutz',4,40.95],
[98762,'Programming Python','Mark Lutz',5,56.80],
[77726,'Head First Python','Paul Barry',3,32.95],
[88112,'Einfuhrung in Python3','Bernd Klein',3,24.99]

lists = []
for item in order:
    if item[-1]*item[-2] < 100:
        lists.append((item[0],item[-1]*item[-2]+10))
    else:
        lists.append((item[0],item[-1]*item[-2]))



print("Order Summary:",lists)



