var DiscoveryV1 = require('watson-developer-cloud/discovery/v1'),
    q = require('q'),
    DISCOVERY,
    credentials = require('../credentials/credentials');


var initializeService = function () {
  DISCOVERY = new DiscoveryV1({
    version_date: credentials.discovery.version,
    username: credentials.discovery.username,
    password: credentials.discovery.password,
  });
};


module.exports.query = function (text) {
  var deferred = q.defer();
  console.log('--- Discovery :: query');
  DISCOVERY.query({
    'environment_id': credentials.discovery.environmentId,
    'collection_id': credentials.discovery.collectionId,
    'natural_language_query': text,
    'highlight': true
  }, function (err, data) {
    if (err) {
      console.log(err);
      deferred.reject(err);
    } else {
      deferred.resolve(data);
    }
  });
  return deferred.promise;
}

initializeService();