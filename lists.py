# Page No - 35,36 (About Lists)
fruit_basket = ['apple','mango','banana','grapes','cherry']
print(fruit_basket[0])

# Page No - 37.38 (About Append,Insert,del in Lists)
fruit_basket.append('papaya')
print(fruit_basket)
fruit_basket.insert(0, 'guava')
print(fruit_basket)
del fruit_basket[2]
print(fruit_basket)

# Page No - 39,40,41 (About pop() and Remove() in Lists)
newlist = ['amit','ajay','prakash','subhi','jaya']
newpoplist = newlist.pop()
print(newpoplist)

newlist.remove('ajay')
print(newlist)

# Page No - 42,43 (Organizing the Lists and using sort() reverse() and len() )
heroes = ['thor','iron-man','hulk','captain america']
heroes.sort()
print(heroes)
heroes.reverse()
print(f'{heroes}')
print(len(heroes))