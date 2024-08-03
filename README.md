# Movie Rental Service

This is a backend project for managing a movie rental service, demonstrating database structure and queries using MongoDB. The project includes functionalities for managing movies, customers, and rentals. It supports both local and remote MongoDB connections.

## Features

- **Movie Management**: Insert movies with details such as title, genre, total copies, and available copies.
- **Customer Management**: Insert customer details including name, email, and phone number.
- **Rental Management**: Track movie rentals with rental status and automatic updates to the number of available copies.
- **Query Examples**: Various database queries including finding movies by genre, listing customers who have rented movies, counting rentals by movie, and more.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/movie-rental-service.git
    cd movie-rental-service
    ```

2. **Install the required Python packages:**

    ```bash
    pip install pymongo
    ```

3. **Set up your MongoDB connection:**

   - **For localhost:**
    ```python
    client = MongoClient('mongodb://localhost:27017/')
    db = client['your_database_name']
    ```

   - **For a remote database with a connection string:**
    ```python
     client = MongoClient(connection_string)
    # Replace 'your_database_name' with the name of your database
    db = client['your_database_name']
    ```

## Usage

1. **Insert sample data into the database:**

    ```bash
    python insert_data.py
    ```

    This script inserts sample movies, customers, and rental records into the database.

2. **Update the rental status of a movie:**

    ```bash
    python update_rental_status.py
    ```

    Modify the script to specify the `rental_id` and `new_status` as needed.

3. **Run query examples:**

    ```bash
    python query_examples.py
    ```

    This script demonstrates various database queries, including:
    - Finding movies by genre
    - Listing customers who have rented movies
    - Finding all rentals for a specific customer
    - Finding movies with available copies
    - Counting the number of rentals for each movie
    - Listing all movies with their IDs

## Query Examples

### Find Movies by Genre

```python
sci_fi_movies = find_movies_by_genre("Sci-Fi")
print("Sci-Fi Movies:")
for movie in sci_fi_movies:
    print(movie)
```

### List Customers Who Rented Movies

```python
customers_who_rented = list_customers_who_rented_movies()
print("Customers Who Rented Movies:")
for customer in customers_who_rented:
    print(customer)
```

### Find Rentals by Customer

```python
example_customer_id = "60d5f9f4d3b2c4a5d4e7b0c9"  # Replace with an actual ObjectId from your customers collection
customer_rentals = find_rentals_by_customer(example_customer_id)
print(f"Rentals for Customer ID {example_customer_id}:")
for rental in customer_rentals:
    print(rental)
```

### Find Movies with Available Copies

```python
movies_with_copies = find_movies_with_available_copies(1)
print("Movies with at least 1 available copies:")
for movie in movies_with_copies:
    print(movie)
```

### Count Rentals by Movie

```python
rental_counts = count_rentals_by_movie()
print("Number of Rentals by Movie:")
for count in rental_counts:
    print(f"{count['movie_title']}: {count['rental_count']} rentals")
```
### List All Movies with Their IDs

```python
movies_with_ids = list_movies_with_ids()
print("Movies and their IDs:")
for movie in movies_with_ids:
    print(f"ID: {movie['_id']}, Title: {movie['title']}")
```
