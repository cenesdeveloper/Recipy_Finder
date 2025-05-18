import os
import requests
from flask import current_app

def search_recipes(query, diet=None, intolerances=None, cuisine=None):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "query": query,
        "apiKey": os.environ.get("SPOONACULAR_API_KEY"),
        "diet": diet,
        "intolerances": intolerances,
        "cuisine": cuisine,
        "number": 10,
        "addRecipeInformation": True
    }
    response = requests.get(url, params=params)
    return response.json().get("results", [])
