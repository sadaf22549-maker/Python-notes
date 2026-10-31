#Accessing data from external server

import requests
url="https://jsonplaceholder.typicode.com/posts/1"
response=requests.get(url)
data=response.json()
#Now we can access any kind of data by using data variable.
print(data)
print("\n")
print(f"{data["title"]},\n{data["userId"]}")
 #think about data which has a dictionary with a "title" & "userId" key.
