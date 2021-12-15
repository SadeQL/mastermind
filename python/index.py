# mastermind starts here
import random

arr = ["red", "blue", "yellow", "green", "purple", "orange", "pink", "maroon"]
secret_code = random.choices(arr, k=4)

guess = [input("Give 4 colors: ")]

for elem in guess:
    first_try = elem.split(", ")


# def master_mind():
