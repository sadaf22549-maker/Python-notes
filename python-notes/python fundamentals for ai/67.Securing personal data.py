#Securing personal data

'''we have to create 2 files in our project folder.   1).env -->here we store our personal data like api,database etc.
2).gitignore -->here we have to tell to ignore. env so that it doesnt track. env file when uploading our code to github.
'''
#we have to install a third-party package named dotenv

from dotenv import load_dotenv
import os
load_dotenv()
#load_dotenv() -->it loads all the environment variables written in. env file.

api_key=os.getenv("environment_variable")
#.getenv() -->it will get the environment_variable passed as a param from the. env file.

#Now we can easily use our personal data without showing it to others.





'''if it doesnt work then we have to write these 2 lines-

env_path=path(__file__).resolve().parent/".env"
load_dotenv(dotenv_path=env_path,override=True)

path(__file__) -->the path of main file
.resolve() -->selects as an absolute
.parent() -->removes the name of main file from                     the path
/".env" -->adds. env with the path

So,it will become our env_path.we can pass it as a param so load_dotenv can understand from where it has to load the environment variables.
'''



 