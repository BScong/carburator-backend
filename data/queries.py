from pymongo import MongoClient, GEO2D
from pprint import pprint
import os

print("Connecting to database...")
client = MongoClient(os.environ['MONGO_PATH'])  # mongodb://localhost:27017
db = client['carburator']

# To find a station with a specific id
station_id = '86000023'
print("Find a station with the id " + station_id)
cursor = db.stations.find({'id': station_id})
results_count = 0
for doc in cursor:
    pprint(doc)
    results_count += 1
print(str(results_count) + " result(s) found.")


# To find a station with specific lon/lat
station_lon = 34002.019025654/100000
station_lat = 4658927.575/100000
print("Find a station with the lonlat " + str(station_lon) + " " + str(station_lat))
cursor = db.stations.find({'lonlat': [station_lon, station_lat]})
results_count = 0
for doc in cursor:
    results_count += 1
print(str(results_count) + " result(s) found.")

# To find a station with a city
station_city = "VILLEURBANNE"
print("Find a station with the city " + station_city)
cursor = db.stations.find({'city': station_city})
results_count = 0
for doc in cursor:
    print(doc['lonlat'])
    results_count += 1
print(str(results_count) + " result(s) found.")

# To find stations near a lonlat (limit 5)
lat = 45.783428
lon = 4.881299
print("Find 5 stations near the lonlat " + str(lon) + " " + str(lat))
cursor = db.stations.find({'lonlat': {'$near': [lon, lat]}}).limit(5)
results_count = 0
for doc in cursor:
    print(doc['address'], doc['city'])
    results_count += 1
print(str(results_count) + " result(s) found.")
