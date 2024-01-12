
from etl import *
from retailers import *
from liptus import *
from collections import Counter


def show_menu():
    print("Welcome to FreshLink, your one-stop shop for fresh fruits and vegetables;how would you like to proceed?")
    print("1. Admin")
    print("2. Wholesaler")
    print("3. Retailer/Customer")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
       # print("Admin Menu")
        admin_menu()
    elif choice == '2':
        #print("Wholesaler Menu")
        wholesaler_menu()
    elif choice == '3':
        #print("Retailer/Customer Menu")
        retailer_menu()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

def admin_menu():
    print("Please Login")
    user=input("Enter your admin ID:")
    password=input("Enter your admin password:")
    if user=="admin" and password=="admin":
        print("Login Successful")
        admin_capabilities()      
    else:
        print("Login Unsuccessful")
        show_menu()
        


#####################################################################################################################

def wholesaler_menu():
    print("Wholesaler Menu")
    print("1.Login")
    print("2.Register")
    print("3.Exit")
    choice=input("Enter your choice:")
    if choice == '1':
        user=int(input("Enter your wholesaler ID:"))
        password=input("Enter your password:")
        query = "SELECT password FROM WholesalersInfo WHERE WholesalerID = %s"
        cursor.execute(query, (user,))
        password_database = cursor.fetchone()[0]


        if password==password_database:
            print("Login Successful")
            
            wholesaler_capabilities()   

        else:
            print("Login Unsuccessful")
            wholesaler_menu()
        
    elif choice == '2':
        try:
            print("Register")
            wholesaler_name=input("Enter Business Name:")
            wholesaler_password=input("Enter password:")
            wholesaler_license=input("Enter license ID:")
            wholesaler_Contact=input("Enter Contact Number:")
            wholesaler_state=input("Enter State:")

            query = "SELECT WholesalerID FROM wholesalersInfo ORDER BY WholesalerID DESC LIMIT 1"
            cursor.execute(query)
            wholesaler_ID = cursor.fetchone()[0] + 1

            query = "INSERT INTO wholesalersInfo VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (wholesaler_ID, wholesaler_name, wholesaler_Contact, wholesaler_state, wholesaler_license, wholesaler_password))

            conn.commit()
            print("Data inserted successfully into WholesalersInfo")

        except Error as e:
            print(f"Error: {e}")
            conn.rollback()
    elif choice == '3':
        #print("Thank you for Visiting")
        show_menu()
    

def wholesaler_capabilities():

    while True:

        print("Please select what you would like to do")
        print("1. Add new products to ProductListing")
        print("2. Remove entire dataSource from ProductListing")
        print("3. Add data from CSV file to ProductListing")
        print("4. Delete Product from ProductListing")
        print("5. Exit")

        choice=input("Enter your choice:")
        if choice == '1':
            print("\nProduct Menu:")
            wholesaler_id=int(input("1: Insert wholesaler_ID:"))
            product_name= input("2: Insert Product_Name:")
            stock=int(input("3: Insert Price:"))
            price=int(input("4: Insert Stock:"))
            add_to_product_listing(wholesaler_id, product_name, stock, price)
        elif choice == '2':
            file_name=input("Enter the name of the file to delete: ")
            delete_csv_file_and_data(file_name)
        elif choice == '3':
            file_name=input("Enter the name of the file to add: ")
            add_csv_file_data(file_name)
        elif choice == '4':
            listing_id= int(input("Enter listing ID: "))
            delete_from_product_listing(listing_id)
        elif choice == '5':
            show_menu()
            




        

        
#####################################################################################################################
def retailer_menu():
    print("Retailer Menu")
    print("1.Login")
    print("2.Register")
    print("3.Leave a Review")
    print("4.Go Back")
    choice=input("Enter your choice:")
    if choice == '1':
        user=int(input("Enter your retailer User code:"))
        password=int(input("Enter your password:"))
        query = "SELECT Retailer_pass FROM RetailersInfo WHERE RetailerInfo = %s"
        cursor.execute(query, (user,))
        password_database = cursor.fetchone()[0]
        if password==password_database:
            print("Login Successful")
            Retailer_catalogue(user)
        else:
            print("Login Unsuccessful")
            retailer_menu()

    elif  choice == '2':

            print("Register")
            retailer_id = input("Enter Retailer ID: ")
            retailer_name = input("Enter Retailer Name: ")
            retailer_phone = input("Contact_No: ")
            retailer_address = input("Location: ")
            retailer_lisence = input("Enter your License Number: ")
            retailer_password = input("Enter your password:")

            csv_data = {
                "Retailer_ID": retailer_id,
                'Retailer_Name': retailer_name,
                "Contact_No": retailer_phone,
                "Location": retailer_address,
                "Lisence_No": retailer_lisence,
                "Retailer_pass": retailer_password
            }

            csv_file = r"C:\Users\Shlok Mehroliya\OneDrive\Documents\IIA Codes\retailers.csv"

            # Append data to CSV file
            with open(csv_file, mode='a', newline='') as file:
                fieldnames = ['Retailer_ID', 'Retailer_Name', 'Contact_No', "Location", "Lisence_No", 'Retailer_pass']
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                # Check if the file is empty, and write the header if needed
                if file.tell() == 0:
                    writer.writeheader()

                # Write the new row
                writer.writerow(csv_data)

                print(f"Data appended to {csv_file}.")
        

    elif choice == '3':
            liptus()      
    elif choice == '4':
            print("Thank you for Visiting")
            show_menu()

    else:
        print("Please enter a valid choice")
        show_menu()


def Retailer_catalogue(user):
    print("Catalogue")
    print("1. View Catalogue")
    print("2. Looking for something specific? Search Catalogue")
    print("3. Exit")
    choice=input("Enter your choice:")
    if choice == '1':
        print("View Catalogue")
        View_Catalogue(user)
    elif choice == '2':
        search_catalogue(user)
        #print("Search Catalogue")
    elif choice == '3':
        print("Thank you for Visiting")
        show_menu()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")





def View_Catalogue(user):

    try:
        # Define and execute the SQL query  (SEMI JOIN)
        query = """
                SELECT pl.ListingID, pl.ProductName, pl.Price, cc.rating
                FROM ProductListing pl
                JOIN customer_catalogue cc ON pl.ListingID = cc.listing_id;
                """
            
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()
        


        # Print the catalog
        if not rows:
            print("Catalog is empty.")
        else:
            print("Catalog:")
            for row in rows:
                ListingID, ProductName, Price, rating = row
                print(f"ListingID: {ListingID} ProductName: {ProductName} Price/20kg: {Price} Rating: {rating}")

        input_str = input("Enter space-separated listing ID of all the products you want to purchase: ")
        integer_list = list(map(int, input_str.split()))

        total_bill = 0

        for listing_id in integer_list:
            query = "SELECT Price_20kg FROM customer_catalogue WHERE listing_id = %s;"
            cursor.execute(query, (listing_id,))
            price = cursor.fetchone()[0]
            total_bill += price
        

        print(f"Total bill: {total_bill}")

        print("Do you want to proceed with the purchase?")
        print("1. Yes")
        print("2. No")
        choice=input("Enter your choice:")
        if choice == 'Yes':
            print("Thank you for your purchase")
            for listing_id in integer_list:
                query = "SELECT Stock FROM customer_catalogue WHERE listing_id = %s;"
                cursor.execute(query, (listing_id,))
                stock = cursor.fetchone()[0]
                stock -= 1
                query = "UPDATE customer_catalogue SET Stock = %s WHERE listing_id = %s;"
                cursor.execute(query, (stock, listing_id))


                query_2 = "SELECT Stock FROM ProductListing WHERE ListingID = %s;"
                cursor.execute(query_2, (listing_id,))
                stock_2 = cursor.fetchone()[0]
                stock_2 -= 1
                query_2 = "UPDATE ProductListing SET Stock = %s WHERE ListingID = %s;"
                cursor.execute(query_2, (stock_2, listing_id))
                            
            conn.commit()
            customer_cart(integer_list,user)
            print("Data inserted successfully into customer_purchase_history")

        elif choice == 'No':
            print("Thank you for Visiting")
            Retailer_catalogue(user)

    except mysql.connector.Error as err:
        conn.rollback()
        print(f"Error: {err}")

#####################################################################################################################

def admin_capabilities():
    print("Please select what you would like to do")
    print("1. Remove wholesaler dataSource from ProductListing")
    print("2. Add new wholesaler products DB to ProductListing")
    print("3. View Transcations on Site ")
    print("4. View Feedback")
    print("5. Exit")
    choice=input("Enter your choice:")
    if choice == '1':
        file_name=input("Enter the name of the file to delete: ")
        delete_csv_file_and_data(file_name)
    elif choice == '2':
        file_name=input("Enter the name of the file to add: ")
        add_csv_file_data(file_name)
    elif choice == '3':
        query="SELECT * FROM customer_purchase_history"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    elif choice == '4':
        conn_review = mysql.connector.connect(**db_config_review)
        cursor_review = conn_review.cursor()
        query='Select * from FEEDBACK'
        cursor_review.execute(query)
        rows = cursor_review.fetchall()
        for row in rows:
            print(row)
       
    elif choice == '5':
        print("Thank you for Visiting")
        show_menu()
        
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        
#####################################################################################################################

def customer_cart(list,user):
    
    try:

            #print(user)
        listing_id_counts = Counter(list)

        for listing_id, count in listing_id_counts.items():
            # Define and execute the SQL query for each unique listing_id
            query = f"""
                INSERT INTO customer_purchase_history (purchase_id, retailerInfo, prod_name, listing_id, wholesaler_id, stock, price)
                SELECT
                    NULL,
                    '{user}',
                    Product,
                    {listing_id},
                    current_wholesaler_id,
                    {count},  -- Use the count as the aggregated stock/quantity
                    Price_20kg
                FROM customer_catalogue
                WHERE listing_id = {listing_id};
            """
            cursor.execute(query)

        conn.commit()

    except mysql.connector.Error as err:
        conn.rollback()
        print(f"Error: {err}")
       

        

#####################################################################################################################
def search_catalogue(user):
    try:
        print(user)
        name=input("Enter the name of the product you are looking for:")
        quantity=int(input("Enter the quantity you are looking for in terms of /20Kg:"))
        range_start=int(input("Enter the minimum price you are looking for:"))
        range_end=int(input("Enter the maximum price you are looking for:"))

        query = f"""
        select * from customer_catalogue where Product like '%{name}%' and Price_20kg between {range_start} and {range_end} and Stock>={quantity};


                """
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
           # ListingID, ProductName, Price, rating = row
            #print(f"ListingID: {ListingID} ProductName: {ProductName} Price/20kg: {Price} Rating: {rating}")
        input_str = input("Enter space-separated listing ID of all the products you want to purchase: ")
        integer_list = list(map(int, input_str.split()))

        total_bill = 0

        for listing_id in integer_list:
                query = "SELECT Price_20kg FROM customer_catalogue WHERE listing_id = %s;"
                cursor.execute(query, (listing_id,))
                price = cursor.fetchone()[0]
                total_bill += price
            

        print(f"Total bill: {total_bill}")

        print("Do you want to proceed with the purchase?")
        print("1. Yes")
        print("2. No")
        choice=input("Enter your choice:")
        if choice == 'Yes':
            print("Thank you for your purchase")
            for listing_id in integer_list:
                query = "SELECT Stock FROM customer_catalogue WHERE listing_id = %s;"
                cursor.execute(query, (listing_id,))
                stock = cursor.fetchone()[0]
                stock -= 1
                query = "UPDATE customer_catalogue SET Stock = %s WHERE listing_id = %s;"
                cursor.execute(query, (stock, listing_id))


                query_2 = "SELECT Stock FROM ProductListing WHERE ListingID = %s;"
                cursor.execute(query_2, (listing_id,))
                stock_2 = cursor.fetchone()[0]
                stock_2 -= 1
                query_2 = "UPDATE ProductListing SET Stock = %s WHERE ListingID = %s;"
                cursor.execute(query_2, (stock_2, listing_id))
                            
            conn.commit()
            customer_cart(integer_list,user)
            print("Data inserted successfully into customer_purchase_history")

        elif choice == 'No':
            print("Thank you for Visiting")
            Retailer_catalogue(user)

    except mysql.connector.Error as err:
        conn.rollback()
        print(f"Error: {err}")
    #print("Search Catalogue")
show_menu()