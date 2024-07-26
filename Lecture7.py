#           FILE INPUT\OUTPUT
'''
-> TYPES OF FILES :
1) TEXT FILES   - .txt, .docx, .log, etc.
2) BINARY FILES - .MP4, .MOV, .PNG, .JPEG, etc.
'''

# READING FILES
f = open("lecture7.txt","r")
print(f.read())
#print(f.readline())
#print(f.readline())
f.close()

#WRITING FILES
f = open("lecture7.txt","w")
f.write("First Line")
f.close()



f = open("Lecture7.txt","a")
f.write("\nSecond Line")
f.close()


f = open("Lecture7.txt","r")
print(f.read())
f.close()