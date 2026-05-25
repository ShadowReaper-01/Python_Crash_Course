# Page No - 50,51 (about for loops)
theboyz = ['homelander','stormfront','billy butcher','hughie','ryan','starlight']

for heroes in theboyz:
    print(heroes)

# Page No - 52 - 59 (about Range Function and min , max, sum)
for value in range(0,7):
    square = value ** 2
    print(square)

lists = [1,3,5,7,4,7,8,3,6,3,6.10]     
print(min(lists))
print(max(lists))
print(sum(lists))  

# Page no - 60 - 65 (about list comprehension and lists slicing)
newlist = ['apple', 'mango','banana','grapes','cherry']
fruits = [fruit for fruit in newlist]
print(fruits)
print(newlist[0:5])
print(newlist[-1:-3])

# Page No - 66,67 (about tuples)

tuple = (39 , 40 , 41)
print(tuple)
tuple = (43,43,45)
print(tuple)