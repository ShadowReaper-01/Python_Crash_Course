# Page No-122,123,124 (While Loop in Lists)
s = input("Enter your name!! ")
lists = ['kunal', 'riya', 'karana', 'arjun']
confirmedlists = []

# Loop until 'lists' is completely empty
while lists:
    newlist = lists.pop()
    confirmedlists.append(newlist)

# Check if the entered name was one of the elements
if s in confirmedlists:
    print("your name has been confirmed")

print(confirmedlists)
