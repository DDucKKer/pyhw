import pymongo
from config import USER, PASSWORD

url = f'mongodb+srv://{USER}:{PASSWORD}@cluster0.uqg8qz6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = pymongo.MongoClient(url)
client.drop_database('books')

db = client.books
fantasy_coll = db.fantasy
school_literature_coll = db.school_literature

fantasy_coll.insert_one(
    {'title': 'Гра престолів', 'price': 200, 'year': 2015, 'number_of_pages': 500}
)

school_literature_books = [
    {'title': 'Історія України', 'class': 9, 'number_of_pages': 320, 'year': 2021},
    {'title': 'Математика. Алгебра та геометрія', 'class': 10, 'number_of_pages': 450, 'year': 2020},
    {'title': 'Українська література', 'class': 11, 'number_of_pages': 370, 'year': 2019},
    {'title': 'Фізика', 'class': 8, 'number_of_pages': 400, 'year': 2018},
    {'title': 'Біологія', 'class': 7, 'number_of_pages': 350, 'year': 2022}
]
school_literature_coll.insert_many(school_literature_books)

history_book = school_literature_coll.find_one({'title': {'$regex': '.*історія.*', '$options': 'i'}})
print('Книга зі словом "історія" в назві:', history_book)

fantasy_coll.update_one({'title': 'Гра престолів'}, {'$inc': {'price': 56}})
updated_game_of_thrones = fantasy_coll.find_one({'title': 'Гра престолів'})
print('Оновлена книга "Гра престолів":', updated_game_of_thrones)

fantasy_coll.delete_one({'title': 'Гра престолів'})
deleted_game_of_thrones = fantasy_coll.find_one({'title': 'Гра престолів'})
print('Перевірка видалення книги "Гра престолів":', deleted_game_of_thrones)

school_literature_coll.delete_many({'year': {'$lt': 2020}})
remaining_books = list(school_literature_coll.find())
print('Книги, які залишилися після видалення:', remaining_books)

# GET DATA *************************************************
# first
# result = mops_coll.find_one()
# result = mops_coll.find_one({'_id': 10})  # by field
# result = mops_coll.find_one({'price': 18})  # by field
# print(result)


# all data
# result = mops_coll.find()
# print(result)
# for doc in result:
#       print(doc)

# looking for the specific field
# query = {'price': 22}
# query = {'price': {'$gt': 15}}
# query = {'title': {'$regex': 'Su*'}}
# query = {'title': {'$regex': r'er22\b'}}
# query = {'title': {'$regex': r'er\b'}, 'price': {'$gte': 15}}
# query = {'title': {'$regex': r'er\b'}, 'price': {'$lte': 15}}

# result = mops_coll.find(query)
# result = mops_coll.find(query).limit(2)
# result = mops_coll.find(query).sort('price').limit(2)
# result = mops_coll.find(query).sort('price', -1).limit(25)
# for doc in result:
#       print(doc)

# UPDATE
#  use $set
# current = {'title': 'Super2 mop'}
# new_data = {'$set': {'brand': 'Samsung2'}}
# data = mops_coll.update_one(current, new_data)
# print(data.raw_result)

# current = {'title': 'Super mop3'}
# new_data = {'$set': {'battery_capacity': 10000}}
# data = mops_coll.update_many(current, new_data)
# print(data.raw_result)

# current = {}
# new_data = {'$set': {'warranty': 3}}
# data = mops_coll.update_many(current, new_data)
# print(data.raw_result)


# multiplication
# query = {}
# # operation = {'$mul': {'price': 1.1}}  # bad idea
# operation = {'$mul': {'price': Decimal128(str(2))}}
# data = mops_coll.update_many(query, operation)
# print(data.raw_result)

# increase
# query = {'price': {'$lt': 350}}
# operation = {'$inc': {'warranty': -1, 'price': 300}}
# data = mops_coll.update_many(query, operation)
# print(data.raw_result)

# DELETE field
# query = {'price': {'$lt': 370}}
# operation = {'$unset': {'warranty': 1}}
# data = mops_coll.update_many(query, operation)
# print(data.raw_result)

# DELETE document
# query = {'price': {'$lt': 370}}
# data = mops_coll.delete_one(query)
# print(data.raw_result)

# query = {}
# data = mops_coll.delete_many(query)
# print(data.deleted_count)


# mops_coll.drop()
# vacuum_cleaners_coll.drop()
