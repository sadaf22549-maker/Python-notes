#put

import requests
data={"name":"Alif","userId":2}
url="https://jsonplaceholder.typicode.com/posts/1"
response=requests.put(url,json=data)
#.put() -->it will completely overwrite the data.
print(response.json())
print("\n")
#patch

data={"name":"Abrar","userId":2,"title":"hello"}
response=requests.patch(url,json=data)
#.patch -->it will update the data partially.
print(response.json())
print("\n")
#delete

response=requests.delete(url)
#it will deletes the data
print(response.status_code)