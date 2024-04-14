from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("localhost", 27017)

# 下 show dbs 指令
query = "use demo;"
client.admin.command(query)

# 顯示所有的資料庫
client.list_database_names()

# create demo database


# Access the database
db = client["your_database_name"]


# Access the collection
collection = db["your_collection_name"]

# Retrieve data from the collection
data = collection.find()

# Print the retrieved data
for document in data:
    print(document)

# Close the connection
client.close()
