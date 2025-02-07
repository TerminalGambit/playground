import json
import requests


def fetch_and_prettify_ingredients():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?i=list"
    response = requests.get(url)
    data = response.json()

    if not data.get("meals"):
        print("No ingredients found.")
        return

    ingredients = data["meals"]

    print("\nIngredients List:")
    for ingredient in ingredients:
        name = ingredient.get("strIngredient", "N/A")
        description = ingredient.get("strDescription")

        # Ensure description is not None before splitting
        if description:
            description = description.split("\r\n")[0]  # Shorten description
        else:
            description = "No description available"

        print(f"\nIngredient: {name}")
        print(f"Description: {description}")
        print("-" * 40)


if __name__ == "__main__":
    fetch_and_prettify_ingredients()