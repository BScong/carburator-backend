import xml.etree.ElementTree as ET
import json
from pymongo import MongoClient

print("Parsing XML data...")
tree = ET.parse('sample.xml')
root = tree.getroot()

print("Connecting to database...")
client = MongoClient("mongodb://localhost:27017")
db = client['carburator']

to_retry = []

count,total=0,0
print("Adding values...")
for child in root:
	data = {
		'id':child.attrib['id'],
		'lat':child.attrib['latitude'],
		'lon':child.attrib['longitude'],
		'address':child.find('adresse').text,
		'city':child.find('ville').text,
		'postcode':child.attrib['cp'],
		'pop':child.attrib['pop'], # ????
		'prices':{
			'':''
		},
		'hours':{
			'open':child.find('ouverture').attrib['debut'],
			'close':child.find('ouverture').attrib['fin'],
			'except':child.find('ouverture').attrib['saufjour']
		}
	}

	services = []
	for service in child.iter('service'):
		services.append(service.text)
	data['services']=services

	prices = {}
	for price in child.iter('prix'):
		priceData = {
			'name':price.attrib['nom'],
			'updated':price.attrib['maj'],
			'value':price.attrib['valeur']
		}
		prices[price.attrib['id']] = priceData
	data['prices']=prices

	result = db.stations.insert_one(data)

	if not result.acknowledged:
		to_retry.append(data) 
	else:
		count+=1
	total+=1
	#print(json.dumps(data, sort_keys=True, indent=4))

# Retry one time if error occured
for data in to_retry:
	result = db.stations.insert_one(data)
	if not result.acknowledged:
		print("Error adding id " + data['id'] + " to the database")
	else:
		count+=1

client.close()

print("Finished adding values, total " + str(total) + " elements, "+ str(count) + " added.")