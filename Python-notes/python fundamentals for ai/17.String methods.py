#String methods
'''for case manipulation-
.capitalize(),.upper(),.lower()'''

str="i want TO learn"
print(str.capitalize()) #I want to learn
print(str.upper()) #I WANT TO LEARN
print(str.lower()) #i want to learn

'''for searching-
.count(),.find()
.count("char") returns the occurances of specific character or word
.find("char") returns the index of the 1st occurance of specific character or word'''

print(str.count('a')) #2
print(str.find('n')) #4

'''for start & end validation-
.startswith(),.endswith()
both of them return True or False'''

print(str.startswith("i want")) #True
print(str.endswith("mn")) #False

'''for character validation-
.isalnum(),.isalpha(),.isdigit()
all of them return True or False'''

new_str="abc123"
print(new_str.isalnum()) #True
print(new_str.isalpha()) #False
print(new_str.isdigit()) #False

'''for splitting & joining-
.split()," ".join()'''

splitting=str.split()
print(splitting) #['i','want','TO','learn']
joining=" ".join(splitting)
print(joining) #i want TO learn

'''for Replacing & stripping-
.replace(),.strip()
.replace("old","new") it replaces the old char or words with the new one.
.strip() it removes all the extra whitespaces'''

print(str.replace("learn","teach")) #i want TO teach
print(str.strip()) #i want TO learn

