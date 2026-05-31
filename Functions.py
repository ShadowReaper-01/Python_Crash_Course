# Page No - 129,130 (About functions)
def sum():
    x = int(input("Enter A Number X:"))
    y = int(input("Enter A NUmber Y:"))
    
    z = x + y
    print(z)
sum() 

# Page No - 131,132 (functions call)
def greet(hero,heroclass):
    print(f"{hero},that is your favourite superhero? you have a good taste")
    print(f"{heroclass}, that is a superb class")

greet('garou','S')
greet("saitama","B")

# Page No-133,134,135,136,137,138 (About Return Function)
def devisibleby2():
    number = int(input("Please Enter Your Number"))
    if number % 2 ==0:
        return "Even"
    else:
        return "Odd"
print(devisibleby2())

# Page No - 140,141 (About Using While Loops In A Function)
def name(firstname,lastname):
    while True:
        if firstname != 'q':
            print(f"{firstname} its a beautiful firstname ")

        if lastname != 'q':
            print(f"{lastname}  its a beautiful lastname")
        break        

name('anuj','kothari')                



