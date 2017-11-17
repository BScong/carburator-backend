'use strict';

var mongoose = require('mongoose'),
  Station = mongoose.model('Stations');

exports.list_all_stations = function(req, res) {
  Station.find({}, function(err, station) {
    if (err)
      res.send(err);
    res.json(station);
  });
};

exports.get_station_by_id = function(req, res) {
	Station.find({'id':req.params.station_id}, function(err, station) {
	if (err)
	  res.send(err);
	res.json(station);
	});
};

exports.get_stations_by_lonlat = function(req, res) {
	var limit = parseInt(req.query.limit)
	if(isNaN(limit) || limit>20 || limit < 1){
		limit = 20
	}
	var search = Station.find({'lonlat':{'$near': [req.params.lon,req.params.lat]}}).limit(limit).exec(
		function(err, station) {
		if (err)
			res.send(err);
		res.json(station);
	});
};
