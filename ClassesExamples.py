import json
import os
from configparser import ConfigParser

class Utils:
 
 def __init__(self) -> None:     
     config=ConfigParser()
     list1=config.read("resources\projectproperties.ini")
     print(config.getint("Database","port"))
class Person:
    def __init__(self,name) -> None:
        self.name=name+"ABC"
    def __str__(self) -> str:
        return (self.name)
    
    @staticmethod
    def getBehviour()->str:
        return "I am good"
    
class Test(Person):
    def __init__(self, name) -> None:
        super().__init__(name) 
        self.name=name
    
    def __str__(self) -> str:
        return super().__str__()
#Observe below from Line#22 to 26
p= Test("Sridhar1") 
print(p)# Test, __str__ is returning super class's return value only, but we "Sridhar1" is result
p= Person("Sridhar1")
print(p)# Person, __str__ returns Sridhar1ABC
print(p.getBehviour())


utils=Utils()
