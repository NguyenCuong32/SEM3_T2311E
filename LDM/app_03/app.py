from pymongo import MongoClient


connetion_string ="mongodb+srv://cuongnx:ODfHFuBZ08zmP0YG@mongocluster.0sn5a89.mongodb.net/"
database_name ="sample_mflix"
collection_user ="users"
collection_movie ="movies"

client = MongoClient(connetion_string)
db = client[database_name]

col_users = db[collection_user]
col_movie = db[collection_movie]
def aggregation_match(email):
    match_by_email = {"$match":{"email":email}}
    match_by_user = {"$match":{"email":email}}
    match_pipline = [match_by_email]
    results = col_users.aggregate(match_pipline)
    if results !=None:
        for user in results:
            print(user["name"])
            print(user["email"])
            print(user["password"])

def aggregation_movies(type, year):
    match_by_type = {"$match":{"type":type}}
    match_by_year = {"$match": {"year": {"$gt": year}}}

    match_pipline = [match_by_type,match_by_year]
    results = col_movie.aggregate(match_pipline)
    if results !=None:
        for mv in results:
            print(mv["title"])
            print(mv["type"])
            print(mv["year"])

def menu():
    print("Demo Aggregation")
    while True:
        choice = input("Please enter a number: ")
        if choice == '1':
            print("Demo match")
            email = input("Please enter an email: ")
            aggregation_match(email)
        if choice == '2':
            print("Demo match")
            type = input("Please enter an type: ")
            year = int(input("Please year: "))
            aggregation_movies(type,year)

if __name__ == "__main__":
    menu()