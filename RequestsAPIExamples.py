import requests
import json

def processAPIBasedRequrest():
    API_KEY="API_KEY" # Go to Settings->> Developers Settings ->> Personal Settings ->> Fine Grained Toekns, 
      #Copy the token and Paste here to access to the GITHUB from your code without login 
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response=requests.get("https://github.com/SridharKammary?tab=repositories",headers==headers)
    responseTextinJson=response.text
    with open("apiBasedResponse.json","w+") as file1:
        json.dump(responseTextinJson,file1,indent=4)
    print("Dumped data to a file successfully!")
def processReqWithParams()->None:
    # Specify query parameters
    params = {'page': 2, 'limit': 5}

    # Make a GET request with query parameters
    #response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
    response = requests.get(url="https://jsonplaceholder.typicode.com/posts",params=params)
    # Print the response content
    #print(response.text)
    responsDict=json.loads(response.text)
    print(responsDict)
    #dump the information to a file
    with open("response.json",mode="w+") as file1:
        json.dump(responsDict,file1,indent=4)
    print("Data dumpued to a file successfully!")

def processRequestWithoutParams():
# Make a GET request to a sample API endpoint
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    # Print the response content
    responseDict=json.loads(response.text)
    print(response.headers)
    print(response.text)
    print(responseDict)
    #response.json
    print(type(response.headers))
    print(response.headers.get("Content-Type"))

#processReqWithParams()
processAPIBasedRequrest()