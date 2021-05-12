#Uncommenter by Zylops
#A simple script that removes all comments from your code.

#Collect User Input
filepath = input("Enter the path to your file: ")
filename = input("Enter your filename: ")

#Define path to output and input file
actualpath = filepath + "\\" + filename

#List that non comment lines are appended to
thingsToWrite = []

#A list of comment tags from different languages
tags = ['#', '//', '/*', '<!–', '*']

#Splits file name into name and extention
nameSplit = filename.split('.')

#Defines the extention variable
extention = nameSplit[1]

#Loads the file in read mode and creates output file
theFile = open(actualpath, 'r')
filewrite = open(filepath + '\\' + nameSplit[0] + '-uncommented.' + extention, 'a')

#Loops through each line of the file and appends it to thingsToWrite if it isnt a comment
for line in theFile:
    #loops through all tags
    for i in tags:
        #Checks if a line in the file starts with a comment tag
        if line.startswith(i):
            #If it does, don't add it to the list of non comments
            pass
        else:
            #Add it to the list of non comments
             thingsToWrite.append(line)


#Loops through list of non comments and writes them to output file
for i in thingsToWrite:
    filewrite.write(i)

#Prints a successfull message and waits for user input before closing.
print("File succesfully uncommented =)")
input()