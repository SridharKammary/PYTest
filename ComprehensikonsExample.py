
#Dictionary Comprension example:
class Person():
    def __init__(self) -> None:
        ...
def dictionaryComprehension():
    list1=[2,3,48,9,0,4,6]
    list2=['a','b','c','d','e','f','g']
    dic={k:v for (k,v) in zip(list2,list1)}
    print(dic)
    print(zip(list2,list1))

#List comprehension
def listCompreHensionExample():
    list1=[2,3,48,9,0,4,6]
    evenList=[x for x in list1 if x%2==0]
    print(f"Normal List={list1} and Even List={evenList}")
    #Prepare the 2D Matrix

    twoDMatrix=[ [x for x in range(2)] for k in list1 ]
    print(f"2D Matrix = {twoDMatrix}")

dictionaryComprehension()