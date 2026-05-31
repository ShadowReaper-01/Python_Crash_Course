# Page No - 10 (Basic Introduction about printing Hello Python World Command)
print("Hello Python World")

# Page no - 16 (Using variables and printing a message)
message = "my name is sparsh"
print(message)

# Page No - 20 (About string and String Methods operation)
name = 'sparsh'
print(name.title())
print(name.lower())
print(name.upper())

# Page No - 21 (Using Variables as Strings and f Function)
firstname = 'sparsh'
lastname = 'gautam'
print(f"{firstname} {lastname}")

# Page No - 21,22 (Using whitespaces and learning how to strip string)
para = '  My name is sparsh gautam \n and i belong to sagar \t madhya pradesh  '
paraLstrip = para.lstrip()
paraRstrip = para.rstrip()
print(para)
print(paraLstrip)
print(paraRstrip)

# Page No - 24 (using removeprefix() and removesuffix())
url = 'https://google.com'
urlRP = url.removeprefix('https://')
urlRS = url.removesuffix('google.com')
print(url , urlRP , urlRS)

# Page No - 27,28 (About Numbers Integers And Floats and Constants)
num = 1
float = 2.0
y = float / num
THISISACONSTANT = 12
print(type(num), type(float), type(y))
