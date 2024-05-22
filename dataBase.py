from pymongo import MongoClient
def connectDB(user, password, data):
    # Replace the uri string with your MongoDB deployment's connection string.
    client = MongoClient(f'mongodb+srv://{user}:{password}@mernapp.fog5yml.mongodb.net/?retryWrites=true&w=majority&appName=MERNapp')

    # Connect to the database (will be created if it doesn't exist)
    db = client['CARDdata']

    # Create a new collection (will be created if it doesn't exist)
    collection = db['info']

    # Insert a document into the collection
    collection.insert_one(data)

    print("Database and collection created successfully")


if __name__ == "__main__":
    data = {
        'NAME': 'E-mail:abhishekameta',
        'COMPANY': 'SantecAocCorporation',
        'COMAPANY GROUP': 'Factory Autonation Group',
        'ADDRESS': 'KomakiAichi485-0802,jAPAN',
        'PHONE': ', Mobile:+81-70-1438-1567, Mobile:+81-70-1438-1567, Tel:+81-568-79-3535, Fax:+81-568-79-3549',
        'EMAIL': 'E-mail:abhishekameta@santeccom',
        'WEBSITE': 'www.santececom',
        'Description': ' santec Photonics Valley Ohkusa Campus Abhishek Ameta 5823 Ohkusa-Nenjozaka'
        }

    connectDB('meishi', 'Database', data)