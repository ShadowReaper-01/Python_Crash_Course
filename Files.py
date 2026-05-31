with open(r"C:\Users\gauta\Desktop\pivalue.txt", "r",encoding = 'utf-8') as file:
    content = file.read()
    
    print(content)

    lines = content.splitlines()
    print(lines)
    print(len(content))


try:
    print(5/0)
    pass

except:
    print("man! you cant devide by 0!!")

from pathlib import Path

desktop = Path.home() / "Desktop"

file_path = desktop / "notes.txt"

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)            
 
   