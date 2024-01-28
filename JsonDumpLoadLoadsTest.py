import json
import os
#Dump and Load Test
# json.dump() will be used to dump the dictionary content to the file
#json.load() will be used the content from the json file to dictionary
def jsonDumpAndLoadTest():
    dict1=dict()
    dict1["name"]="Sridhar"
    dict1["addr"]="hyd"
    #Write the dictionary to file
    try:
        with open("resources\file1.json","w+") as file1:
            json.dump(dict1,file1,indent=4)
    except:
        print("Error")
    finally: 
        if(file1!=None):    
            file1.close()
            print("file is closed successfull!")
    #Load the data from file to dictionary
    try:
        with open("resources\file1.json","r") as file1:
            dic= json.load(file1)
            print(f"{type(dic)}  Matter is:  {dic}")
        
    except:
        print("Loading Error")
    finally:
        if(file1!=None):
            file1.close()
            print("File is closed succssfully!")
#json.dumps() will be used to convert the dictionary obj to json string
#json.loads() will be used to convert the jsonString to Dictionary object
def jsonDumpsAndLoadsTest():
    dict1=dict()
    dict1["name"]="Sridhar"
    dict1["addr"]="hyd"
    jsonString=json.dumps(dict1)
    print(f"JSOn String= {jsonString}")

    #converth the JSOn string to Dictionary
    dic=json.loads(jsonString)
    print(f" Type of dic is : {type(dic)} and dic= {dic}")

jsonDumpsAndLoadsTest()


                
