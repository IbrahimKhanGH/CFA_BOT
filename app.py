from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

# Global storage for orders
orders = {}
last_ordered_item = {}

# Price list for menu items
price_list = {
    # Entrees
    "Chicken Sandwich": 4.29,
    "Deluxe Chicken Sandwich": 4.95,
    "Spicy Chicken Sandwich": 4.69,
    "Spicy Deluxe Sandwich": 5.25,
    "Grilled Chicken Sandwich": 5.65,
    "Grilled Chicken Club Sandwich": 7.25,
    "Nuggets (8-count)": 4.05,
    "Nuggets (12-count)": 5.95,
    "Grilled Nuggets (8-count)": 5.25,
    "Grilled Nuggets (12-count)": 7.85,
    "Chick-n-Strips (3-count)": 4.35,
    "Chick-n-Strips (4-count)": 5.19,
    "Chick-fil-A Cool Wrap": 6.75,
    "Grilled Cool Wrap": 6.79,

    # Salads
    "Cobb Salad": 8.19,
    "Spicy Southwest Salad": 8.19,
    "Market Salad": 8.19,
    "Side Salad": 4.09,

    # Sides
    "Waffle Potato Fries (Small)": 1.89,
    "Waffle Potato Fries (Medium)": 2.15,
    "Waffle Potato Fries (Large)": 2.45,
    "Mac & Cheese (Small)": 2.99,
    "Mac & Cheese (Medium)": 3.55,
    "Mac & Cheese (Large)": 5.25,
    "Fruit Cup (Small)": 2.85,
    "Fruit Cup (Medium)": 3.25,
    "Fruit Cup (Large)": 4.25,
    "Chicken Noodle Soup (Small)": 2.65,
    "Chicken Noodle Soup (Large)": 4.65,
    "Greek Yogurt Parfait": 3.45,
    "Side of Kale Crunch": 1.85,
    "Waffle Potato Chips": 1.89,

    # Beverages
    "Freshly-Brewed Iced Tea Sweetened (Small)": 1.65,
    "Freshly-Brewed Iced Tea Sweetened (Medium)": 1.85,
    "Freshly-Brewed Iced Tea Sweetened (Large)": 2.15,
    "Freshly-Brewed Iced Tea Unsweetened (Small)": 1.65,
    "Freshly-Brewed Iced Tea Unsweetened (Medium)": 1.85,
    "Freshly-Brewed Iced Tea Unsweetened (Large)": 2.15,
    "Chick-fil-A Lemonade (Small)": 1.99,
    "Chick-fil-A Lemonade (Medium)": 2.29,
    "Chick-fil-A Lemonade (Large)": 2.69,
    "Chick-fil-A Diet Lemonade (Small)": 1.99,
    "Chick-fil-A Diet Lemonade (Medium)": 2.29,
    "Chick-fil-A Diet Lemonade (Large)": 2.69,
    "Soft Drink (Small)": 1.65,
    "Soft Drink (Medium)": 1.85,
    "Soft Drink (Large)": 2.15,
    "1% Chocolate Milk": 1.29,
    "1% White Milk": 1.29,
    "Simply Orange Juice": 2.25,
    "Bottled Water": 1.79,
    "Coffee": 1.65,
    "Iced Coffee (Small)": 2.69,
    "Iced Coffee (Large)": 3.09,
    "Sunjoy (Small)": 1.99,
    "Sunjoy (Medium)": 2.29,
    "Sunjoy (Large)": 2.69,

    # Treats
    "Frosted Lemonade (Small)": 3.85,
    "Frosted Lemonade (Large)": 4.45,
    "Frosted Coffee (Small)": 3.85,
    "Frosted Coffee (Large)": 4.45,
    "Milkshake (Small)": 3.45,
    "Milkshake (Large)": 4.25,
    "Peppermint Chocolate Chip Milkshake (Small)": 3.65,
    "Peppermint Chocolate Chip Milkshake (Large)": 4.45,
    "Chocolate Chunk Cookie": 1.29,
    "Chocolate Chunk Cookie (6-count)": 7.29,
    "Icedream Cone": 1.39,
    "Icedream Cup": 1.25,
    "Chocolate Fudge Brownie": 1.89,

    # Kid's Meals
    "Nuggets Kid's Meal (4-count)": 3.35,
    "Nuggets Kid's Meal (6-count)": 4.05,
    "Grilled Nuggets Kid's Meal (4-count)": 3.75,
    "Grilled Nuggets Kid's Meal (6-count)": 4.45,
    "Chick-n-Strips Kid's Meal (1-count)": 3.25,
    "Chick-n-Strips Kid's Meal (2-count)": 3.95,

    # Breakfast Items
    "Chick-fil-A Chicken Biscuit": 3.09,
    "Spicy Chicken Biscuit": 3.29,
    "Chick-n-Minis (4-count)": 4.49,
    "Egg White Grill": 4.35,
    "Hash Brown Scramble Burrito": 3.75,
    "Hash Brown Scramble Bowl": 4.65,
    "Sausage Biscuit": 2.19,
    "Bacon, Egg & Cheese Biscuit": 3.59,
    "Sausage, Egg & Cheese Biscuit": 3.79,
    "Chicken, Egg & Cheese Bagel": 4.79,
    "Hash Browns": 1.09,
    "Greek Yogurt Parfait (Breakfast)": 3.45,
    "Fruit Cup (Breakfast, Small)": 2.85,

    # Sauces and Dressings (if applicable)
    "Chick-fil-A Sauce": 0.00,
    "Polynesian Sauce": 0.00,
    "Garden Herb Ranch Sauce": 0.00,
    "Zesty Buffalo Sauce": 0.00,
    "Honey Mustard Sauce": 0.00,
    "Barbeque Sauce": 0.00,
    "Sweet and Spicy Sriracha Sauce": 0.00,
    "Honey Roasted BBQ Sauce": 0.00,

    # Dressings
    "Avocado Lime Ranch Dressing": 0.00,
    "Fat-Free Honey Mustard Dressing": 0.00,
    "Garden Herb Ranch Dressing": 0.00,
    "Light Balsamic Vinaigrette Dressing": 0.00,
    "Light Italian Dressing": 0.00,
    "Zesty Apple Cider Vinaigrette Dressing": 0.00,
}

# Item name mapping and size required items
item_name_mapping = {
    "Waffle Fries": "Waffle Potato Fries",
    "Milkshake": "Milkshake",
    # Add other mappings as needed
}

size_required_items = [
    "Waffle Potato Fries",
    "Mac & Cheese",
    "Fruit Cup",
    "Chicken Noodle Soup",
    "Freshly-Brewed Iced Tea Sweetened",
    "Freshly-Brewed Iced Tea Unsweetened",
    "Chick-fil-A Lemonade",
    "Chick-fil-A Diet Lemonade",
    "Soft Drink",
    "Iced Coffee",
    "Sunjoy",
    "Frosted Lemonade",
    "Frosted Coffee",
    "Milkshake",
    "Peppermint Chocolate Chip Milkshake"
]

menu_items = {
    "Chicken Sandwich": {
        "price": 4.29,
        "ingredients": ["bun", "breaded chicken breast", "pickle slices", "butter"],
        "modifiable_ingredients": ["pickle slices"]
    },
    "Deluxe Chicken Sandwich": {
        "price": 4.95,
        "ingredients": ["bun", "breaded chicken breast", "pickle slices", "lettuce", "tomato", "American cheese", "butter"],
        "modifiable_ingredients": ["pickle slices", "lettuce", "tomato", "American cheese"]
    },
    "Spicy Chicken Sandwich": {
        "price": 4.69,
        "ingredients": ["bun", "spicy breaded chicken breast", "pickle slices", "butter"],
        "modifiable_ingredients": ["pickle slices"]
    },
    "Spicy Deluxe Sandwich": {
        "price": 5.25,
        "ingredients": ["bun", "spicy breaded chicken breast", "pickle slices", "lettuce", "tomato", "Pepper Jack cheese", "butter"],
        "modifiable_ingredients": ["pickle slices", "lettuce", "tomato", "Pepper Jack cheese"]
    },
    "Grilled Chicken Sandwich": {
        "price": 5.65,
        "ingredients": ["multigrain bun", "grilled chicken breast", "lettuce", "tomato", "honey roasted BBQ sauce"],
        "modifiable_ingredients": ["lettuce", "tomato", "honey roasted BBQ sauce"]
    },
    "Grilled Chicken Club Sandwich": {
        "price": 7.25,
        "ingredients": ["multigrain bun", "grilled chicken breast", "Colby-Jack cheese", "bacon", "lettuce", "tomato", "honey roasted BBQ sauce"],
        "modifiable_ingredients": ["Colby-Jack cheese", "bacon", "lettuce", "tomato", "honey roasted BBQ sauce"]
    },
    "Nuggets (8-count)": {
        "price": 4.05,
        "ingredients": ["bite-sized breaded chicken breast pieces", "seasoned breading", "peanut oil"],
        "modifiable_ingredients": []
    },
    "Nuggets (12-count)": {
        "price": 5.95,
        "ingredients": ["bite-sized breaded chicken breast pieces", "seasoned breading", "peanut oil"],
        "modifiable_ingredients": []
    },
    "Grilled Nuggets (8-count)": {
        "price": 5.25,
        "ingredients": ["bite-sized grilled chicken breast pieces", "seasoning"],
        "modifiable_ingredients": []
    },
    "Grilled Nuggets (12-count)": {
        "price": 7.85,
        "ingredients": ["bite-sized grilled chicken breast pieces", "seasoning"],
        "modifiable_ingredients": []
    },
    "Chick-n-Strips (3-count)": {
        "price": 4.35,
        "ingredients": ["breaded chicken breast strips", "seasoned breading", "peanut oil"],
        "modifiable_ingredients": []
    },
    "Chick-n-Strips (4-count)": {
        "price": 5.19,
        "ingredients": ["breaded chicken breast strips", "seasoned breading", "peanut oil"],
        "modifiable_ingredients": []
    },
    "Chick-fil-A Cool Wrap": {
        "price": 6.75,
        "ingredients": ["flaxseed flour flatbread", "grilled chicken breast", "lettuce", "shredded Monterey Jack and Cheddar cheeses", "red cabbage", "carrots"],
        "modifiable_ingredients": ["lettuce", "shredded Monterey Jack and Cheddar cheeses", "red cabbage", "carrots"]
    },
    "Grilled Cool Wrap": {
        "price": 6.79,
        "ingredients": ["flaxseed flour flatbread", "grilled chicken breast", "lettuce", "shredded Monterey Jack and Cheddar cheeses", "red cabbage", "carrots"],
        "modifiable_ingredients": ["lettuce", "shredded Monterey Jack and Cheddar cheeses", "red cabbage", "carrots"]
    },
    "Cobb Salad": {
        "price": 8.19,
        "ingredients": ["mixed greens", "breaded chicken nuggets", "roasted corn", "Monterey Jack and Cheddar cheeses", "bacon", "hard-boiled egg", "grape tomatoes", "crispy red bell peppers"],
        "modifiable_ingredients": ["breaded chicken nuggets", "roasted corn", "Monterey Jack and Cheddar cheeses", "bacon", "hard-boiled egg", "grape tomatoes", "crispy red bell peppers"]
    },
    "Spicy Southwest Salad": {
        "price": 8.19,
        "ingredients": ["mixed greens", "grilled spicy chicken breast", "Monterey Jack and Cheddar cheeses", "grape tomatoes", "roasted corn and black bean blend", "poblano chiles", "red bell peppers"],
        "modifiable_ingredients": ["grilled spicy chicken breast", "Monterey Jack and Cheddar cheeses", "grape tomatoes", "roasted corn and black bean blend", "poblano chiles", "red bell peppers"]
    },
    "Market Salad": {
        "price": 8.19,
        "ingredients": ["mixed greens", "grilled chicken breast", "blue cheese", "red and green apples", "strawberries", "blueberries", "harvest nut granola", "roasted almonds"],
        "modifiable_ingredients": ["grilled chicken breast", "blue cheese", "red and green apples", "strawberries", "blueberries", "harvest nut granola", "roasted almonds"]
    },
    "Side Salad": {
        "price": 4.09,
        "ingredients": ["mixed greens", "Monterey Jack and Cheddar cheeses", "grape tomatoes", "crispy red bell peppers"],
        "modifiable_ingredients": ["Monterey Jack and Cheddar cheeses", "grape tomatoes", "crispy red bell peppers"]
    },
    "Waffle Potato Fries (Small)": {
        "price": 1.89,
        "ingredients": ["potatoes", "canola oil", "sea salt"],
        "modifiable_ingredients": []
    },
    "Waffle Potato Fries (Medium)": {
        "price": 2.15,
        "ingredients": ["potatoes", "canola oil", "sea salt"],
        "modifiable_ingredients": []
    },
    "Waffle Potato Fries (Large)": {
        "price": 2.45,
        "ingredients": ["potatoes", "canola oil", "sea salt"],
        "modifiable_ingredients": []
    },
    "Mac & Cheese (Small)": {
        "price": 2.99,
        "ingredients": ["macaroni pasta", "cheddar cheese", "parmesan cheese", "romano cheese", "milk", "butter"],
        "modifiable_ingredients": []
    },
    "Mac & Cheese (Medium)": {
        "price": 3.55,
        "ingredients": ["macaroni pasta", "cheddar cheese", "parmesan cheese", "romano cheese", "milk", "butter"],
        "modifiable_ingredients": []
    },
    "Mac & Cheese (Large)": {
        "price": 5.25,
        "ingredients": ["macaroni pasta", "cheddar cheese", "parmesan cheese", "romano cheese", "milk", "butter"],
        "modifiable_ingredients": []
    },
    "Fruit Cup (Small)": {
        "price": 2.85,
        "ingredients": ["red apples", "green apples", "mandarin orange segments", "strawberries", "blueberries"],
        "modifiable_ingredients": ["red apples", "green apples", "mandarin orange segments", "strawberries", "blueberries"]
    },
    "Fruit Cup (Medium)": {
        "price": 3.25,
        "ingredients": ["red apples", "green apples", "mandarin orange segments", "strawberries", "blueberries"],
        "modifiable_ingredients": ["red apples", "green apples", "mandarin orange segments", "strawberries", "blueberries"]
    },
    "Fruit Cup (Large)": {
        "price": 4.25,
        "ingredients": ["red apples", "green apples", "mandarin orange segments", "strawberries", "blueberries"],
        "modifiable_ingredients": ["red apples", "green apples", "mandarin orange segments", "strawberries", "blueberries"]
    },
    "Chicken Noodle Soup (Small)": {
        "price": 2.65,
        "ingredients": ["shredded chicken breast", "egg noodles", "celery", "carrots", "broth"],
        "modifiable_ingredients": ["shredded chicken breast", "egg noodles", "celery", "carrots"]
    },
    "Chicken Noodle Soup (Large)": {
        "price": 4.65,
        "ingredients": ["shredded chicken breast", "egg noodles", "celery", "carrots", "broth"],
        "modifiable_ingredients": ["shredded chicken breast", "egg noodles", "celery", "carrots"]
    },
    "Greek Yogurt Parfait": {
        "price": 3.45,
        "ingredients": ["vanilla Greek yogurt", "strawberries", "blueberries", "harvest nut granola or chocolate cookie crumbs"],
        "modifiable_ingredients": ["strawberries", "blueberries", "harvest nut granola or chocolate cookie crumbs"]
    },
    "Side of Kale Crunch": {
        "price": 1.85,
        "ingredients": ["kale", "green cabbage", "apple cider and Dijon mustard vinaigrette", "roasted almonds"],
        "modifiable_ingredients": ["kale", "green cabbage", "roasted almonds"]
    },
    "Waffle Potato Chips": {
        "price": 1.89,
        "ingredients": ["potatoes", "canola oil", "sea salt"],
        "modifiable_ingredients": []
    },
    "Freshly-Brewed Iced Tea Sweetened (Small)": {
        "price": 1.65,
        "ingredients": ["brewed black tea", "cane sugar", "water", "ice"],
        "modifiable_ingredients": []
    },
    "Freshly-Brewed Iced Tea Sweetened (Medium)": {
        "price": 1.85,
        "ingredients": ["brewed black tea", "cane sugar", "water", "ice"],
        "modifiable_ingredients": []
    },
    "Freshly-Brewed Iced Tea Sweetened (Large)": {
        "price": 2.15,
        "ingredients": ["brewed black tea", "cane sugar", "water", "ice"],
        "modifiable_ingredients": []
    },
    "Freshly-Brewed Iced Tea Unsweetened (Small)": {
        "price": 1.65,
        "ingredients": ["brewed black tea", "water", "ice"],
        "modifiable_ingredients": []
    },
    "Freshly-Brewed Iced Tea Unsweetened (Medium)": {
        "price": 1.85,
        "ingredients": ["brewed black tea", "water", "ice"],
        "modifiable_ingredients": []
    },
    "Freshly-Brewed Iced Tea Unsweetened (Large)": {
        "price": 2.15,
        "ingredients": ["brewed black tea", "water", "ice"],
        "modifiable_ingredients": []
    },
    "Chick-fil-A Lemonade (Small)": {
        "price": 1.99,
        "ingredients": ["water", "lemon juice", "cane sugar", "ice"],
        "modifiable_ingredients": []
    },
    "Chick-fil-A Lemonade (Medium)": {
        "price": 2.29,
        "ingredients": ["water", "lemon juice", "cane sugar", "ice"],
        "modifiable_ingredients": []
    },
    "Chick-fil-A Lemonade (Large)": {
        "price": 2.69,
        "ingredients": ["water", "lemon juice", "cane sugar", "ice"],
        "modifiable_ingredients": []
    },
    "Chick-fil-A Diet Lemonade (Small)": {
        "price": 1.99,
        "ingredients": ["water", "lemon juice", "Splenda® No Calorie Sweetener", "ice"],
        "modifiable_ingredients": []
    },
    "Chick-fil-A Diet Lemonade (Medium)": {
        "price": 2.29,
        "ingredients": ["water", "lemon juice", "Splenda® No Calorie Sweetener", "ice"],
        "modifiable_ingredients": []
    },
    "Chick-fil-A Diet Lemonade (Large)": {
        "price": 2.69,
        "ingredients": ["water", "lemon juice", "Splenda® No Calorie Sweetener", "ice"],
        "modifiable_ingredients": []
    },
    "Soft Drink (Small)": {
        "price": 1.65,
        "ingredients": ["carbonated water", "sweetener", "natural flavors", "ice"],
        "modifiable_ingredients": []
    },
    "Soft Drink (Medium)": {
        "price": 1.85,
        "ingredients": ["carbonated water", "sweetener", "natural flavors", "ice"],
        "modifiable_ingredients": []
    },
    "Soft Drink (Large)": {
        "price": 2.15,
        "ingredients": ["carbonated water", "sweetener", "natural flavors", "ice"],
        "modifiable_ingredients": []
    },
    "1% Chocolate Milk": {
        "price": 1.29,
        "ingredients": ["low-fat milk", "sugar", "cocoa", "vitamins"],
        "modifiable_ingredients": []
    },
    "1% White Milk": {
        "price": 1.29,
        "ingredients": ["low-fat milk", "vitamins"],
        "modifiable_ingredients": []
    },
    "Simply Orange Juice": {
        "price": 2.25,
        "ingredients": ["100% orange juice"],
        "modifiable_ingredients": []
    },
    "Bottled Water": {
        "price": 1.79,
        "ingredients": ["purified water"],
        "modifiable_ingredients": []
    },
    "Coffee": {
        "price": 1.65,
        "ingredients": ["coffee", "water"],
        "modifiable_ingredients": []
    },
    "Iced Coffee (Small)": {
        "price": 2.69,
        "ingredients": ["coffee", "2% milk", "cane syrup", "ice"],
        "modifiable_ingredients": []
    },
    "Iced Coffee (Large)": {
        "price": 3.09,
        "ingredients": ["coffee", "2% milk", "cane syrup", "ice"],
        "modifiable_ingredients": []
    },
    "Sunjoy (Small)": {
        "price": 1.99,
        "ingredients": ["lemonade", "unsweetened iced tea", "ice"],
        "modifiable_ingredients": []
    },
    "Sunjoy (Medium)": {
        "price": 2.29,
        "ingredients": ["lemonade", "unsweetened iced tea", "ice"],
        "modifiable_ingredients": []
    },
    "Sunjoy (Large)": {
        "price": 2.69,
        "ingredients": ["lemonade", "unsweetened iced tea", "ice"],
        "modifiable_ingredients": []
    },
    "Frosted Lemonade (Small)": {
        "price": 3.85,
        "ingredients": ["Icedream®", "lemonade", "ice"],
        "modifiable_ingredients": []
    },
    "Frosted Lemonade (Large)": {
        "price": 4.45,
        "ingredients": ["Icedream®", "lemonade", "ice"],
        "modifiable_ingredients": []
    },
    "Frosted Coffee (Small)": {
        "price": 3.85,
        "ingredients": ["Icedream®", "cold-brewed coffee", "ice"],
        "modifiable_ingredients": []
    },
    "Frosted Coffee (Large)": {
        "price": 4.45,
        "ingredients": ["Icedream®", "cold-brewed coffee", "ice"],
        "modifiable_ingredients": []
    },
    "Milkshake (Small)": {
        "price": 3.45,
        "ingredients": ["Icedream®", "milk", "flavor syrup", "whipped cream", "cherry"],
        "modifiable_ingredients": ["whipped cream", "cherry"]
    },
    "Milkshake (Large)": {
        "price": 4.25,
        "ingredients": ["Icedream®", "milk", "flavor syrup", "whipped cream", "cherry"],
        "modifiable_ingredients": ["whipped cream", "cherry"]
    },
    "Peppermint Chocolate Chip Milkshake (Small)": {
        "price": 3.65,
        "ingredients": ["Icedream®", "milk", "peppermint flavor", "chocolate chips", "whipped cream", "cherry"],
        "modifiable_ingredients": ["whipped cream", "cherry"]
    },
    "Peppermint Chocolate Chip Milkshake (Large)": {
        "price": 4.45,
        "ingredients": ["Icedream®", "milk", "peppermint flavor", "chocolate chips", "whipped cream", "cherry"],
        "modifiable_ingredients": ["whipped cream", "cherry"]
    },
    "Chocolate Chunk Cookie": {
        "price": 1.29,
        "ingredients": ["flour", "sugar", "butter", "oats", "dark and milk chocolate chunks", "eggs"],
        "modifiable_ingredients": []
    },
    "Chocolate Chunk Cookie (6-count)": {
        "price": 7.29,
        "ingredients": ["flour", "sugar", "butter", "oats", "dark and milk chocolate chunks", "eggs"],
        "modifiable_ingredients": []
    },
    "Icedream Cone": {
        "price": 1.39,
        "ingredients": ["Icedream®", "waffle cone"],
        "modifiable_ingredients": []
    },
    "Icedream Cup": {
        "price": 1.25,
        "ingredients": ["Icedream®"],
        "modifiable_ingredients": []
    },
    "Chocolate Fudge Brownie": {
        "price": 1.89,
        "ingredients": ["cocoa", "semi-sweet chocolate", "butter", "sugar", "eggs", "flour"],
        "modifiable_ingredients": []
    },
    "Nuggets Kid's Meal (4-count)": {
        "price": 3.35,
        "ingredients": ["bite-sized breaded chicken breast pieces", "seasoned breading", "peanut oil"],
        "modifiable_ingredients": []
    },
    "Nuggets Kid's Meal (6-count)": {
        "price": 4.05,
        "ingredients": ["bite-sized breaded chicken breast pieces", "seasoned breading", "peanut oil"],
        "modifiable_ingredients": []
    },
    "Grilled Nuggets Kid's Meal (4-count)": {
        "price": 3.75,
        "ingredients": ["bite-sized grilled chicken breast pieces", "seasoning"],
        "modifiable_ingredients": []
    },
    "Grilled Nuggets Kid's Meal (6-count)": {
        "price": 4.45,
        "ingredients": ["bite-sized grilled chicken breast pieces", "seasoning"],
        "modifiable_ingredients": []
    },
    "Chick-n-Strips Kid's Meal (1-count)": {
        "price": 3.25,
        "ingredients": ["breaded chicken breast strips", "seasoned breading", "peanut oil"],
        "modifiable_ingredients": []
    },
    "Chick-n-Strips Kid's Meal (2-count)": {
        "price": 3.95,
        "ingredients": ["breaded chicken breast strips", "seasoned breading", "peanut oil"],
        "modifiable_ingredients": []
    },
    "Chick-fil-A Chicken Biscuit": {
        "price": 3.09,
        "ingredients": ["buttermilk biscuit", "breaded chicken breast", "butter"],
        "modifiable_ingredients": []
    },
    "Spicy Chicken Biscuit": {
        "price": 3.29,
        "ingredients": ["buttermilk biscuit", "spicy breaded chicken breast", "butter"],
        "modifiable_ingredients": []
    },
    "Chick-n-Minis (4-count)": {
        "price": 4.49,
        "ingredients": ["mini yeast rolls", "breaded chicken nuggets", "honey butter spread"],
        "modifiable_ingredients": []
    },
    "Egg White Grill": {
        "price": 4.35,
        "ingredients": ["multigrain English muffin", "grilled chicken breast", "egg whites", "American cheese"],
        "modifiable_ingredients": ["grilled chicken breast", "egg whites", "American cheese"]
    },
    "Hash Brown Scramble Burrito": {
        "price": 3.75,
        "ingredients": ["tortilla", "scrambled eggs", "hash browns", "Monterey Jack and Cheddar cheeses", "nuggets or sausage"],
        "modifiable_ingredients": ["scrambled eggs", "hash browns", "Monterey Jack and Cheddar cheeses", "nuggets or sausage"]
    },
    "Hash Brown Scramble Bowl": {
        "price": 4.65,
        "ingredients": ["scrambled eggs", "hash browns", "Monterey Jack and Cheddar cheeses", "nuggets or sausage"],
        "modifiable_ingredients": ["scrambled eggs", "hash browns", "Monterey Jack and Cheddar cheeses", "nuggets or sausage"]
    },
    "Sausage Biscuit": {
        "price": 2.19,
        "ingredients": ["buttermilk biscuit", "sausage patty", "butter"],
        "modifiable_ingredients": []
    },
    "Bacon, Egg & Cheese Biscuit": {
        "price": 3.59,
        "ingredients": ["buttermilk biscuit", "bacon", "scrambled egg", "American cheese", "butter"],
        "modifiable_ingredients": ["bacon", "scrambled egg", "American cheese"]
    },
    "Sausage, Egg & Cheese Biscuit": {
        "price": 3.79,
        "ingredients": ["buttermilk biscuit", "sausage patty", "scrambled egg", "American cheese", "butter"],
        "modifiable_ingredients": ["sausage patty", "scrambled egg", "American cheese"]
    },
    "Chicken, Egg & Cheese Bagel": {
        "price": 4.79,
        "ingredients": ["toasted sunflower multigrain bagel", "breaded chicken breast", "folded egg", "American cheese"],
        "modifiable_ingredients": ["folded egg", "American cheese"]
    },
    "Hash Browns": {
        "price": 1.09,
        "ingredients": ["potatoes", "canola oil", "sea salt"],
        "modifiable_ingredients": []
    },
    "Greek Yogurt Parfait (Breakfast)": {
        "price": 3.45,
        "ingredients": ["vanilla Greek yogurt", "strawberries", "blueberries", "harvest nut granola or chocolate cookie crumbs"],
        "modifiable_ingredients": ["strawberries", "blueberries", "harvest nut granola or chocolate cookie crumbs"]
    },
    "Fruit Cup (Breakfast, Small)": {
        "price": 2.85,
        "ingredients": ["red apples", "green apples", "mandarin orange segments", "strawberries", "blueberries"],
        "modifiable_ingredients": ["red apples", "green apples", "mandarin orange segments", "strawberries", "blueberries"]
    },
    "Chick-fil-A Sauce": {
        "price": 0.00,
        "ingredients": ["soybean oil", "sugar", "BBQ sauce", "mustard", "egg yolk", "vinegar", "lemon juice"],
        "modifiable_ingredients": []
    },
    "Polynesian Sauce": {
        "price": 0.00,
        "ingredients": ["sugar", "soybean oil", "corn syrup", "tomato paste", "vinegar"],
        "modifiable_ingredients": []
    },
    "Garden Herb Ranch Sauce": {
        "price": 0.00,
        "ingredients": ["soybean oil", "buttermilk", "egg yolk", "vinegar", "herbs"],
        "modifiable_ingredients": []
    },
    "Zesty Buffalo Sauce": {
        "price": 0.00,
        "ingredients": ["distilled vinegar", "cayenne red pepper", "salt", "garlic"],
        "modifiable_ingredients": []
    },
    "Honey Mustard Sauce": {
        "price": 0.00,
        "ingredients": ["honey", "mustard", "vinegar", "soybean oil", "spices"],
        "modifiable_ingredients": []
    },
    "Barbeque Sauce": {
        "price": 0.00,
        "ingredients": ["tomato paste", "vinegar", "corn syrup", "molasses", "spices"],
        "modifiable_ingredients": []
    },
    "Sweet and Spicy Sriracha Sauce": {
        "price": 0.00,
        "ingredients": ["sugar", "water", "red chili peppers", "vinegar", "garlic"],
        "modifiable_ingredients": []
    },
    "Honey Roasted BBQ Sauce": {
        "price": 0.00,
        "ingredients": ["soybean oil", "honey", "BBQ sauce", "mustard", "vinegar"],
        "modifiable_ingredients": []
    },
    "Avocado Lime Ranch Dressing": {
        "price": 0.00,
        "ingredients": ["soybean oil", "buttermilk", "avocado", "lime juice", "herbs"],
        "modifiable_ingredients": []
    },
    "Fat-Free Honey Mustard Dressing": {
        "price": 0.00,
        "ingredients": ["water", "honey", "mustard", "vinegar", "spices"],
        "modifiable_ingredients": []
    },
    "Garden Herb Ranch Dressing": {
        "price": 0.00,
        "ingredients": ["soybean oil", "buttermilk", "egg yolk", "vinegar", "herbs"],
        "modifiable_ingredients": []
    },
    "Light Balsamic Vinaigrette Dressing": {
        "price": 0.00,
        "ingredients": ["water", "balsamic vinegar", "olive oil", "spices"],
        "modifiable_ingredients": []
    },
    "Light Italian Dressing": {
        "price": 0.00,
        "ingredients": ["water", "vinegar", "olive oil", "lemon juice", "spices"],
        "modifiable_ingredients": []
    },
    "Zesty Apple Cider Vinaigrette Dressing": {
        "price": 0.00,
        "ingredients": ["apple cider vinegar", "olive oil", "orange juice", "spices"],
        "modifiable_ingredients": []
    }
}


# Add this function at the top with your other helper functions


def calculate_total(order_items):
    total = 0
    for item in order_items:
        # Use base item name for price lookup
        base_item_name = item['base_item_name']
        quantity = item.get('quantity', 1)
        # Get base price from menu_items
        item_data = menu_items.get(base_item_name)
        if item_data:
            price = item_data.get('price', 0)
            total += price * quantity
        else:
            print(f"Warning: '{base_item_name}' not found in menu_items.")
    return total

# Helper function to create response


def create_response(message):
    return jsonify({
        'fulfillmentText': message,
        'fulfillmentMessages': [
            {
                'text': {
                    'text': [message]
                }
            }
        ]
    })


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        print("\n=== WEBHOOK REQUEST ===")
        req = request.get_json(silent=True, force=True)

        # Detailed debug logging
        query_result = req.get('queryResult', {})
        intent = query_result.get('intent', {})

        print("Intent Data:", {
            'displayName': intent.get('displayName'),
            'parameters': query_result.get('parameters'),
            'queryText': query_result.get('queryText'),
            'fulfillmentText': query_result.get('fulfillmentText')
        })

        # Check if intent names match exactly
        intent_name = intent.get('displayName')
        print(f"Received intent: '{intent_name}'")
        print(f"Intent type: {type(intent_name)}")  # Check if it's a string

        if req is None:
            return jsonify({'fulfillmentText': "Invalid request format."})

        print("Raw Request:", json.dumps(req, indent=2))

        session_id = req.get('session')
        query_result = req.get('queryResult', {})
        intent_name = query_result.get('intent', {}).get('displayName')
        query_text = query_result.get('queryText', '').lower()
        parameters = query_result.get('parameters', {})

        # Initialize orders if needed
        if session_id not in orders:
            orders[session_id] = []

        print(f"Session ID: {session_id}")
        print(f"Received intent: {intent_name}")
        print(f"Query Text: {query_text}")
        print(f"Parameters: {parameters}")
        print(
            f"Current orders before processing: {orders.get(session_id, [])}")

        # List of handled intents
        HANDLED_INTENTS = [
            'OrderFood',
            'OrderFood - size',
            'SpecifySize',
            'ModifyOrder',
            'SandwichSpicyOrNot',
            'SandwichSpicyOrNot - custom',
            'SandwichSpicyOrNot - custom-2',
            'ReviewOrder',
            'OrderCompletion',
            'ConfirmOrder',
            'Default Welcome Intent'
        ]
        print(
            f"Is intent '{intent_name}' in handled intents? {intent_name in HANDLED_INTENTS}")

        if intent_name == 'OrderFood':
            order_items = parameters.get('order_items')
            if not order_items:
                return create_response("Please specify what you'd like to order.")

            # Ensure order_items is a list
            if not isinstance(order_items, list):
                order_items = [order_items]

            for order in order_items:
                food_item = order.get('food_item')
                size = order.get('size', '')
                quantity = order.get('quantity', 1)
                modifications = order.get('modification', [])
                ingredients = order.get('ingredient', [])

                # Ensure modifications and ingredients are lists
                if not isinstance(modifications, list):
                    modifications = [modifications]
                if not isinstance(ingredients, list):
                    ingredients = [ingredients]

                # Build base item name and full item name
                mapped_item = item_name_mapping.get(food_item, food_item)
                base_item_name = mapped_item  # Base item name without size
                if size:
                    full_item_name = f"{mapped_item} ({size})"
                else:
                    full_item_name = mapped_item

                # Validate item exists in menu_items
                item_data = menu_items.get(full_item_name)
                if not item_data:
                    return create_response(f"Sorry, we don't have {full_item_name} on the menu.")

                # Process modifications
                applied_modifications = []
                modifiable_ingredients = item_data.get(
                    'modifiable_ingredients', [])

                if modifications and ingredients:
                    if len(modifications) != len(ingredients):
                        return create_response("Please specify both the modification and the ingredient you want to modify.")

                    for mod, ing in zip(modifications, ingredients):
                        if ing in modifiable_ingredients:
                            if mod in ['no', 'remove', 'without', 'hold', 'skip']:
                                applied_modifications.append(f"no {ing}")
                            elif mod in ['add', 'extra', 'more', 'with']:
                                applied_modifications.append(f"extra {ing}")
                            else:
                                applied_modifications.append(f"{mod} {ing}")
                        else:
                            return create_response(f"Sorry, you can't modify {ing} on the {full_item_name}.")
                elif modifications or ingredients:
                    # If only one is provided
                    return create_response("Please specify both the modification and the ingredient you want to modify.")

                # Create order item
                order_item = {
                    # Use full_item_name as base item name for price lookup
                    'base_item_name': full_item_name,
                    'full_item_name': full_item_name,
                    'quantity': int(quantity),
                    'modifications': applied_modifications
                }
                orders[session_id].append(order_item)

            return create_response("Your items have been added to your order. Would you like anything else?")

        elif intent_name == 'OrderFood - size':
            size = parameters.get('size', '')
            if session_id in last_ordered_item:
                pending_item = last_ordered_item[session_id]
                food_item = pending_item['item']
                quantity = pending_item['quantity']

                full_item_name = f"{food_item} ({size})"
                order_item = {
                    'base_item_name': full_item_name,  # Use full_item_name as base_item_name
                    'full_item_name': full_item_name,
                    'quantity': quantity,
                    'modifications': []
                }
                orders[session_id].append(order_item)
                del last_ordered_item[session_id]

                return create_response(f"I've added {quantity} {full_item_name} to your order. Would you like anything else?")

        elif intent_name == 'SpecifySize':
            size = parameters.get('Size', '')
            if session_id in last_ordered_item:
                pending_item = last_ordered_item[session_id]
                food_item = pending_item['item']
                quantity = pending_item['quantity']

                full_item_name = f"{food_item} ({size})"
                order_item = {
                    'base_item_name': full_item_name,
                    'full_item_name': full_item_name,
                    'quantity': quantity,
                    'modifications': []
                }
                orders[session_id].append(order_item)
                del last_ordered_item[session_id]

                return create_response(f"I've added {quantity} {full_item_name} to your order. Would you like anything else?")

        elif intent_name == 'ModifyOrder':
            # Implement modify order functionality as needed
            pass  # Placeholder

        elif intent_name == 'SandwichSpicyOrNot':
            return create_response("Would you like your chicken sandwich original or spicy?")

        elif intent_name == 'SandwichSpicyOrNot - custom':
            order_item = {
                'base_item_name': 'Spicy Chicken Sandwich',
                'full_item_name': 'Spicy Chicken Sandwich',
                'quantity': 1,
                'modifications': []
            }
            orders[session_id].append(order_item)
            print(f"Added to order: {order_item}")
            return create_response("Sure, I have added a Spicy Chicken Sandwich to your order.")

        elif intent_name == 'SandwichSpicyOrNot - custom-2':
            order_item = {
                'base_item_name': 'Chicken Sandwich',
                'full_item_name': 'Chicken Sandwich',
                'quantity': 1,
                'modifications': []
            }
            orders[session_id].append(order_item)
            print(f"Added to order: {order_item}")
            return create_response("Sure, I have added a Chicken Sandwich to your order.")

        elif intent_name == 'ReviewOrder':
            order_items = orders.get(session_id, [])
            if not order_items:
                return create_response("You haven't ordered anything yet.")

            order_summary = ''
            for item in order_items:
                quantity = item.get('quantity', 1)
                full_item_name = item['full_item_name']
                mods = ', '.join(item.get('modifications', []))
                if mods:
                    order_summary += f"{quantity} x {full_item_name} ({mods})\n"
                else:
                    order_summary += f"{quantity} x {full_item_name}\n"

            total_price = calculate_total(order_items)
            return create_response(f"Here's your current order:\n{order_summary}\nTotal: ${total_price:.2f}")

        elif intent_name == 'OrderCompletion':
            order_items = orders.get(session_id, [])
            if not order_items:
                return create_response("It seems you haven't ordered anything yet. What would you like to order?")

            order_summary = ''
            for item in order_items:
                quantity = item.get('quantity', 1)
                full_item_name = item['full_item_name']
                base_item_name = item['base_item_name']
                item_data = menu_items.get(base_item_name)
                price = item_data.get('price', 0) if item_data else 0
                item_total = price * quantity
                mods = ', '.join(item.get('modifications', []))
                if mods:
                    order_summary += f"{quantity} x {full_item_name} ({mods}) - ${item_total:.2f}\n"
                else:
                    order_summary += f"{quantity} x {full_item_name} - ${item_total:.2f}\n"

            total_price = calculate_total(order_items)
            return create_response(f"Thank you for your order! Here's what you ordered:\n{order_summary}\nTotal: ${total_price:.2f}\nWould you like to confirm your order?")

        elif intent_name == 'ConfirmOrder':
            # Handle order confirmation
            order_items = orders.get(session_id, [])
            if not order_items:
                return create_response("It seems you haven't ordered anything yet. What would you like to order?")

            # Confirm the order
            order_summary = ''
            for item in order_items:
                quantity = item.get('quantity', 1)
                full_item_name = item['full_item_name']
                order_summary += f"{quantity} x {full_item_name}\n"

            total_price = calculate_total(order_items)
            # Clear the order after confirmation
            orders[session_id] = []
            return create_response(f"Your order has been confirmed! Here's what you ordered:\n{order_summary}\nTotal: ${total_price:.2f}\nThank you for choosing Chick-fil-A!")

        elif intent_name == 'MenuQuery':
            # Respond with menu categories or items
            menu_categories = "We offer Chicken Sandwiches, Salads, Sides, Beverages, and Treats. What would you like to know more about?"
            return create_response(menu_categories)

        elif intent_name == 'ItemQuery':
            food_item = parameters.get('food_item', '')
            attribute = parameters.get('attribute', '')
            if not food_item:
                return create_response("Please specify the item you're interested in.")

            item_data = menu_items.get(food_item)
            if not item_data:
                return create_response(f"Sorry, we don't have {food_item} on the menu.")

            if attribute in ['price', 'cost']:
                price = item_data.get('price')
                return create_response(f"The {food_item} costs ${price:.2f}.")
            elif attribute in ['ingredients', 'nutrition']:
                ingredients = ', '.join(item_data.get('ingredients', []))
                return create_response(f"The {food_item} contains: {ingredients}.")
            else:
                # Provide a general description or handle other attributes
                return create_response(f"The {food_item} is one of our popular items.")

        elif intent_name == 'Default Welcome Intent':
            return create_response("Welcome to Chick-fil-A! How can I help you today?")

        else:
            print(f"WARNING: Unhandled intent: {intent_name}")
            return jsonify({
                'fulfillmentText': f"I'm sorry, I didn't understand that. Could you please rephrase?"
            })

        print(f"Current orders after processing: {orders.get(session_id, [])}")

    except Exception as e:
        print(f"Error in webhook: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'fulfillmentText': "I encountered an error processing your request."
        })


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
