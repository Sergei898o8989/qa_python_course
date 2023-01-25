import csv
import json
import os

CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), 'examples', 'books.csv')
JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), 'examples', 'users.json')
RESULT_JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), 'result.json')

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
    user["books"] = books[i * num_books // num_users:(i + 1) * num_books // num_users]

# write result to JSON file
with open("result.json", "w") as jsonfile:
    json.dump(users, jsonfile, indent=4)
