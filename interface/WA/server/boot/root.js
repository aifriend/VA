'use strict';

var credentials = require('../../common/credentials/credentials');
module.exports = function(server) {
  // Install a `/` route that returns server status
  var router = server.loopback.Router();
  router.get('/', server.loopback.status());

  router.post('/api/**/*', function(req, res, next) {
    console.log(req.headers);
    var apiToken = req.headers['x-ibm-token'];
    if (apiToken === credentials.xclient.token) {
      next(); // if client ok then continue to loopback
    } else {
      const error = {
        status: 500,
        message: 'Request Headers for Client ID and Client Secret invalids'
      };
      res.status(500).send(error);
    }
  });
  server.use(router);
};
