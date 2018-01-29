'use strict';
module.exports = function(app) {
  var carburator = require('../controllers/carburatorController');

  // carburator Routes
  app.route('/stations')
    .get(carburator.list_all_stations);


  app.route('/stations/id/:station_id')
    .get(carburator.get_station_by_id);

  app.route('/stations/lon/:lon/lat/:lat')
    .get(carburator.get_stations_by_lonlat);

  app.route('/ping')
    .get(function(req,res){
  		res.status(200).send("Running.") // Maybe implement express-ping (health) on ping endpoint
  	});

};
