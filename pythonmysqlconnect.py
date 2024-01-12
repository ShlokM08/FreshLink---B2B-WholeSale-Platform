import csv
import mysql.connector
from mysql.connector import Error

# Database credentials and information for the wholesaler's database
db_config = {
    "user": "root",
    "password": "root",
    "host": "127.0.0.1",
    "database": "WHOLESALER_1"
}

# Connecting to the MySQL database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("Successfully connected to the database")
except Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit(1)

def update_table():


    '''
    csv_file_name_user = input("Enter the name of the csv file: ")
    csv_file_name = csv_file_name_user + '.csv'

    try:

        with open(csv_file_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                productid = int(row[product_id])
                productname = row[product_name]
                Price = int(row[price])
                Stock = int(row[stock])


                
                query = f"INSERT INTO {csv_file_name_user} ({product_id}, {product_name}, {price}, {stock}) VALUES (%s, %s, %s, %s)"
                values = (productid, productname, Price, Stock)
                cursor.execute(query, values)
            conn.commit()
            print("Data inserted successfully")
            '''


def create_table_and_insert_data():
    table_name = input("Enter the name of the wholesaler (table): ")
    product_name = input("Name of the productname attribute: ")
    product_id = input("Name of the productid attribute: ")
    stock = input("Name of the stock attribute: ")
    price = input("Name of the price attribute: ")

    # Creating the table
    try:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {product_id} INT PRIMARY KEY,
            {product_name} VARCHAR(255),
            {price} INT,
            {stock} INT
        )
        """)
        print(f"Table {table_name} created successfully")
    except Error as e:
        print(f"Error creating table: {e}")
        return

    # Inserting data into the table
    csv_file_name = table_name + '.csv' 
    
    try:
        with open(csv_file_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                productid = int(row[product_id])
                productname = row[product_name]
                Price = int(row[price])
                Stock = int(row[stock])
                
                query = f"INSERT INTO {table_name} ({product_id}, {product_name}, {price}, {stock}) VALUES (%s, %s, %s, %s)"
                values = (productid, productname, Price, Stock)
                cursor.execute(query, values)
            conn.commit()
            print("Data inserted successfully")
    except FileNotFoundError:
        print(f"Error: The file {csv_file_name} does not exist")
    except Error as e:
        print(f"Error reading CSV file: {e}")
        conn.rollback()

def delete_table():
    table_name = input("Enter the name of the wholesaler (table): ")
    try:
        cursor.execute(f"DROP TABLE {table_name}")
        conn.commit()
        print(f"Table {table_name} deleted successfully")
    except Error as e:
        print(f"Error deleting table: {e}")
        conn.rollback()


def menu():
    while True:
        print("\nMenu:")
        print("1: Create new wholesaler (table) and insert data")
        #print("2: Update existing wholesaler (table)")
        #print("2: Delete existing wholesaler (table)")
        print("2: Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            create_table_and_insert_data()
        #elif choice == '2':
            #update_table()
            #continue
            
        elif choice == '2':
            break
        else:
            print("Invalid choice, please choose again.")

menu()
cursor.close()
conn.close()
print("Database connection closed")
