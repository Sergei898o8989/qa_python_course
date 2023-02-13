import csv
import json
from examples import CSV_FILE_PATH, JSON_FILE_PATH

# read books data from CSV
books = []
with open(CSV_FILE_PATH, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        books.append(row)

# read users data from JSON
with open(JSON_FILE_PATH, 'r') as jsonfile:
    users = json.load(jsonfile)

# distribute books among users
num_books = len(books)
num_users = len(users)
for i, user in enumerate(users):
    user_books = []
    for book in books[i * num_books // num_users:(i + 1) * num_books // num_users]:
        user_book = {
            "title": book.get("Title", ""),
            "author": book.get("Author", ""),
            "pages": int(book.get("Pages", 0)),
            "genre": book.get("Genre", ""),
        }
        user_books.append(user_book)
    user["books"] = user_books
    user.pop("_id", None)
    user.pop("index", None)
    user.pop("guid", None)
    user.pop("isActive", None)
    user.pop("balance", None)
    user.pop("picture", None)
    user.pop("company", None)
    user.pop("email", None)
    user.pop("phone", None)
    user.pop("about", None)
    user.pop("registered", None)
    user.pop("latitude", None)
    user.pop("longitude", None)
    user.pop("tags", None)
    user.pop("friends", None)
    user.pop("greeting", None)
    user.pop("favoriteFruit", None)
    user.pop("eyeColor", None)

    user["books"] = books[i * num_books // num_users:(i + 1) * num_books // num_users]

# write result to JSON file
with open("result.json", "w") as jsonfile:
    json.dump(users, jsonfile, indent=4)
