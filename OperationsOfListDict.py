import json
#Dictionary Operations
dict1=dict()#create dictionary

dict1["name"]="sridhar" # assign key and value
dict1["age"]=43
dict1["addr"]="hyd"

print(dict1)
print(f"JSON String={json.dumps(dict1)}")
print(f"{dict1.fromkeys(dict1.items())}")#Understand this

print(f"Length of the dict = {len(dict1)}")

list1=list([])
list1.append(34)
list1.append(23)
list1.append(100)
list1.append(1)
print(list1)# Order is presevered
list1.sort(reverse=False)
print(list1)

set1=set({1,2,3,4})#set edclartions
#set1={}
fz=frozenset(set1) #You cannot add any elements to frozenset
print(f" {set1} and {fz}")
