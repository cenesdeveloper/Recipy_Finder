import os
import requests

def search_recipes(query, diet=None, intolerances=None, cuisine=None):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": os.environ.get("SPOONACULAR_API_KEY"),
        "query": query,
        "diet": diet,
        "intolerances": intolerances,
        "cuisine": cuisine,
        "number": 10,
        "addRecipeInformation": True
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data.get('results', [])
