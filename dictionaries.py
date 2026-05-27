# Page No-92 (About Dicitonaries)
dict1 = {'hero1' : 'thor', 'ranking' : 1, 'enemy' : 'hulk'}
print(dict1['hero1'])
print(dict1['ranking'])

# Page No-97,98 (More on dictionaries using get() and del )
dict1["power_level"] = 'S-Class'
dict1["level"] = 1
level_up =int(input("type how many levels thor has leveled up??"))
if level_up ==1:
    dict1["power_level"] = 'S+ Class'
    print(dict1)
if level_up ==2:
    dict1['power_level'] = 'S++ Class'
    print(dict1) 
else:
    dict1['power_level'] = 'S-Class'
    print(dict1)

del(dict1['ranking'])
print(dict1)
print(dict1.get("xyz key"))

