#Uncommenter by Zylops
#A simple script that removes all comments from your code.

filepath = input("Enter the path to your file: ")
filename = input("Enter your filename: ")

actualpath = filepath + "\\" + filename

thingsToWrite = []

tags = ['#', '//', '/*', '<!–', '*']

nameSplit = filename.split('.')

extention = nameSplit[1]

theFile = open(actualpath, 'r')
filewrite = open(filepath + '\\' + nameSplit[0] + '-uncommented.' + extention, 'a')

for line in theFile:
    for i in tags:
        if line.startswith(i):
            pass
        else:
             thingsToWrite.append(line)


for i in thingsToWrite:
    filewrite.write(i)

print("File succesfully uncommented =)")
input()