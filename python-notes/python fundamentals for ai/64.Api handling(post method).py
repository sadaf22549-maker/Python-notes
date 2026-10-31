#post method

import requests
data={"name":"Alif","userId":2}
url="https://jsonplaceholder.typicode.com/posts"
response=requests.post(url,json=data)
#.post() -->it sends specific data to the external server.
#json=data -->it converts python data types to json format.

print(response.status_code)
print(response.json())