import csv
import mysql.connector
from mysql.connector import Error

# Database credentials and information for the wholesaler's database
db_config = {
    "user": "root",
    "password": "root",
    "host": "127.0.0.1",
    "database": "REVIEW_DATA"  # Name of the wholesaler's database
}

# Connecting to the MySQL database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("Successfully connected to the database")
except Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit(1)

table_name = "feedback"

# Creating the table with user provided name
try:
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS feedback (
        Review_ID INT PRIMARY KEY AUTO_INCREMENT,
        ListingID INT,
        Rating INT,
        Review_date DATE,
        Review_description VARCHAR(255)
    )
    """)
    print(f"Table {table_name} created successfully")
except Error as e:
    print(f"Error creating table: {e}")
    cursor.close()
    conn.close()
    exit(1)

# Function to transform and insert data
def insert_data(row):
    try:
        if isinstance(row, dict):  # If data is coming from CSV
            ListingID = int(row['ListingID'])
            Rating = int(row['Rating'])
            Review_Date = row['Review_Date']
            Review_description = row['Review']
        else:  # If data is coming from user input
            ListingID, Rating, Review_Date, Review_description = row
        
        query = f"INSERT INTO {table_name} (ListingID, Rating, Review_Date, Review_description) VALUES (%s, %s, %s, %s)"
        values = (ListingID, Rating, Review_Date, Review_description)
        cursor.execute(query, values)
        conn.commit()
    except Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

# Function to read data from CSV
def read_from_csv():
    csv_file_name = table_name + '.csv'
    try:
        with open(csv_file_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                insert_data(row)
        print("Data inserted successfully")
    except FileNotFoundError:
        print(f"Error: The file {csv_file_name} does not exist")
    except Error as e:
        print(f"Error reading CSV file: {e}")

# Function to handle user input
def input_data_manually():
    csv_file_name = table_name + '.csv'
    with open(csv_file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #get recent value of Review_ID
            Review_ID = int(row['Review_ID'])
        csvfile.close()


    ListingID = int(input("Enter ListingID: "))
    Rating = int(input("Enter Rating(1-5): "))
    Review_Date = input("Enter Review Date (YYYY-MM-DD): ")
    Review_description = input("Enter Review: ")
    
    user_input_data = (Review_ID, ListingID, Rating, Review_Date, Review_description)
    insert_data(user_input_data)
    print("Data inserted successfully")

# Main menu function
def main_menu():
    while True:
        print("\nMain Menu")
        print("1: Read from existing CSV file")
        print("2: Input data manually")
        print("0: Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            read_from_csv()
        elif choice == '2':
            input_data_manually()
        elif choice == '0':
            print("Exiting program")
            break
        else:
            print("Invalid choice, please enter a number between 0 and 2")

# Running the main menu
main_menu()

# Closing the database connection
cursor.close()
conn.close()
print("Database connection closed")
