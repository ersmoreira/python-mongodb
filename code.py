import pymongo
import urllib
from pprint import pprint

password = 'adminpass'
dbase = ''


my_client = pymongo.MongoClient(
    "mongodb+srv://adminuser:admin1234@cluster0.9lnw1.mongodb.net/?retryWrites=true&w=majority")
my_db = my_client['sample_airbnb']
my_col = my_db['listingsAndReviews']

# houses = my_col.find({'accommodates': 5, 'beds': 3, 'property_type': 'House'})
# for house in houses:
#     pprint(house)

# first_filter = my_col.find_one({"_id": "10009999"})
# pprint(first_filter)
# my_col.update_one({"_id": "10009999"}, {'$set':{"accommodates": 6}})
# first_filter = my_col.find_one({"_id": "10009999"})
# pprint(first_filter)

newdoc = {
    "_id": '999999999',
    "accommodates": 2,
    "bedrooms": 1,
    "beds": 2
}
my_col.insert_one(newdoc)
my_doc = my_col.find_one({"_id": "999999999"})
pprint(my_doc)
