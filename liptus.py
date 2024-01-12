from etl import *

def liptus_logic(retail_no,prod_to_review,product_name,review):
    
     #user,prod_to_review,product_name,review
    
    not_word=["not"]
    positive_review = [
    "ripe",
    "crisp",
    "juicy",
    "sweet",
    "nutrient-rich",
    "vibrant",
    "delicious",
    "wholesome",
    "organic",
    "succulent",
    "flavorful",
    "healthy",
    "plump",
    "colorful",
    "nourishing",
    "refreshing",
    "tasty",
    "fresh",
    "fragrant",
    "luscious",
    "mouth-watering",
    "good",
    ]
    negative_review = [
    "moldy",
    "spoiled",
    "rotten",
    "decayed",
    "mushy",
    "fermented",
    "discolored",
    "putrid",
    "moldy",
    "sour",
    "smelly",
    "slimy",
    "mushy",
    "off",
    "foul",
    "stale",
    "inedible",
    "rancid",
    "mold-covered",
    "infested"
    ]
    positive_adverbs = [
    "very",
    "extremely",
    "incredibly",
    "exceptionally",
    "remarkably",
    "exceedingly",
    "intensely",
    "outstandingly",
    "amazingly",
    "exquisitely",
    "fantastically",
    "splendidly",
    "wonderfully",
    "positively",
    "superbly",
    "marvelously",
    "phenomenally",
    "brilliantly",
    "exuberantly",
    "impressively"
    ]
    negative_adverbs = [
    "very",
    "extremely",
    "incredibly",
    "unbelievably",
    "exceptionally",
    "alarmingly",
    "dreadfully",
    "terribly",
    "horribly",
    "awfully",
    "appallingly",
    "disastrously",
    "atrociously",
    "disgustingly",
    "abominably",
    "dismally",
    "deplorably",
    "painfully",
    "distressingly",
    "unpleasantly",
]


    rating=0
    words=review.split()
    for word in words:
        if word in positive_review and positive_adverbs: #very good apple
            rating=5
        elif word in not_word and positive_review: #not good apple
            rating=2
        elif word in positive_adverbs and negative_review: #very bad apple
            rating=2
        elif word in not_word and negative_review: #not bad apple
            rating=3
        elif word in negative_review and negative_adverbs: #very bad apple
            rating=1
        elif word in positive_review: #good apple
            rating=4
        elif word in negative_review: #bad apple
            rating=2
        else:
            continue


    query = "SELECT * FROM customer_catalogue;"
    cursor.execute(query)
    customer_catalogue_info = cursor.fetchall()
    for row in customer_catalogue_info:
        if row[0]==prod_to_review:
            rating=(rating+row[5])/2
            query = "UPDATE customer_catalogue SET rating = %s WHERE listing_id = %s;"
            cursor.execute(query, (rating,prod_to_review))
            conn.commit()
    print("Rating updated")


    try:
        conn_review = mysql.connector.connect(**db_config_review)
        cursor_review = conn_review.cursor()

        query = "INSERT INTO FEEDBACK (listing_id, retailer_no, product_name, Rating, Review) VALUES (%s, %s, %s, %s, %s)"
        cursor_review.execute(query, (prod_to_review, retail_no, product_name, rating, review))

        # Commit the changes to the database using the connection object, not the cursor
        conn_review.commit()
        print("Review stored")

    except Error as e:
        print(f"Error: {e}")
        # Rollback the transaction in case of an error
        conn_review.rollback()



def liptus():
    
    print("Thank you for for sharing your feedback,please login to view which product you would like to review")
   
    retail_no=int(input("Enter your retailer infonumber :"))
   
    query = "SELECT * FROM customer_purchase_history;"
    cursor.execute(query)
    retailerinfo_rows = cursor.fetchall()
    sno=1
    i=0
    print("Sno,purchase_id, retailerInfo, prod_name, listing_id, wholesaler_id, quantity, price")
    for row in retailerinfo_rows:
        #print("row",row[3])
        
        
        if row[1]==retail_no:
            print(sno,")",row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            sno+=1
        
    
    prod_to_review=int(input("Enter the Listing id of the product you would like to review:"))
    for row in retailerinfo_rows:
        if prod_to_review==row[3]:
            product_name=row[2]
            print(product_name)
            print("You will be writing a review on",row[2])
            print("Enter your review")
            review=input()
            print("Thank you for your review")
            break
    liptus_logic(retail_no,prod_to_review,product_name,review)
    #liptus_logic(review,user,user,product_name)
    #liptus_logic(retail_no,prod_to_review,product_name,review)
    

 


    


    
#liptus()



