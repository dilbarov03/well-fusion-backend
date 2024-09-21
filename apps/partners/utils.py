from random import randint, choice
import decimal

from django.core.files import File

from apps.partners.models import CatererMenu, Caterer

# Sample data for populating
caterer_names = ["Healthy Eats", "Fit Fuel", "Green Plate", "Fresh Feasts", "Energy Bites",
                 "Lean Cuisine", "Vital Meals", "Nourish Now", "BodyFuel", "Clean Kitchen"]
locations = ["Tashkent", "Samarkand", "Bukhara", "Andijan", "Nukus", "Khiva",
             "Fergana", "Navoi", "Kokand", "Namangan"]
working_hours = ["9:00 AM - 6:00 PM", "8:00 AM - 5:00 PM", "10:00 AM - 8:00 PM",
                 "7:00 AM - 3:00 PM", "12:00 PM - 9:00 PM"]

meal_names = ["Grilled Chicken Salad", "Vegan Quinoa Bowl", "Protein Smoothie",
              "Turkey Wrap", "Salmon Avocado Roll", "Steak and Veggies",
              "Chicken Stir Fry", "Beef Tacos", "Spicy Tuna Sushi", "Egg White Omelette"]
ingredients = [
    "Chicken, Lettuce, Tomatoes, Olive Oil",
    "Quinoa, Avocado, Chickpeas, Lemon Dressing",
    "Whey Protein, Banana, Almond Milk",
    "Turkey, Whole Grain Wrap, Lettuce, Tomato",
    "Salmon, Avocado, Seaweed, Rice",
    "Steak, Broccoli, Carrots, Peppers",
    "Chicken, Bell Peppers, Soy Sauce, Rice",
    "Beef, Tortillas, Cheese, Lettuce, Tomatoes",
    "Tuna, Rice, Seaweed, Spicy Mayo",
    "Egg Whites, Spinach, Mushrooms, Cheese"
]
meal_prices = [12.99, 10.50, 8.00, 7.50, 15.00, 18.00, 11.00, 9.50, 13.00, 5.99]

# Placeholder image URLs for meals (you can replace these with real images)
image_urls = [
    "food-images/salad.jpg",
    "food-images/quinoa_bowl.jpg",
    "food-images/smoothie.jpg",
    "food-images/turkey_wrap.jpg",
    "food-images/salmon_roll.jpg",
    "food-images/steak.jpg",
    "food-images/stir_fry.jpg",
    "food-images/tacos.jpg",
    "food-images/tuna_sushi.jpg",
    "food-images/omelette.jpg"
]


def add_carterers():
    # Create 10 Caterers
    for i in range(10):
        caterer = Caterer.objects.create(
            name=caterer_names[i],
            location=locations[i % len(locations)],
            working_hours=working_hours[i % len(working_hours)],
            phone=f"+998{randint(71, 99)}{randint(100, 999)}{randint(10, 99)}{randint(10, 99)}"
        )

        # Create 10 Meals per Caterer
        for j in range(10):
            CatererMenu.objects.create(
                caterer=caterer,
                name=meal_names[j],
                ingredients=ingredients[j],
                image=File(open(f"static/{image_urls[j]}", "rb")),
                price=decimal.Decimal(meal_prices[j])
            )

    print("Database successfully populated with 10 caterers and 10 meals each!")
