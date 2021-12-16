# mastermind starts here


import numpy as np

import random

from numpy.lib.shape_base import split

arr = ["red", "blue", "yellow", "green", "purple", "orange", "pink", "maroon"]
secret_code = random.choices(arr, k=4)

guess = [input("Give 4 colors: ")]

first_try = []

#def returnMatches(lst1,lst2):
       #return list(set(lst1) & set(lst2))
       
def Intersection(lst1, lst2):
    return list(set(lst1).intersection(lst2))



def check_turn(turn):
    for elem in guess:
       elem.split(', ')
    return turn.append(elem.split(', '))


check_turn(first_try)

set1 = set(secret_code)
set2 = set(first_try)

set3 = set1 & set2
list3 = list(set3)




print(secret_code)
print(first_try)
#print(list(set(secret_code) & set(first_try)))
#print(secret_code.intersection(first_try))
print(list3)

#def check_color():






