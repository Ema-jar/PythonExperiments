from colorama import Fore
import random

treeHeight = input("Quanto deve essere alto l'albero?")

if treeHeight < 2:
    print "L'albero deve essere alto almeno 2"
    exit()

currentWidth = 0
maxTreeWidth = (treeHeight * 2) + 1
whiteSpaces = treeHeight

# print tree
for i in range(0, treeHeight):
    stars = maxTreeWidth - (whiteSpaces * 2)
    prev = "green"
    
    for j in range (0, whiteSpaces):
        print " ",
    for j in range (0, stars):
        if(j != 0 and j != stars - 1):
            if (random.randint(0,1) and prev != "red"):
                print Fore.RED + "*",
                prev = "red"
            else:
                print Fore.GREEN + "*",
                prev = "green"
        else:
            print Fore.GREEN + "*",
            prev = "green"
    for j in range (0, whiteSpaces):
        print " ",
    
    print "\n"
    whiteSpaces -= 1

# print base
baseWidth = treeHeight / 3
if baseWidth != 1:
    baseWidth += 1

baseHeight = 2
whiteSpaces = treeHeight

for i in range(0, baseHeight):

    for j in range(0, (maxTreeWidth - baseWidth) / 2):
        print " ",
    for j in range(0, baseWidth):
        print Fore.YELLOW + "*",
    for j in range(0, (maxTreeWidth - baseWidth) / 2):
        print " ",

    print "\n"

