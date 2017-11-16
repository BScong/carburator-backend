'use strict';
var mongoose = require('mongoose');
var Schema = mongoose.Schema;


var StationSchema = new Schema(
{
  id: {
    type: String
  },
  address: {
    type: String
  },
  city: {
    type: String
  },
  postcode: {
    type: Date
  },
  hours: {
    open: {
      type: String
    },
    close: {
      type: String
    },
    except: {
      type: String
    }
  },
  last_modified: {
    type: Date
  },
  lonlat: {
    type: [
      Number
    ]
  },
  pop: {
    type: String
  },
  prices: {
    1: {
      name: {
        type: String
      },
      updated: {
        type: Date
      },
      value: {
        type: String
      }
    },
    2: {
      name: {
        type: String
      },
      updated: {
        type: Date
      },
      value: {
        type: String
      }
    },
    3: {
      name: {
        type: String
      },
      updated: {
        type: Date
      },
      value: {
        type: String
      }
    },
    4: {
      name: {
        type: String
      },
      updated: {
        type: Date
      },
      value: {
        type: String
      }
    },
    5: {
      name: {
        type: String
      },
      updated: {
        type: Date
      },
      value: {
        type: String
      }
    },
    6: {
      name: {
        type: String
      },
      updated: {
        type: Date
      },
      value: {
        type: String
      }
    }
  },
  services: {
    type: [
      String
    ]
  }
}
);

module.exports = mongoose.model('Stations', StationSchema);