

treeHeight = input("Quanto deve essere alto l'albero?")

if treeHeight < 1:
    print "L'albero deve essere alto almeno 1"
    exit()

currentWidth = 0
maxWidth = (treeHeight * 2) + 1
whiteSpaces = treeHeight

for i in range(0, treeHeight):
    stars = maxWidth - (whiteSpaces * 2)

    for j in range (0, whiteSpaces):
        print " ",
    for j in range (0, stars):
        print "*",
    for j in range (0, whiteSpaces):
        print " ",
    
    print "\n"
    whiteSpaces -= 1




