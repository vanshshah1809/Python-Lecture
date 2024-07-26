import os

files = os.listdir("C:\\Users\\VANSH\\Pictures\\jpeg")

i = 1
for file in files:
   os.rename(f"{file}",f"{i}.jpeg")
   i = i + 1