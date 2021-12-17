from math import nan
import random

arr = ["red", "blue", "yellow", "green", "purple", "orange", "pink", "maroon"]
#secret_code = random.sample(arr, k=4)
#guess = input("Give 4 colors: ")
#first_try = guess.split(', ')


def user_color():
    guess = input("Give 4 colors: ")
    first_try = guess.split(', ')
    return first_try


user_color()


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def check_list(first_try, secret_code):
    matches = intersection(first_try, secret_code)
    bad_order = len(matches)
    good_color_count = 0
    if matches != []:
        for i in range(0, len(first_try)):
            if first_try[i] == secret_code[i]:
                good_color_count += 1
                bad_order -= 1
    else:
        good_color_count = 0
        bad_order = 0
    return good_color_count, bad_order


def play_turn():
    secret_code = random.sample(arr, k=4)
    first_try = user_color()
    i = 1
    while i < 10:
        i += 1
        if check_list(first_try, secret_code) == (4, 4):
            break
        else:
            user_color()
    return first_try


print(check_list(first_try, secret_code))
