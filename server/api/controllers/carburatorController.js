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