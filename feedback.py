
from faker import Faker
import random
import csv

fake = Faker("en_IN")

# List of fruits and vegetables
fruits_vegetables = [
    "Mango", "Banana", "Guava", "Pomegranate", "Papaya", "Jackfruit", "Sapota", "Custard Apple", 
    "Indian Gooseberry", "Lychee", "Pineapple", "Grapes", "Watermelon", "Orange", "Guava",
    "Apple", "Pear", "Plum", "Apricot", "Fig", 
    "Okra", "Brinjal", "Tomato", "Onion", "Potato", "Cauliflower", "Spinach", "Lady's Finger",
    "Radish", "Carrot", "Cabbage", "Chilli", "Bitter Gourd", "Ridge Gourd", "Coriander Leaves",
    "Bottle Gourd", "Green Peas", "Green Beans", "Drumstick", "Beetroot", "Cucumber", "Pumpkin",
    "Turnip", "Sweet Potato", "Amaranth", "Cluster Beans", "Snake Gourd", "Lemon", "Ginger",
    "Garlic", "Green Bell Pepper", "Ash Gourd", "Fenugreek Leaves", "Mint Leaves", "Curry Leaves",
    "Radish Leaves", "Mustard Leaves", "Pointed Gourd", "Red Bell Pepper", "Turmeric", "Black Eyed Peas",
    "Elephant Foot Yam", "Taro Root", "Arbi", "Bottle Gourd Leaves", "Red Pumpkin", "Cluster Fig",
    "Ridge Gourd Leaves", "Colocasia Leaves", "Banana Flower", "Ivy Gourd", "Malabar Spinach",
    "Yardlong Bean", "Chayote", "Black Cumin Seeds", "Green Sorrel", "Jute Mallow", "Water Spinach",
    "Amaranth Leaves", "Dill Leaves", "Purslane", "Fenugreek Seeds", "Cluster Fig Leaves", "Curry Plant",
    "Black Gram", "Lentils", "Chickpeas", "Pigeon Peas", "Green Gram", "Fenugreek Seeds"
]

# Generate wholesalers and locations
wholesalers = []
locations = [fake.city() for _ in range(5)]

for _ in range(5):
    wholesaler = {
        "Name": fake.unique.company(),
        "Location": random.choice(locations)
    }
    wholesalers.append(wholesaler)

# Create a dictionary to map products to wholesalers
product_wholesaler_mapping = {}

for product in fruits_vegetables:
    random_wholesalers = random.sample(wholesalers, random.randint(1, 3))
    product_wholesaler_mapping[product] = random_wholesalers

# Generate CSV data
csv_data = []

product_id_counter = 1000
Review_id_counter =0
wholesaler_id=2000

for product, wholesalers in product_wholesaler_mapping.items():
    for wholesaler in wholesalers:
        csv_data.append({
            "ReviewID": Review_id_counter,
            "ListingID": product_id_counter+wholesaler_id,
            "Rating": random.randint(1, 5),
            "Review_Date": fake.date_between(start_date='-1y', end_date='today'),
            "Review": fake.paragraph(nb_sentences=3),

        })
    
        product_id_counter += 1
        wholesaler_id += 1
        Review_id_counter+=1

# Define CSV file path
csv_file = r"C:\Users\Shlok Mehroliya\OneDrive\Documents\IIA Codes\feedback.csv"

# Write data to CSV file
with open(csv_file, mode='w', newline='') as file:
    fieldnames = ["ReviewID",'ListingID', 'Rating', 'Review_Date','Review']
    writer = csv.DictWriter(file, fieldnames=fieldnames)  
    writer.writeheader()
    for row in csv_data:
        writer.writerow(row)

print(f"Data saved to {csv_file}.")
