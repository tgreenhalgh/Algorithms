#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    count = 0
    check = True

    for key in recipe:
        if key not in ingredients:
            return 0

    while check:
        keys = 0
        for key in recipe:
            keys += 1
            if (check and recipe[key] * (count + 1)) <= ingredients[key]:
                check = True
            else:
                check = False
                break
            if check and keys == len(recipe):
                count += 1

    if count:
        return count
    else:
        return 0


if __name__ == '__main__':
            # Change the entries of these dictionaries to test
            # your implementation with different inputs
    # recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    # ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    recipe = {'milk': 2, 'sugar': 40, 'butter': 20}
    ingredients = {'milk': 5, 'sugar': 120, 'butter': 500}

    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
