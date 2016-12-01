#My solution for the problem given to us for class
import numpy as np

#Reads the text file and splits the list based upon white space
with open("COSC450_P2_Data.txt", "r") as myFile:
    lines = myFile.read().split()

#Rids of the white space in thel ist
lines = list(filter(None, lines))

#Gets rid of the newline and tab characters in the list
lines = [each.replace('\n', '') for each in lines]
lines = [each.replace('\t', '') for each in lines]

#Used to create 2D list
index = int(len(lines) / 5)
temp = 5

for x in range(len(lines)):
    lines[x] = float(lines[x])

a = (np.array(lines).reshape(index, temp))
b = (np.array(lines).reshape(temp, index))

c = a * np.transpose(b)

#Creates a list containing 5 lists, with 30 items each
#tempMatrix1 = [[0 for x in range(index)] for y in range(temp)]
#tempVar1 = 0

#Loops through list adding correct item
#for x in range(temp):
 #   for y in range(index):
  #      tempMatrix1[x][y] = lines[tempVar1]
   #     tempVar1 = tempVar1 + 1

#Creates a list containing 30 lists, with 5 items each

#tempMatrix2 = [[0 for x in range(temp)] for y in range(index)]
#tempVar2 = 0

#Loops through list adding correct item
#for x in range(index):
 #   for y in range(temp):
  #      tempMatrix2[x][y] = lines[tempVar2]
   #     tempVar2 = tempVar2 + 1

print(c)

#Checking lists for correct length
#print(len(tempMatrix1))
#print(len(tempMatrix2))

