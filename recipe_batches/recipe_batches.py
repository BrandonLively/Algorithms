#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    recipe_name_list = list(recipe.keys())
    has_ingredients = True
    ingredient_values = []
    counter = -1
    while has_ingredients == True:
        counter += 1
        for i in range(len(recipe)):
            try:
                ingredient_values.append(ingredients[recipe_name_list[i]])
            except:
                has_ingredients = False
        if len(recipe) > len(ingredient_values):
            has_ingredients = False
        for j in range(len(recipe)):
            try:
                ingredient_values[j] -= recipe[recipe_name_list[j]]
            except:
                has_ingredients = False
            try:
                if ingredient_values[j] < 0:
                    has_ingredients = False
            except:
                has_ingredients = False
    return counter


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
