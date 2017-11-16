'use strict';
module.exports = function(app) {
  var carburator = require('../controllers/carburatorController');

  // carburator Routes
  app.route('/stations')
    .get(carburator.list_all_stations);


  //app.route('/stations/:station_id')
  //  .get(carburator.get_station_by_id);
};
