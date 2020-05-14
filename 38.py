dict1 ={'Name':'Ramakrishna','Age':25}
dict2={'EmpId':1234,'Salary':5000}

dict1.update(dict2)

dict1["Salary"] += 500
print(dict1)

dict1["Age"] += 1
print(dict1)

dict1.update({'grade':'B1'})

for keys,values in dict1.items():
  print(keys,values)

dict1.pop("Age")

print(dict1)