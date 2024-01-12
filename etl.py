import mysql.connector
from mysql.connector import Error

import os
import os
import csv
import os
import csv
import mysql.connector
import random as rand

from mysql.connector import Error

# Database credentials and information
db_config = {
    "user": "root",
    "password": "root",
    "host": "127.0.0.1",
    "database": "IIA_database"
}

db_config_wholesaler = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'wholesaler_1',
}
db_config_review = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'review_data',
}

# Connecting to the MySQL database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("Successfully connected to the database")
except Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit(1)



def insert_into_wholesalers():
    try:
        wholesaler_id = int(input("Enter wholesaler ID: "))
        business_name = input("Enter business name: ")
        contact_no = input("Enter contact number: ")
        state = input("Enter state: ")
        license_id = input("Enter license ID: ")

        query = """
        INSERT INTO WholesalersInfo (WholesalerID, BusinessName, ContactNo, State, LicenseID)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (wholesaler_id, business_name, contact_no, state, license_id)
        cursor.execute(query, values)
        conn.commit()
        print("Data inserted successfully into WholesalersInfo")
    except Error as e:
        print(f"Error: {e}")
        conn.rollback()

# Function to list tables from the wholesaler_1 database

def list_table():
    
    try:
        # Connecting to the wholesaler_1 database
        conn_wholesaler = mysql.connector.connect(**db_config_wholesaler)
        cursor_wholesaler = conn_wholesaler.cursor()

        # Getting the table names from wholesaler_1
        cursor_wholesaler.execute("SHOW TABLES")
        tables = cursor_wholesaler.fetchall()
        print("\nNumber of tables in wholesaler_1:", len(tables))
        for table in tables:
            table_name = table[0]
            print("\nTable name:", table_name)
            
            # Asking user for additional information
            wholesaler_id_counter = int(input("Enter wholesaler ID for this wholesaler: "))
            contact_no = input("Enter contact number for this wholesaler: ").strip()
            state = input("Enter state for this wholesaler: ").strip()
            license_id = input("Enter license ID for this wholesaler: ").strip()
            
            # Inserting the data into WholesalersInfo in IIA_database
            try:
                query = """
                INSERT INTO WholesalersInfo (WholesalerID, BusinessName, ContactNo, State, LicenseID)
                VALUES (%s, %s, %s, %s, %s)
                """
                values = (wholesaler_id_counter, table_name, contact_no, state, license_id)
                cursor.execute(query, values)
                conn.commit()
                print(f"Data for table name {table_name} inserted into WholesalersInfo with WholesalerID {wholesaler_id_counter}")
                
                wholesaler_id_counter += 1  # Increment the counter for the next entry
                
            except Error as e:
                print(f"Error inserting data for table name {table_name} into WholesalersInfo: {e}")
                conn.rollback()

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor_wholesaler.close()
        conn_wholesaler.close()


# Function for the main menu
def wholesaler_menu():
    while True:
        print("\nMenu:")
        print("1: Insert into NEW WholesalersInfo")
        print("2: Adding from wholesaler database")
        print("3: Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            insert_into_wholesalers()
        elif choice == '2':
            list_table()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please choose again.")

def insert_into_retailers():
    try:
        retailer_info = int(input("Enter retailer info ID: "))
        retailer_name = input("Enter retailer name: ")
        contact_no = input("Enter contact number: ")
        address = input("Enter address: ")
        license_no = input("Enter license ID: ")

        query = """
        INSERT INTO RetailersInfo (RetailerInfo, RetailerName, ContactNo, Address, license_no)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (retailer_info, retailer_name, contact_no, address,license_no)
        cursor.execute(query, values)
        conn.commit()
        print("Data inserted successfully into RetailersInfo")
    except Error as e:
        print(f"Error: {e}")
        conn.rollback()

# def insert_into_retailer_csv():
#     # Function to read data from CSV
#     csv_input = input("Enter CSV file name: ")
#     csv_file_name = csv_input + '.csv'
#     try:
#         with open(csv_file_name, 'r') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
#                     print(row)

#                     retailer_info = int(row['Retailer_ID'])
#                     retailer_name = row['Retailer_Name']
#                     contact_no = row['Contact_No']
#                     address = row['Location']
#                     license_no = row['Lisence_No']
#                     Retailer_pass=int(row['Retailer_pass'])

#                     query = """ 
#                     Insert into RetailersInfo (RetailerInfo, RetailerName, ContactNo, Address, Lisence_No,Retailer_pass) Values (%s, %s, %s, %s, %s, %s)
#                     """

#                     values=(retailer_info, retailer_name, contact_no, address, license_no,Retailer_pass)
#                     cursor.execute(query, values)
#                     conn.commit()  


#         print("Data inserted successfully")
#     except FileNotFoundError:
#         print(f"Error: The file {csv_file_name} does not exist")
#     except Error as e:
#         print(f"Error reading CSV file: {e}")
import csv
import mysql.connector
from mysql.connector import Error

def insert_into_retailer_csv():
    # Function to read data from CSV
    csv_input = input("Enter CSV file name: ")
    csv_file_name = csv_input + '.csv'

    try:
        with open(csv_file_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                print(row)

                retailer_info = int(row['Retailer_ID'])
                retailer_name = row['Retailer_Name']
                contact_no = row['Contact_No']
                address = row['Location']
                license_no = row['Lisence_No']
                Retailer_pass = int(row['Retailer_pass'])

                # Check if the record with the same 'Retailer_ID' already exists
                check_query = "SELECT RetailerInfo FROM RetailersInfo WHERE RetailerInfo = %s"
                cursor.execute(check_query, (retailer_info,))
                existing_record = cursor.fetchone()

                if existing_record:
                    print(f"Record with Retailer_ID {retailer_info} already exists. Skipping insertion.")
                else:
                    # If not, insert the record
                    insert_query = """
                        INSERT INTO RetailersInfo (RetailerInfo, RetailerName, ContactNo, Address, Lisence_No, Retailer_pass)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """

                    values = (retailer_info, retailer_name, contact_no, address, license_no, Retailer_pass)
                    cursor.execute(insert_query, values)
                    conn.commit()

        print("Data inserted successfully")
    except FileNotFoundError:
        print(f"Error: The file {csv_file_name} does not exist")
    except Error as e:
        print(f"Error reading CSV file: {e}")
import os
import csv
import mysql.connector

# Establish your database connection here
# db_connection = mysql.connector.connect(...)
# cursor = db_connection.cursor()

def insert_into_product_listing():
    try:
        folder_path = r"C:\Users\Shlok Mehroliya\OneDrive\Documents\IIA Codes\wholesaler_csv"

        # Assuming WholesalerID starts at 1 and increments with each new CSV file
        current_wholesaler_id = 1

        # Process each CSV file in the directory
        for filename in os.listdir(folder_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(folder_path, filename)
                print("Processing file:", filename)

                with open(file_path, 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    next(csv_reader)  # Skip the header row

                    # Read and insert each row from the CSV file
                    for row in csv_reader:
                        if row and row != ['Product_ID', 'Product', 'Price_20kg', 'Stock']:
                            Product = row[1]
                            Stock = int(row[3])
                            Price_20kg = row[2]

                            # Prepare the insert statement with the current WholesalerID
                            
                            insert_query = "INSERT INTO ProductListing (WholesalerID, ProductName, Stock, Price, SourceFile) VALUES (%s, %s, %s, %s, %s)"
                            insert_data = (current_wholesaler_id, Product, Stock, Price_20kg, filename)
                            cursor.execute(insert_query, insert_data)
                        else:
                            # Skip the header if encountered again inside the CSV
                            continue

                print("Data insertion completed for file:", filename)
                # Increment the WholesalerID after each file is processed
                current_wholesaler_id += 1

        # Commit the transaction if all files processed without any error
        conn.commit()
        print("All data inserted successfully.")

    except Exception as e:
        # Rollback the transaction if any error occurs during the process
        conn.rollback()
        print("Error:", str(e))




def delete_csv_file_and_data(file_name):
    # Hardcoded folder path
    folder_path = r"C:\Users\Shlok Mehroliya\OneDrive\Documents\IIA Codes\wholesaler_csv"

    try:
        # First, delete associated data from the database
        delete_query = "DELETE FROM ProductListing WHERE SourceFile = %s"
        cursor.execute(delete_query, (file_name,))
        conn.commit()
        print(f"Data associated with {file_name} deleted from the database.")

        # Then, delete the file from the file system
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            os.remove(file_path)
            print(f"The file {file_name} has been deleted from the folder.")
        else:
            print("The file does not exist or is not a file.")

    except Exception as e:
        conn.rollback()
        print("Error:", str(e))


import os

def add_csv_file_data(file_name):
    try:
        folder_path = r"C:\Users\Shlok Mehroliya\OneDrive\Documents\IIA Codes\wholesaler_csv"
        file_path = os.path.join(folder_path, file_name)

        # Check if the specific file exists
        if not os.path.isfile(file_path):
            print(f"The file {file_name} does not exist.")
            return

        # Retrieve the current maximum WholesalerID
        cursor.execute("SELECT MAX(WholesalerID) FROM wholesalersinfo")
        result = cursor.fetchone()
        max_wholesaler_id_in_info = result[0]
        
        
        # Now check against the ProductListing for the next WholesalerID
        cursor.execute("SELECT MAX(WholesalerID) FROM ProductListing")
        result = cursor.fetchone()
        max_wholesaler_id_in_listing = result[0]

        # Determine the next WholesalerID to use
        current_wholesaler_id = max(max_wholesaler_id_in_info, max_wholesaler_id_in_listing)

        print("Processing file:", file_name)

        # Read the CSV file and insert the data into ProductListing

        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row

            # Read and insert each row from the CSV file
            for row in csv_reader:
                if row and row[0].lower().strip() != 'product_id':
                    Product = row[1]
                    Stock = int(row[3])
                    Price_20kg = row[2]


                    # Prepare the insert statement
                    insert_query = "INSERT INTO ProductListing (WholesalerID, ProductName, Stock, Price, SourceFile) VALUES (%s, %s, %s, %s, %s)"
                    insert_data = (current_wholesaler_id, Product, Stock, Price_20kg, file_name)
                    cursor.execute(insert_query, insert_data)

            print("Data insertion completed for file:", file_name)

        # Commit the transaction if all files processed without any error
        conn.commit()
        print("All data inserted successfully.")

    except Exception as e:
        # Rollback the transaction if any error occurs
        conn.rollback()
        print("Error:", str(e))


def delete_from_product_listing(listing_id):
    try:
        # Prepare the delete statement
        delete_query = "DELETE FROM ProductListing WHERE ListingID = %s"
        delete_data = (listing_id,)

        # Execute the delete statement
        cursor.execute(delete_query, delete_data)

        # Commit the transaction
        conn.commit()
        print(f"Product with ListingID {listing_id} deleted successfully.")

    except Exception as e:
        # Rollback the transaction if any error occurs
        conn.rollback()
        print("Error:", str(e))



def add_to_product_listing(wholesaler_id, product_name, stock, price):
    try:
        # Prepare the insert statement
        insert_query = "INSERT INTO ProductListing (WholesalerID, ProductName, Stock, Price) VALUES (%s, %s, %s, %s)"
        insert_data = (wholesaler_id, product_name, stock, price)

        # Execute the insert statement
        cursor.execute(insert_query, insert_data)

        # Commit the transaction
        conn.commit()
        print(f"Product {product_name} added successfully with WholesalerID {wholesaler_id}.")

    except Exception as e:
        # Rollback the transaction if any error occurs
        conn.rollback()
        print("Error:", str(e))



def read_last_transaction_id():

    # Fetch the last transaction ID from the Transactions table
    cursor.execute("SELECT MAX(TransID) FROM Transactions")
    result = cursor.fetchone()
    if result:
        last_transaction_id = result[0]

    return last_transaction_id

def insert_into_transactions():
    try:

        # Fetch the last transaction ID from the Transactions table
        trans_id = read_last_transaction_id()+1
        
        wholesaler_id = int(input("Enter wholesaler ID: "))
        retailer_id = int(input("Enter retailer ID: "))
        listing_id = int(input("Enter listing ID: "))
        quantity = int(input("Enter quantity: "))
        payment_method = input("Enter payment method: ")
        date = input("Enter date (YYYY-MM-DD): ")
        time = input("Enter time (HH:MM:SS): ")

        query = """
        
        INSERT INTO Transactions (TransID, WholesalerID, Retailer_ID, ListingID, Quantity, PaymentMethod, Date, Time)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (trans_id, wholesaler_id, retailer_id, listing_id, quantity, payment_method, date, time)
        cursor.execute(query, values)
        conn.commit()
        print("Data inserted successfully into Transactions")
    except Error as e:
        print(f"Error: {e}")
        conn.rollback()

def insert_into_transaction_csv():
    # Function to read data from CSV
    csv_input = input("Enter CSV file name: ")
    csv_file_name = csv_input + '.csv'
    try:
        with open(csv_file_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                    print(row)

                    trans_id = int(row['Transaction_ID'])
                    wholesaler_id = int(row['Wholesaler_ID'])
                    retailer_id = int(row['Retailer_ID'])
                    listing_id = int(row['Listing_ID'])
                    quantity = int(row['Quantity'])
                    payment_method = row['Payment']
                    date = row['Date']
                    time = row['Time']

                    query = """ Insert into Transactions (TransID, WholesalerID, Retailer_ID, ListingID, Quantity, PaymentMethod, Date, Time) Values (%s, %s, %s, %s, %s, %s, %s, %s)"""

                    values=(trans_id, wholesaler_id, retailer_id, listing_id, quantity, payment_method, date, time)
                    cursor.execute(query, values)
                    conn.commit()  


        print("Data inserted successfully")
    except FileNotFoundError:
        print(f"Error: The file {csv_file_name} does not exist")
    except Error as e:
        print(f"Error reading CSV file: {e}")

def menu():
    while True:
        print("\nMenu:")
        print("1: Insert into WholesalersInfo")
        print("2: Insert into RetailersInfo")
        print("3: Insert into ProductListing")
        print("4: Delete Product From ProductListing")
        print("5: Add Product to ProductListing")
        print("6: Remove entire dataSource from ProductListing")
        print("7: Add data from CSV file to ProductListing")
        print("8: Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            wholesaler_menu()
        elif choice == '2':
            print("\nRetailer Menu:")
            print("1: Input data manually")
            print("2: Read from existing CSV file")
            retailer_choice = input("Enter choice: ")
            if retailer_choice == '1':
                insert_into_retailers()
            elif retailer_choice == '2':
                insert_into_retailer_csv()
            else:
                print("Invalid choice, please choose again.")
        elif choice == '3':
            insert_into_product_listing()
        elif choice == '4':
           listing_id= int(input("Enter listing ID: "))
           delete_from_product_listing(listing_id)   
            
       
        elif choice == '5':
            print("\nProduct Menu:")
            wholesaler_id=int(input("1: Insert Product_id:"))
            product_name= input("2: Insert Product_Name:")
            stock=int(input("3: Insert Price:"))
            price=int(input("4: Insert Stock:"))
            add_to_product_listing(wholesaler_id, product_name, stock, price)
        elif choice == '6':
            file_name=input("Enter the name of the file to delete: ")
            delete_csv_file_and_data(file_name)
        elif choice == '7':
            file_name=input("Enter the name of the file to add: ")
            add_csv_file_data(file_name)
        elif choice == '8':
            break
        
        else:
            print("Invalid choice, please choose again.")

#menu()
def test():
    print("It works")


#print("Database connection closed")
def update_customer_catalogue():
    try:
            # Define and execute the SQL query  (SEMI JOIN)
            query = """
                INSERT INTO customer_catalogue (listing_id, current_wholesaler_id, Product, Stock, Price_20kg, rating)
                SELECT ListingID, WholesalerID, ProductName, Stock, Price, IFNULL(FLOOR(1 + RAND() * 5), 5)
                FROM ProductListing;
            """

            cursor.execute(query)

            # Commit the changes
            conn.commit()

            print("Data successfully inserted into customer_catalogue.")

    except mysql.connector.Error as err:
            conn.rollback()
            print(f"Error: {err}")
