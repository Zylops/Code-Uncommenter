#Uncommenter by Zylops
#A simple script that removes all comments from your code.

filepath = input("Enter the path to your file: ")
filename = input("Enter your filename: ")

actualpath = filepath + "\\" + filename

thingsToWrite = []

theFile = open(actualpath, 'r')
filewrite = open(filepath + '\\' + 'uncommented-version.txt', 'a')

for line in theFile:
    if line.startswith('#'):
        pass
    else:
        thingsToWrite.append(line)

for i in thingsToWrite:
    filewrite.write(i)

print("File succesfully uncommented =)")
input()