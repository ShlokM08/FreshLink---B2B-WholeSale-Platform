# from faker import Faker
# import random
# import csv

# fake = Faker("en_IN")

# # List of fruits and vegetables
# fruits_vegetables = [
#     "Mango", "Banana", "Guava", "Pomegranate", "Papaya", "Jackfruit", "Sapota", "Custard Apple", 
#     "Indian Gooseberry", "Lychee", "Pineapple", "Grapes", "Watermelon", "Orange", "Guava",
#     "Apple", "Pear", "Plum", "Apricot", "Fig", 
#     "Okra", "Brinjal", "Tomato", "Onion", "Potato", "Cauliflower", "Spinach", "Lady's Finger",
#     "Radish", "Carrot", "Cabbage", "Chilli", "Bitter Gourd", "Ridge Gourd", "Coriander Leaves",
#     "Bottle Gourd", "Green Peas", "Green Beans", "Drumstick", "Beetroot", "Cucumber", "Pumpkin",
#     "Turnip", "Sweet Potato", "Amaranth", "Cluster Beans", "Snake Gourd", "Lemon", "Ginger",
#     "Garlic", "Green Bell Pepper", "Ash Gourd", "Fenugreek Leaves", "Mint Leaves", "Curry Leaves",
#     "Radish Leaves", "Mustard Leaves", "Pointed Gourd", "Red Bell Pepper", "Turmeric", "Black Eyed Peas",
#     "Elephant Foot Yam", "Taro Root", "Arbi", "Bottle Gourd Leaves", "Red Pumpkin", "Cluster Fig",
#     "Ridge Gourd Leaves", "Colocasia Leaves", "Banana Flower", "Ivy Gourd", "Malabar Spinach",
#     "Yardlong Bean", "Chayote", "Black Cumin Seeds", "Green Sorrel", "Jute Mallow", "Water Spinach",
#     "Amaranth Leaves", "Dill Leaves", "Purslane", "Fenugreek Seeds", "Cluster Fig Leaves", "Curry Plant",
#     "Black Gram", "Lentils", "Chickpeas", "Pigeon Peas", "Green Gram", "Fenugreek Seeds"
# ]

# # Generate wholesalers and locations
# wholesalers = []
# locations = [fake.city() for _ in range(5)]

# for _ in range(5):
#     wholesaler = {
#         "Name": fake.unique.company(),
#         "Location": random.choice(locations)
#     }
#     wholesalers.append(wholesaler)

# # Create a dictionary to map products to wholesalers
# product_wholesaler_mapping = {}

# for product in fruits_vegetables:
#     random_wholesalers = random.sample(wholesalers, random.randint(1, 3))
#     product_wholesaler_mapping[product] = random_wholesalers

# # Generate CSV data
# csv_data = []

# processed_products = set()  # Set to keep track of processed products

# product_id_counter = 1000

# for product, wholesalers in product_wholesaler_mapping.items():
#     if product in processed_products:
#         continue  # Skip if product is already processed
#     processed_products.add(product)
    
#     if len(wholesalers) > 1:
#         wholesalers = random.sample(wholesalers, 1)  # Take a random wholesaler if more than one
    
#     for wholesaler in wholesalers:
#         csv_data.append({
#             "Product_ID": product_id_counter,
#             "Product": product,
#             'Price_20kg': random.randint(500,1000),
#             #'Wholesaler': wholesaler['Name'],
#             "Stock": random.randint(500,1000)
#         })
    
#         product_id_counter += 1

# # Define CSV file path
# csv_file = r"C:\Users\Shlok Mehroliya\OneDrive\Documents\IIA Codes\wholesale_data3.csv"
# gloabl_file = r"C:\Users\Shlok Mehroliya\OneDrive\Documents\IIA Codes\amazon.csv"


# # Write data to CSV file
# with open(csv_file, mode='w', newline='') as file:
#     fieldnames = ["Product_ID",'Product','Price_20kg',"Stock"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)  
#     writer.writeheader()
#     for row in csv_data:
#         writer.writerow(row)

# print(f"Data saved to {csv_file}.")

# with open(gloabl_file, mode='w', newline='') as file:
#     fieldnames = ["Product_ID",'Product','Price_20kg',"Stock"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)  
#     writer.writeheader()
#     for row in csv_data:
#         writer.writerow(row)

# print(f"Data saved to {gloabl_file}.")
