def add1(**keys):
   total=0
   for k,v in keys.items():
      total=total+v
   return total

def add2(*list1):
   total=0
   print(type(list1))
   for k in list1:
      #print(type(k))
      total=total+k 
   return total
 
c=add1(a=2,b=3,c=5,d=6)
print(c)


print(add2(1,2,3,4,5,6,7,9))