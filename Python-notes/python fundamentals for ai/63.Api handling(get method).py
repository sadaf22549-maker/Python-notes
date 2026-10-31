#Api handling

#we need a library called requests for Api handling
import requests
url="https://jsonplaceholder.typicode.com/posts/1"
response=requests.get(url)
'''requests has different http methods like-           1)get 
2)post
3)put
4)patch
5)delete

.get() -->it gets the response after sending a request to the given url.'''

print(response.status_code) #it prints the status code.
'''status code:200 -->gets the response successfully.
status code:404 -->having an error
'''
print(response.json()) 
#.json() -->converts json data to python data types
#response.json() -->converts response's json to python data types.

#filtering data
#params={"user id":2}
#response=requests.get(url,params) #we can use an extra parameter for filter out important data.In this case,It fetchs the data related with params.

#print(response.status_code)
#print(response.json())