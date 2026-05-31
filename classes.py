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