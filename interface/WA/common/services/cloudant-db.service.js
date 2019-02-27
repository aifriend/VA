var CLOUDANT = require('cloudant');
var q = require('q');

var DB,
  credentials = require('../credentials/credentials');

var initDB = function (databaseName) {
  var cloudant = CLOUDANT({
    url: credentials.cloudantDb.url
  });
  DB = cloudant.db.use(databaseName);
};
//initDB();

module.exports.list = function() {
  console.log('--- CloudantDBService : list');
  initDB(credentials.cloudantDb.names.documents);
  var deferred = q.defer();
  DB.list(function (err, data) {
    if (err) {
      console.log(err);
      deferred.reject(err);
    } else {
      deferred.resolve(data);
    }
  });
};


module.exports.findById = function (id) {
  console.log('--- CloudantDBService : findById');
  initDB(credentials.cloudantDb.names.documents);

  var query = {
    'selector': {
      '_id': id
    }
  };

  var deferred = q.defer();
  DB.find(query, function (err, data) {
    if (err) {
      console.log(err);
      deferred.reject(err);
    } else {
      deferred.resolve(data);
    }
  });
  return deferred.promise;
};
