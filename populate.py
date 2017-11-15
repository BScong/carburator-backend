import xml.etree.ElementTree as ET
import json
from pymongo import MongoClient, GEO2D
import datetime

print("Parsing XML data...")
tree = ET.parse('sample.xml')
root = tree.getroot()

print("Connecting to database...")
client = MongoClient("mongodb://localhost:27017")
db = client['carburator']
db.stations.create_index([("lonlat", GEO2D )])

to_retry = []

count,total=0,0
print("Adding values...")
for child in root:
	data = {
		'id':child.attrib['id'],
		'address':child.find('adresse').text,
		'city':child.find('ville').text.upper(),
		'postcode':child.attrib['cp'],
		'pop':child.attrib['pop'], # ????
		'prices':{
		},
		'hours':{
			'open':child.find('ouverture').attrib['debut'],
			'close':child.find('ouverture').attrib['fin'],
			'except':child.find('ouverture').attrib['saufjour']
		},
		'last_modified':datetime.datetime.utcnow()
	}

	if child.attrib['longitude'] and child.attrib['longitude']:
		data['lonlat']=[float(child.attrib['longitude'])/100000,float(child.attrib['latitude'])/100000]

	services = []
	for service in child.iter('service'):
		services.append(service.text)
	data['services']=services

	prices = {}
	for price in child.iter('prix'):
		priceData = {
			'name':price.attrib['nom'],
			'updated':datetime.datetime.strptime(price.attrib['maj'],"%Y-%m-%d %H:%M:%S"),
			'value':price.attrib['valeur']
		}
		prices[price.attrib['id']] = priceData
	data['prices']=prices

	try:
		result = db.stations.insert_one(data)

		if not result.acknowledged:
			to_retry.append(data) 
		else:
			count+=1
	except Exception as err:
		to_retry.append(data) 
		print(err)
	total+=1
	#print(json.dumps(data, sort_keys=True, indent=4))

# Retry one time if error occured
for data in to_retry:
	try:
		result = db.stations.insert_one(data)
		if not result.acknowledged:
			print("Error adding id " + data['id'] + " to the database")
		else:
			count+=1
	except Exception as err:
		print(json.dumps(data, sort_keys=True, indent=4))
		print(err)

client.close()

print("Finished adding values, total " + str(total) + " elements, "+ str(count) + " added.")