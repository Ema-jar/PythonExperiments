import random
from colorama import Fore


def tree_check(tree_height):
    if tree_height < 2:
        print "L'albero deve essere alto almeno 2"
        exit()
    return

def print_tree(tree_height):

    max_tree_width = (tree_height * 2) + 1
    white_spaces = tree_height

    for i in range(0, tree_height):
        stars = max_tree_width - (white_spaces * 2)
        
        print_spaces(white_spaces)
        print_stars(stars)
        print_spaces(white_spaces)
        
        print "\n"
        white_spaces -= 1
    
    return

def print_base(tree_height):
    
    max_tree_width = (tree_height * 2) + 1
    base_width = tree_height / 3
    base_height = 2

    if base_width != 1:
        base_width += 1

    for i in range(0, base_height):

        for j in range(0, (max_tree_width - base_width) / 2):
            print " ",
        for j in range(0, base_width):
            print Fore.YELLOW + "*",
        for j in range(0, (max_tree_width - base_width) / 2):
            print " ",

        print "\n"

    return

def print_spaces(num_of_spaces):
    for j in range (0, num_of_spaces):
        print " ",
    
    return

def print_stars(num_of_stars):
    
    for j in range (0, num_of_stars):
            if(j != 0 and j != num_of_stars - 1):
                print_internal()
            else:
                print_external()
    
    return

def print_internal():
    if (random.randint(0,1)):
        print Fore.RED + "*",
    else:
        print Fore.GREEN + "*",

    return

def print_external():
    print Fore.GREEN + "*",
    prev = "green"
    
    return