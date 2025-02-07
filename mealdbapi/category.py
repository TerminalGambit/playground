import json
import requests


def fetch_and_prettify_categories():
    url = "https://www.themealdb.com/api/json/v1/1/categories.php"
    response = requests.get(url)
    data = response.json()

    if not data.get("categories"):
        print("No categories found.")
        return

    categories = data["categories"]

    print("\nMeal Categories:")
    for category in categories:
        name = category.get("strCategory", "N/A")
        description = category.get("strCategoryDescription", "N/A").split("\r\n")[0]  # Shorten description
        image_url = category.get("strCategoryThumb", "N/A")

        print(f"\nCategory: {name}")
        print(f"Description: {description}")
        print(f"Image: {image_url}")
        print("-" * 40)


if __name__ == "__main__":
    fetch_and_prettify_categories()
