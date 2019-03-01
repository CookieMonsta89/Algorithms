#!/usr/bin/python

import math
import operator

def recipe_batches(recipe, ingredients):
  # Need to get the max value from ingredients.items, this is a starting point
  batch = max(ingredients.items(), key=operator.itemgetter(1))[1]
  # Now I need to loop 
  for recKey in recipe.items():
    # if the key from recipes does not appear in ingredients, batch=0 because we can't make recipe
    if recKey[0] not in ingredients.keys():
      batch = 0
    # loop through the ingredients dict
    for ingKey in ingredients.items():
      # if the key of ingredients matches the key of the recipe
      if ingKey[0] == recKey[0]:
        # checking that we have more in ingrediants than the recipe calls for
        if (ingKey[1] // recKey[1]) < batch:
          # if it is lower, then we decrease the total number of batches we can make to this new total
          batch = (ingKey[1] // recKey[1])
  # return total number of batches we can make
  return batch

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))