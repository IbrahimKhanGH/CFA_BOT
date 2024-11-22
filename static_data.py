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
    "original chicken sandwich": "Original Chicken Sandwich",
    "regular chicken sandwich": "Original Chicken Sandwich",
    "original sandwich": "Original Chicken Sandwich",
    'waffle fries': 'Waffle Potato Fries',
    'fries': 'Waffle Potato Fries',
    'fry': 'Waffle Potato Fries',
    'milkshake': 'Milkshake',
    'shake': 'Milkshake',
    'iced tea': 'Freshly-Brewed Iced Tea',
    'tea': 'Freshly-Brewed Iced Tea',
    'iced coffee': 'Iced Coffee',
    'coffee': 'Iced Coffee',
    # Add other mappings as needed
}


size_required_items = {
    "Waffle Potato Fries": "Waffle Potato Fries",
    "Mac & Cheese": "Mac & Cheese",
    "Fruit Cup": "Fruit Cup",
    "Chicken Noodle Soup": "Chicken Noodle Soup",
    "Sweet Tea": "Freshly-Brewed Iced Tea Sweetened",
    "Unsweet Tea": "Freshly-Brewed Iced Tea Unsweetened",
    "Tea": "Freshly-Brewed Iced Tea Sweetened",
    "Iced Tea": "Freshly-Brewed Iced Tea Sweetened",
    "Lemonade": "Chick-fil-A Lemonade",
    "Diet Lemonade": "Chick-fil-A Diet Lemonade",
    "Soft Drink": "Soft Drink",
    "Soda": "Soft Drink",
    "Coke": "Soft Drink",
    "Sprite": "Soft Drink",
    "Dr Pepper": "Soft Drink",
    "Diet Coke": "Soft Drink",
    "Iced Coffee": "Iced Coffee",
    "Sunjoy": "Sunjoy",
    "Frosted Lemonade": "Frosted Lemonade",
    "Frosted Coffee": "Frosted Coffee",
    "Milkshake": "Milkshake",
    "Shake": "Milkshake",
    "Peppermint Milkshake": "Peppermint Chocolate Chip Milkshake",
    "Peppermint Chocolate Chip Milkshake": "Peppermint Chocolate Chip Milkshake"
}

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