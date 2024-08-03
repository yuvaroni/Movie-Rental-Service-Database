from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['movie_rental_service']

def find_movies_by_genre(genre):

    movies = db.movies.find({"genre": genre})
    return list(movies)

def list_customers_who_rented_movies():

    rental_customer_ids = db.rentals.distinct("customer_id")
    customers = db.customers.find({"_id": {"$in": rental_customer_ids}})
    return list(customers)

def find_rentals_by_customer(customer_id):

    rentals = db.rentals.find({"customer_id": ObjectId(customer_id)})
    return list(rentals)

def find_movies_with_available_copies(min_copies=1):

    movies = db.movies.find({"available_copies": {"$gte": min_copies}})
    return list(movies)

def count_rentals_by_movie():

    pipeline = [
        {
            "$group": {
                "_id": "$movie_id",
                "rental_count": {"$sum": 1}
            }
        },
        {
            "$lookup": {
                "from": "movies",
                "localField": "_id",
                "foreignField": "_id",
                "as": "movie"
            }
        },
        {
            "$unwind": "$movie"
        },
        {
            "$project": {
                "_id": 0,
                "movie_title": "$movie.title",
                "rental_count": 1
            }
        }
    ]
    rental_counts = list(db.rentals.aggregate(pipeline))
    return rental_counts

def list_movies_with_ids():

    movies = db.movies.find({}, {"_id": 1, "title": 1})
    movie_list = [{"_id": str(movie["_id"]), "title": movie["title"]} for movie in movies]
    return movie_list

# Example usage:

# 1. Find movies by genre (e.g., "Sci-Fi")
sci_fi_movies = find_movies_by_genre("Sci-Fi")
print("Sci-Fi Movies:")
for movie in sci_fi_movies:
    print(movie)

# 2. List all customers who have rented movies
customers_who_rented = list_customers_who_rented_movies()
print("Customers Who Rented Movies:")
for customer in customers_who_rented:
    print(customer)

# 3. Find all rentals for a specific customer (replace 'example_customer_id' with an actual ObjectId from your database)
example_customer_id = "60d5f9f4d3b2c4a5d4e7b0c9"  # Replace with an actual ObjectId from your customers collection
customer_rentals = find_rentals_by_customer(example_customer_id)
print(f"Rentals for Customer ID {example_customer_id}:")
for rental in customer_rentals:
    print(rental)

# 4. Find movies with at least 1 available copies
movies_with_copies = find_movies_with_available_copies(1)
print("Movies with at least 1 available copies:")
for movie in movies_with_copies:
    print(movie)

# 5. Count the number of rentals for each movie
rental_counts = count_rentals_by_movie()
print("Number of Rentals by Movie:")
for count in rental_counts:
    print(f"{count['movie_title']}: {count['rental_count']} rentals")

# 6. List all movies with their IDs
movies_with_ids = list_movies_with_ids()
print("Movies and their IDs:")
for movie in movies_with_ids:
    print(f"ID: {movie['_id']}, Title: {movie['title']}")
