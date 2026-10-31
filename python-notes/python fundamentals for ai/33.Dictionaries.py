#Dictionary
''''Dictionary is mutable data type.it can contain
Key:value pairs.it doesnt allow duplicate keys whether it can overwrite the value of key'''

D={ } #Empty dictionary

D={
       "name":"Adil",
       "mark":68,
       "grade":"B"
} #1D dictionary

D={
       "name":"Rashid",
       "roll":43,
       "subjects":{
                           "math":68,
                           "phy":79,
                           "CSE":92
       },
       "grade":"B"
} #2D dictionary

'''We can access the values with the help of keys in a dictionary.
Variable_name["key"] '''

D={
       "name":"Adil",
       "mark":68,
       "grade":"B"
}
D["name"]="Majid"
print(D) #it will overwrite the value of name 
print(D["grade"]) #B
D["position"]=10 #it will add this new key-value pair in the existing dictionary.
print(D)

D={
       "name":"Rashid",
       "roll":43,
       "subjects":{
                           "math":68,
                           "phy":79,
                           "CSE":92
       },
       "grade":"B"
}

D["subjects"]["phy"]=82 #it will change the value of phy
D["subjects"]["Chem"]=57 #it will add a new key-value pair in inner dictionary
print(D)

