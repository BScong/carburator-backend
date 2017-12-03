# Carburator Backend
Building an RESTful API around gas prices open data (France only).

Using Python to fetch data, NodeJS for server computations and MongoDB for data storage.

Data from [prix-carburants.gouv.fr/rubrique/opendata/](https://www.prix-carburants.gouv.fr/rubrique/opendata/).

## API Usage
NodeJS server. Install with ```npm install```then start with ```npm start```. It should start on localhost:3000.

If your MongoDB is running (and populated), you can request the different endpoints.

## Endpoints
### /stations
Returns all the stations.

### /stations/id/:id
Return the station with the ID mentionned.

### /stations/lon/:lon/lat/:lat?limit=5
Return the stations near the lonlat mentionned. You can indicate a limit (by default 20, max 20).

## Fetching data
Launch your MongoDB server. The script uses the default location : ```mongodb://localhost:27017```.

Install the dependencies with ```pip install -r requirements.txt```.

Execute the Python script ```populate.py```. It will populate the database with the file ```sample.xml```. This script parses the xml into json objects, then store them in the MongoDB database.

You can schedule a cron job to execute ```populate.py``` to have up-to-date data. For this use the xml located at [donnees.roulez-eco.fr/opendata/instantane](https://donnees.roulez-eco.fr/opendata/instantane). The file is refreshed every 10 minutes. Use [donnees.roulez-eco.fr/opendata/jour](https://donnees.roulez-eco.fr/opendata/jour) if you prefer to have the daily flow.

## Querying data
You can find examples of queries in the ```queries.py``` file.

## Data format
Here is an example of formatting for a single station : 

```json
{
	"id": "86000023",
	"address": "10 Boulevard Jeanne d'Arc",
	"city": "POITIERS",
	"postcode": "86000",
	"hours": {
		"open": "07:00",
		"close": "21:00",
		"except": ""
	},
	"last_modified": "2017-11-15 14:56:20",
	"lonlat": [0.34002019025654, 46.58927575],
	"pop": "R",
	"prices": {
		"1": {
			"name": "Gazole",
			"updated": "2017-11-12 06:46:26",
			"value": "1.400"
		},
		"2": {
			"name": "SP95",
			"updated": "2017-11-12 06:46:26",
			"value": "1.570"
		},
		"5": {
			"name": "E10",
			"updated": "2017-11-12 06:46:26",
			"value": "1.530"
		},
		"6": {
			"name": "SP98",
			"updated": "2017-11-12 06:46:26",
			"value": "1.610"
		}
	},
	"services": [
		"Restauration à emporter",
		"Carburant qualité supérieure",
		"Station de lavage",
		"Boutique alimentaire",
		"Station de gonflage",
		"Boutique non alimentaire",
		"Vente de gaz domestique",
		"Relais colis",
		"Lavage multi-programmes"
 	]
 }
```

## Todo
* Handle exceptions without crashing app.
* Sanitize user input (id, lon, lat). Limit done.
* Change id, lon, lat requests to a single endpoint with GET parameters
* Add city endpoint / postcode endpoint
* Add search by address/city = convert address/city to lonlat then request on lonlat endpoint.
* Add GasType parameter to searches
* Add price filter to searches
* Add opening hours filter to searches. (Maybe?, a lot of data has incorrect hours).
* Write script to automatically fetch new data and update the database
* Deploy on server
* Tests
* Cleaner structure for code
* Better documentation for endpoints
* Switch database from MongoDB to MySQL
* Frontend : Android app
* Frontend : webapp
* Frontend : Google Assistant integration
* Dockerize project
* Deployment with Capistrano