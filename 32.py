lst1 = ["tokyo","berlin","delhi","goa","paris"]
lst2 = ["denver","rio","munich","madrid","lyon"]
lst3 = ["nantes","palermo","bogota","turin","sofia"]

for i in lst1:
    print(len(i),i)

print("\n")

for i in lst2:
    print(len(i),i)
print("\n")

for i in lst3:
    print(len(i),i)
print("\n")


print(min(len(i) for i in lst1),max(len(i) for i in lst1)) 
print(min(len(i) for i in lst2),max(len(i) for i in lst2)) 
print(min(len(i) for i in lst2),max(len(i) for i in lst2)) 

print("\n")

print(max(max(len(i) for i in lst1),max(max(len(i) for i in lst1),max(len(i) for i in lst2))))
print(min(min(len(i) for i in lst1),min(min(len(i) for i in lst1),min(len(i) for i in lst2))))

print("\n")

lst1.pop()
lst1.pop(0)
print(lst1)

lst2.pop()
lst2.pop(0)
print(lst2)

lst3.pop()
lst3.pop(0)
print(lst3)