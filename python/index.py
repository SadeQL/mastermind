# mastermind starts here

import numpy as np

import random

arr = ["red", "blue", "yellow", "green", "purple", "orange", "pink", "maroon"]
secret_code = random.choices(arr, k=4)

guess = [input("Give 4 colors: ")]


def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)

    
def check_turn():
    for elem in guess:
        first_try = elem.split(", ")
        print(secret_code)
        print(first_try)
        print(Intersection(secret_code, first_try))


check_turn()




