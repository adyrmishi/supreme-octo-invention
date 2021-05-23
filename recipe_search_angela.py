import requests
import json

def recipe_search():

    # This part of the code works to filter on diet_type if desired.
    health_filters = ['vegan','vegetarian','red-meat-free','pork-free','peanut-free','kosher','gluten-free','alcohol-free','egg-free','dairy-free']

    all_health_filters = '\n- '.join(health_filters)

    has_diet = input('Do you follow any specific diet? (Y/N) ')

    if has_diet.lower() == 'y':
        diet_type = input(f'What type of diet do you follow from the following: \n- {all_health_filters}? \n')
        # This loop means the user cannot continue without entering an option from the list.
        while diet_type not in health_filters:
            diet_type = input(f'{diet_type} is not a valid option, please choose from: \n- {all_health_filters} \n')
        else:
            print(f'{diet_type} is your chosen diet.')
    else:
        diet_type = False
        print('You have no dietary requests.')

    #     This creates a string to add to the url if a diet type is specified, but allows for a diet type not to be chosen and for the URL to work.
    diet_url_string = f"&dietType={diet_type}" if diet_type is not False else ""

    # This part of the script asks for an ingredient which is required for the url to work and if there are any ingredients the user wouldn't like in the recipe.
    ingredient = input('What ingredient(s) would you like in your meal? ')

    wants_excluded_ingredient = input('Are there any ingredients you would not like in your meal? (Y/N) ')

    if wants_excluded_ingredient.lower() =='y':
        excluded_ingredient = input('What ingredient would you not like in your meal? ')
    else:
        excluded_ingredient = False

    excluded_ingredient_url = f"&excluded={excluded_ingredient}" if excluded_ingredient is not False else ""

    url = f'https://api.edamam.com/search?q={ingredient}&app_id=08ee5759&app_key=e9b043f56e57efe7282ee66f9488aede{diet_url_string}{excluded_ingredient_url}'

    response = requests.get(url)
    recipes_database = response.json()
    recipes = recipes_database['hits']

    for recipe in recipes:
        recipe_name = recipe['recipe']['label']
        recipe_url = recipe['recipe']['url']
        print(f'\n - {recipe_name}\n Find the recipe here: {recipe_url}\n')

recipe_search()


