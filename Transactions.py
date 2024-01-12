from faker import Faker
import random
import csv

fake = Faker("en_IN")


# Generate wholesalers and locations
wholesalers = []
locations = [fake.city() for _ in range(50)]


for _ in range(50):
    wholesaler = {
        "Name": fake.unique.company(),
        "Location": random.choice(locations)
    }
    wholesalers.append(wholesaler)



# Generate CSV data
csv_data = []
Trans_id=1000

    
for wholesaler in wholesalers:
        csv_data.append({
             "Transaction_ID": Trans_id,
            "Wholesaler_ID": random.randint(1,5),
            'Retailer_ID': random.randint(5000,5049),
            "Listing_ID": random.randint(1,400),
            "Quantity": random.randint(500,549),
            "Payment": random.choice(["Cash","UPI","Credit Card","Debit Card","Cheque"]),
            "Date": fake.date_between(start_date='-1y', end_date='today'),
            "Time": fake.time_object(end_datetime=None)

            
        })
        Trans_id+=1
# Define CSV file path
csv_file = r"C:\Users\Shlok Mehroliya\OneDrive\Documents\IIA Codes\Transacations.csv"

# Write data to CSV file
with open(csv_file, mode='w', newline='') as file:
    fieldnames = ['Transaction_ID','Wholesaler_ID','Retailer_ID',"Listing_ID","Quantity","Payment","Date","Time"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)  
    writer.writeheader()
    for row in csv_data:
        writer.writerow(row)

print(f"Data saved to {csv_file}.")






