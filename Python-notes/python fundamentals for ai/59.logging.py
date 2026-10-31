#logging
'''
In production server,we cant see the print statements.So,with the help of logging,we can log the important info to understand the issues during production.
'''

import logging
#we have to import this built-in module for logging
import os
#we have to import this module to work with file directories.
LOG_DIR="log" #this is our folder name
LOG_FILE_NAME="app.log" #this is our file name which is in. log format.
os.makedirs(LOG_DIR,exist_ok=True)
#this creates directory/folder with the name provided by the param.exist_ok=True is another param used for avoiding error when program is execute multiple times.
log_path=os.path.join(LOG_DIR,LOG_FILE_NAME)
#this creates the path for our log file
logging.basicConfig(
  filename=log_path,
  format="[%(asctime)s] %(name)s-%(levelname)s-%(message)s",
  level=logging.INFO
)
#this creates our log file in the log folder with the specific format
logging.info("hello world")
#logging.info() saved the information in our log file.