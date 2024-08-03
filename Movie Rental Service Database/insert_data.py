from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')

db = client['movie_rental_service']

movies = [
    {
        "title": "Inception",
        "genre": "Sci-Fi",
        "release_year": 2010,
        "available_copies": 5
    },
    {
        "title": "The Dark Knight",
        "genre": "Action",
        "release_year": 2008,
        "available_copies": 3
    },
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "release_year": 2014,
        "available_copies": 4
    },
    {
        "title": "The Matrix",
        "genre": "Sci-Fi",
        "release_year": 1999,
        "available_copies": 2
    },
    {
        "title": "Gladiator",
        "genre": "Action",
        "release_year": 2000,
        "available_copies": 1
    },
    {
        "title": "Titanic",
        "genre": "Romance",
        "release_year": 1997,
        "available_copies": 3
    }
]


customers = [
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "membership_start_date": "2022-01-01"
    },
    {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "membership_start_date": "2023-03-15"
    },
    {
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com",
        "membership_start_date": "2022-05-20"
    },
    {
        "name": "Bob Brown", "email": "bob.brown@example.com",
        "membership_start_date": "2023-01-10"
    },
    {
        "name": "Charlie Davis",
        "email": "charlie.davis@example.com",
        "membership_start_date": "2022-12-25"
    },
    {
        "name": "Diana Evans",
        "email": "diana.evans@example.com",
        "membership_start_date": "2023-06-30"
    }
]

rentals = [
    {
        "customer_id": None,
        "movie_id": None,
        "rental_date": datetime.strptime("2023-07-01", "%Y-%m-%d"),
        "return_date": datetime.strptime("2023-07-10", "%Y-%m-%d"),
        "status": "returned"
    },
    {
        "customer_id": None,
        "movie_id": None,
        "rental_date": datetime.strptime("2023-07-20", "%Y-%m-%d"),
        "return_date": None,
        "status": "rented"
    },
    {
        "customer_id": None,
        "movie_id": None,
        "rental_date": datetime.strptime("2023-07-15", "%Y-%m-%d"),
        "return_date": datetime.strptime("2023-07-22", "%Y-%m-%d"),
        "status": "returned"
    },
    {
        "customer_id": None,
        "movie_id": None,
        "rental_date": datetime.strptime("2023-07-18", "%Y-%m-%d"),
        "return_date": datetime.strptime("2023-07-25", "%Y-%m-%d"),
        "status": "returned"
    },
    {
        "customer_id": None,
        "movie_id": None,
        "rental_date": datetime.strptime("2023-07-10", "%Y-%m-%d"),
        "return_date": datetime.strptime("2023-07-17", "%Y-%m-%d"),
        "status": "returned"
    },
    {
        "customer_id": None,
        "movie_id": None,
        "rental_date": datetime.strptime("2023-07-05", "%Y-%m-%d"),
        "return_date": None,
        "status": "rented"
    }
]


movie_ids = db.movies.insert_many(movies).inserted_ids


customer_ids = db.customers.insert_many(customers).inserted_ids


rentals[0]['customer_id'] = customer_ids[0]
rentals[0]['movie_id'] = movie_ids[0]
rentals[1]['customer_id'] = customer_ids[1]
rentals[1]['movie_id'] = movie_ids[1]
rentals[2]['customer_id'] = customer_ids[2]
rentals[2]['movie_id'] = movie_ids[2]
rentals[3]['customer_id'] = customer_ids[3]
rentals[3]['movie_id'] = movie_ids[3]
rentals[4]['customer_id'] = customer_ids[4]
rentals[4]['movie_id'] = movie_ids[4]
rentals[5]['customer_id'] = customer_ids[5]
rentals[5]['movie_id'] = movie_ids[5]


db.rentals.insert_many(rentals)

print("Data inserted successfully!")
