# Page No - 76,77,78 (If Statements)
lists = [1 , 3, 3 ,5, 6, 7, 8, 9,2, 5,3 ,4 ,22]
count = 0
for numbers in lists:
    if numbers%2 ==0:
        print(f"numbers are even {numbers}")
        count += 1
        print(f"numbers that are even {count}")

# Page No - 79 (if else statements)
age = int(input())
if age < 18:
    print("you are not adult enough to see this movie!!")
else:
    print("you are adult enough to see this movie")

# Page No - 80 - 87 (about using if statements in a lists)
available_pizza = ['cheeze pizza','macaroni pizza','tomato pizza','onion pizza','garlic pizza','capcicum pizza']   

notavailable_pizza = ['hot pizza','xyz pizza','mickey piza','kids pizza','pizza-pizza']

s = input("please type what type of pizza you want??")

for pizzas in available_pizza:
    if s in available_pizza:
        print(f"ordering {s} , order would be ready in two minutes")
        break
    if s in notavailable_pizza:
        print(f"sorry!! {s} not currently available")
        break
    else:
        print(f"get out of store!!")
print("thanks for choosing dash pizzas")            