
from bson import ObjectId
from datetime import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['movie_rental_service']


def update_rental_status(rental_doc_id, new_status):

    rental_doc = db.rentals.find_one({"_id": rental_doc_id})

    if rental_doc:
        # Update the rental status
        db.rentals.update_one(
            {"_id": rental_doc_id},
            {"$set": {
                "status": new_status,
                "return_date": datetime.now() if new_status == "returned" else None
            }}
        )


        if new_status == "rented":
            db.movies.update_one(
                {"_id": rental_doc["movie_id"]},
                {"$inc": {"available_copies": -1}}
            )
        elif new_status == "returned":
            db.movies.update_one(
                {"_id": rental_doc["movie_id"]},
                {"$inc": {"available_copies": 1}}
            )

        print(f"Rental status updated to '{new_status}' and available copies adjusted.")
    else:
        print("Rental not found.")




example_rental_doc_id = ObjectId(
    "66a91d51d3e52e83a0dc5f30")  # Replace with an actual ObjectId from your rentals collection
update_rental_status(example_rental_doc_id, "returned")
