import os
import requests
from bs4 import BeautifulSoup  # ✅ add this

def clean_summary(html):
    """Remove raw HTML from Spoonacular summary."""
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

def search_recipes(query, diet=None, intolerances=None, cuisine=None):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": os.environ.get("SPOONACULAR_API_KEY"),
        "query": query,
        "diet": diet,
        "intolerances": intolerances,
        "cuisine": cuisine,
        "number": 3,
        "addRecipeInformation": True
    }

    response = requests.get(url, params=params)
    data = response.json()
    recipes = data.get('results', [])

    # ✅ Clean the summary for each recipe
    for recipe in recipes:
        if "summary" in recipe:
            recipe["summary"] = clean_summary(recipe["summary"])

    return recipes
