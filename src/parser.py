import json
import os
from datetime import datetime
from typing import List, Dict

import requests
from bs4 import BeautifulSoup

allowed_categories = ["vorspeise", "hauptgang", "dessert", "fruehstueck", "snacks", "brote", "getraenke"]
report = []

"""Get and provide Page Content"""


def get_page_content(link: str) -> str:
    """
    Get a Parsed HTML-Page as str.
    :param link:
    :return: parsed_page
    """
    homepage = requests.get(link)
    if not homepage.status_code == 200:
        report.append(f"Can't reach {link} with status code 200.")
        return False
    elif homepage.status_code == 200:
        parsed_page = BeautifulSoup(homepage.text, 'html.parser')
        return parsed_page


# main_page = get_page_content("https://storage.googleapis.com/www.selinaschoice.ch/index.html")

"""Get Links to scrape."""


def get_links_from_category(main_page: str, category: List) -> List:
    """
    Get a List recipes acording to the categories
    :param main_page: str
    :param category: list
    :return recipes: list
    """
    recipes = []
    recipes_by_category = main_page.find_all("div", class_=category)  # a -> div
    for tag in recipes_by_category:
        recipe = tag.a.get('href', None)
        recipes.append(recipe)
    return recipes


def get_links_to_scrape(main_page: str, categories=None) -> List:
    """
    Get all or some Recipes by categories. Default is None and will give you all recipies links.
    :param main_page: str
    :param categories: None, str oder List
    :return: recipes: list
    """
    if categories is None:
        recipes = get_links_from_category(main_page, allowed_categories)
        return recipes
    elif set(categories).issubset(set(allowed_categories)):
        recipes = get_links_from_category(main_page, categories)
        return recipes
    else:
        print(f"The one of the provided category's is not supported: {categories}")
        return False


"""Parse a Recipe"""


def get_timestamp(recipe: str) -> str:
    """
    Get Timestamp from when the recipe is created.
    :param recipe: str
    :return time: str
    """
    recipe.find_all('time')
    datetime_str = recipe.find('time')["datetime"]
    datetime_object = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%SZ")
    return str(datetime_object)


def get_recipe_title(recipe: str) -> str:
    """
    Get the Title from a recipe with a recipe link.
    :param recipe: str
    :return: title: str
    """
    title = recipe.h1.text
    return title


def get_prep_time(recipe: str) -> str:
    """
    Get the preparation time from a recipe.
    :param recipe: str
    :return prep_time: str
    """
    try:
        prep_time = recipe.find('time', itemprop="prepTime").text
    except AttributeError as e:
        print(f"Problem with {e}")
        prep_time = recipe.find('time', itemprop="performTime").text
    return prep_time


def get_serves(recipe: str) -> str:
    """
    Get serves from recipe.
    :param recipe: str
    :return serves: str
    """
    serves = recipe.find_all('li')[1].text
    return serves[8:]  # without index returns "serves: 4 persons"


def get_difficulty(recipe: str) -> str:
    """
    Get difficulty from recipe.
    :param recipe: str
    :return difficulty: str
    """
    difficulty = recipe.find_all('li')[2].text
    if difficulty[0:12] == "Difficulty: ":
        parts = difficulty.split(' ')
        return parts[1]  # without index returns "difficulty: easy emoji"
    else:
        return "easy"


def get_ingredients(recipe: str) -> List[Dict]:
    """
    get all ingredients from a recipe.
    :param recipe: str
    :return ingredientArray: list
    """
    ingredients = recipe.find("section", class_="ingredients")
    ingredient_array = []
    for li in ingredients.find_all('li'):
        quantity = li.find('div', class_='quantity').text
        ingredient = li.find('div', class_='name').text
        ingredientValues = {
            "quantity": quantity,
            "name": ingredient,
        }
        ingredient_array.append(ingredientValues)
    return ingredient_array


def get_instructions(recipe: str) -> List[Dict]:
    """
    Get the instructions from a recipe.
    :param recipe: str
    :return instructionArray: list
    """
    instruction_array = []
    instructions = recipe.find('section', class_='instructions')
    for li in instructions.find_all('li'):
        stepTitle = li.find('div', class_='details').h3.text
        stepInfo = li.find('div', class_='text').text
        instruction_values = {
            "step": stepTitle,
            "instruction": stepInfo,
        }
        instruction_array.append(instruction_values)
    return instruction_array


def get_category_from_recipe(main_page, link: str) -> str:
    """
    Get the one of allowed classes based on the recipe link.
    :param link: str
    :return recipe_class: str
    """
    specific_recipe = main_page.find("a", href=link).parent
    specific_recipe_class = specific_recipe["class"][1:]
    recipe_class = "".join(specific_recipe_class)
    if recipe_class in allowed_categories:
        return recipe_class
    else:
        print(f"The class from recipe: {link} is {recipe_class} and not in {allowed_categories}.")


def get_recipe_img_path(main_page: str, link: str) -> str:
    """
    Get the img path from a recipe with the recipe link.
    :param main_page: str
    :param link: str
    :return img_path: str
    """
    specific_recipe = main_page.find("a", href=link)
    img = specific_recipe.find("img")
    img_path_raw = img.get("src")
    img_path = img_path_raw.replace("\\", "/")
    return img_path


def get_parsed_recipe(recipe_link: str, main_page: str) -> Dict:
    if not get_page_content(recipe_link):
        print(f"{recipe_link} is corrupt")
    else:
        recipe = get_page_content(recipe_link)

        title = get_recipe_title(recipe)
        recipe_class = get_category_from_recipe(main_page, recipe_link)
        time_stamp = get_timestamp(recipe)
        img = get_recipe_img_path(main_page, recipe_link)
        prep_time = get_prep_time(recipe)
        serves = get_serves(recipe)
        difficulty = get_difficulty(recipe)
        ingredients = get_ingredients(recipe)
        instructions = get_instructions(recipe)

        recipe_dict = {
            "title": title,
            "recipe_class": recipe_class,
            "time": time_stamp,
            "img_path": img,
            "prep_time": prep_time,
            "serves": serves,
            "difficulty": difficulty,
            "ingredients": ingredients,
            "instructions": instructions,
        }
        return recipe_dict


"""Create Folder Structure"""


def create_folders():
    """
    Creates the main and subfolders for recipes and img.
    """
    os.chdir("..")
    try:
        os.mkdir("recipes")
        os.mkdir("img")
    except FileExistsError:
        print("Directory recipe and img already exists")

    for category in allowed_categories:
        dirName = category
        try:
            # create folders recipe
            os.chdir("./recipes")
            os.mkdir(dirName)
            # create img folders
            os.chdir("../img")
            os.mkdir(dirName)
            os.chdir("..")
        except FileExistsError:
            print("Directory ", dirName, " already exists")
    os.chdir("./src")
    print(os.getcwd())


"""Save a recipe"""


# ToDo
#  - function create_folders img/{recipe_class} and recipe/{recipe_class}
#  - make the backup function work
#  - provide a function, that saves the img from the recipe correct:
#  - recipes/img/{category}/{img_name}.jpg -> img_name = chili_con_simon.jpg

def save_recipe(recipe=Dict) -> json:
    filename = recipe["title"] + ".json"
    folder = recipe["recipe_class"]
    os.chdir(f"../recipes/{folder}")
    json_object = json.dumps(recipe, indent=4, ensure_ascii=False)
    with open(filename, "w", encoding="utf-8") as outfile:
        outfile.write(json_object)
    os.chdir("../../src")


def backup_recipe(main_page: str, link: str):
    if not get_page_content(link):
        print(f"{link} is corrupt")
    else:
        os.chdir("../recipes")
        dirName = get_category_from_recipe(main_page, link)
        recipe = get_parsed_recipe(main_page, link)
        try:
            # Create target Directory
            os.mkdir(dirName)
        except FileExistsError:
            print("Directory ", dirName, " already exists")
        save_recipe(recipe)


def backup_website(main_page: str, category=None):
    if category is None:
        raw_recipes = get_links_to_scrape(main_page, allowed_categories)
    else:
        raw_recipes = get_links_to_scrape(main_page, category)
    for recipe in raw_recipes:
        backup_recipe(recipe)
