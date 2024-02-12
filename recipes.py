import json
import random

with open('data.json', 'r') as file:
    recipes = json.load(file)

def RandomRecipe():

    recipe = random.choice(recipes)

    return recipe

def PrintRecipe(recipe):

    print("Name:", recipe["name"])
    print("Time:", recipe["time"], "minutes")
    print("Diet:", recipe["diet"])
    print("Details:", recipe["details"])

def AddNewRecipe(name,time,diet,details):
    new_recipe = {
        "name": name,
        "time": time,
        "diet": diet,
        "details": details
    }
    recipes.append(new_recipe)

    with open('data.json', 'w') as file:
        json.dump(recipes,file,indent=2)

def MatchingRecipe(diet):
    matching_recipes = [recipe for recipe in recipes if recipe["diet"] == diet]
    return matching_recipes


print("Welcome to Today's recipe!")
while True:
    print("Current features: ")
    print("\n")
    print("1. Share your favorite recipe with others!")
    print("2. Don't know what to cook? Get one random recipe from our database! ")
    print("3. Look up a recipe by your dietary restrictions!")
    print("\n")

    user_input = input("Enter the corresponding number to select of the above options(or 'exit' to exit the program at any time): " )
   
    if user_input == "1":
        name = input("Enter the name of the recipe that you want to share: ")
        time = input("Enter the how long it'd cost to make this recipe(in the unit of minutes): ")
        print("'V': vegetarian, 'VG': vegan, 'H': halal, 'K': kosher, 'GF': gluten free, 'DF': dairy free")
        diet = input("Enter the dietary restriction (abbreviation) this recipe satisfies: ")
        details = input("Enter the full recipe: ")
        print("\n")
        AddNewRecipe(name,time,diet,details)
        user_input = input("Thanks for sharing! Enter 'menu' to go back to manu or 'exit' to quit the program: ")
        if user_input.lower() == "exit":
            break  

    elif user_input == "2":
        PrintRecipe(RandomRecipe())

        user_input = input("There's one random recipe. Enter 'menu' to go back to manu or 'exit' to quit the program: ")
        if user_input.lower() == "exit":
            break  

    elif user_input == "3":
        diet_search = input("What's your dietary restriction? ")
        match = MatchingRecipe(diet_search)
        if match:
            random_recipe = random.choice(match)
            PrintRecipe(random_recipe)
        
        user_input = input("There's one recipe that meets the requirment. Enter 'menu' to go back to manu or 'exit' to quit the program: ")

        if user_input.lower() == "exit":
            break 

    elif user_input.lower() == "exit":
        break

