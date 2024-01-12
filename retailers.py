# from faker import Faker
# import random
# import csv

# fake = Faker("en_IN")


# # Generate wholesalers and locations
# wholesalers = []
# locations = [fake.city() for _ in range(50)]


# for _ in range(50):
#     wholesaler = {
#         "Name": fake.unique.company(),
#         "Location": random.choice(locations)
#     }
#     wholesalers.append(wholesaler)



# # Generate CSV data
# csv_data = []
# product_id_counter=5000
# passw=1234
    
# for wholesaler in wholesalers:
#         csv_data.append({
#             "Retailer_ID": product_id_counter,
#             'Retailer_Name': wholesaler["Name"],
#             "Contact_No": fake.phone_number(),
#             "Location": wholesaler["Location"],
#             "Lisence_No": fake.license_plate(),
#             "Retailer_pass":passw
            
#         })
#         product_id_counter+=1
# # Define CSV file path
# csv_file = r"C:\Users\Shlok Mehroliya\OneDrive\Documents\IIA Codes\retailers.csv"

# # Write data to CSV file
# with open(csv_file, mode='w', newline='') as file:
#     fieldnames = ['Retailer_ID','Retailer_Name','Contact_No',"Location","Lisence_No",'Retailer_pass']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)  
#     writer.writeheader()
#     for row in csv_data:
#         writer.writerow(row)

# print(f"Data saved to {csv_file}.")






