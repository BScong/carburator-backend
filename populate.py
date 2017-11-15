import xml.etree.ElementTree as ET
import json

tree = ET.parse('sample.xml')
root = tree.getroot()
types={}
count=0
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

	count+=1
	print(json.dumps(data, sort_keys=True, indent=4))
print(count)