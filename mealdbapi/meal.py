import json
import requests


def fetch_and_prettify_meal(meal_name):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal_name}"
    response = requests.get(url)
    data = response.json()

    if not data["meals"]:
        print("No meal found.")
        return

    meal = data["meals"][0]

    # Extracting relevant details
    meal_name = meal.get("strMeal", "N/A")
    category = meal.get("strCategory", "N/A")
    area = meal.get("strArea", "N/A")
    instructions = meal.get("strInstructions", "N/A").replace("\r\n", "\n")
    image_url = meal.get("strMealThumb", "N/A")
    youtube_url = meal.get("strYoutube", "N/A")

    # Extracting ingredients and measurements
    ingredients = []
    for i in range(1, 21):
        ingredient = meal.get(f"strIngredient{i}")
        measure = meal.get(f"strMeasure{i}")
        if ingredient and ingredient.strip():
            ingredients.append(f"{measure} {ingredient}".strip())

    # Pretty print the output
    print("\nMeal Information:")
    print(f"Name: {meal_name}")
    print(f"Category: {category}")
    print(f"Cuisine: {area}")
    print(f"Image: {image_url}")
    print(f"YouTube Tutorial: {youtube_url}")
    print("\nIngredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

    print("\nInstructions:")
    print(instructions)


if __name__ == "__main__":
    meal_name = "Curry"
    fetch_and_prettify_meal(meal_name)
