#Dictionary methods
#for getting all the keys-.keys()

D={"Outfit":"Shoe","brand":"Nike","price":6000}
print(D.keys()) #dict_keys([outfit,brand,price])

#for getting all the values-.values()
print(D.values()) #dict_values([shoe,Nike,6000])

#for getting all the key-value pairs-.items()
print(D.items()) #dict_items([(outfit,shoe),(brand,Nike),(price,6000)])

#for removing items-.pop(),.clear()
D.pop("brand")
print(D) #{outfit:shoe,price:6000}
D.clear()
print(D) #{ }

#for updating items-.update()
D={"Outfit":"Shoe","brand":"Nike","price":6000}
D.update({"gurantee":"2 years","Quality":"moderate"})
print(D)  #{"Outfit":"Shoe","brand":"Nike","price":6000,"gurantee":"2 years","Quality":"moderate"}