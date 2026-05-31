# Page No - 159,160,161 (defining a class and __init__() method)
class hero:

    def __init__(self,name,Hero_class):
        self.name = name
        self.Hero_class = Hero_class

    def power(self):
        return f"{self.name} is a great superhero!!" 

    def classes(self):
        return f"{self.Hero_class} is an awesome hero-class"

hero1 = hero('Saitama','B-Class')
hero2 = hero("Goku","S-Class")

print(hero1)
print(hero2)
print(hero1.name)
print(hero2.Hero_class)

# Page No-179 (About Python Libraries)
from random import randint as ri
from random import choice as ch
print(ri(1,100))
characters = ['amit','queen','king','subaru','goku','saitama']
print(ch(characters))