#Page No-114,115,116,117 (About using Input Function)
user_input = int(input("enter your number = "))

if user_input %10 ==0:
    print("numbers is divisible by 10!!")

else:
    print("number is not divisible by 10!!") 

# Page no - 118,119 (Inroduction to While Loops)
number = 2
while number < 20:
    number += 1
    print(number)

message = input("Who is your favourite superhero?")

while message != 'quit':
    print(f"{message}, that is also mine favourite superhero!!")

# Page No - 120 (using Flags In While Loop)
new_message = input("What do you like pizza or burger??")
flag = True

while True:
    print(f"{new_message} i love it too")
    break

# Page No-121 (Using Break In A While Loop)
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

