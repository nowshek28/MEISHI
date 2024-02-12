import pymongo

class MongoDBHandler:
    def __init__(self, database_name, collection_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def upload_data(self, data):
        # Insert data into the collection
        self.collection.insert_many(data)

    def read_data(self):
        # Query the collection to retrieve the data
        return self.collection.find()

# Example usage
if __name__ == "__main__":
    # Sample data list
    data = [
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "San Francisco"},
        {"name": "Charlie", "age": 35, "city": "Los Angeles"}
    ]

    # Create an instance of the MongoDBHandler class
    handler = MongoDBHandler(database_name="mydatabase", collection_name="mycollection")

    # Call the upload_data method to upload the data
    handler.upload_data(data)

    # Call the read_data method to retrieve and print the data
    for data in handler.read_data():
        print(data)