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

# Page No- 99,100 (Looping Through a Dictionary)
for key,value in dict1.items():
    print(f"{key} this is the key and its value is {value}")

# Page No- 100,104 (sorting a list in a loop)
dict2 = {'student1':"aman",'student2':'riya','student3':'kunal','student4':'zoya'}
for value in sorted(dict2.values()):   
    print(f"these are the sorted values of dictionary 2 \n {value}") 

