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