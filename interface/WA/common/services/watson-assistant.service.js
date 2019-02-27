var AssistantV1 = require('watson-developer-cloud/assistant/v1'),
    q = require('q'),
    ASSISTANT,
    credentials = require('../credentials/credentials');

var initializeService = function () {
  ASSISTANT = new AssistantV1({
    version: credentials.assistant.version,
    username: credentials.assistant.username,
    password: credentials.assistant.password,
    url: credentials.assistant.url
  });
};


module.exports.message = function (text) {
  var deferred = q.defer();
  console.log('--- Assistant :: message');


  ASSISTANT.message({
    workspace_id: credentials.assistant.workspaceId,
    input: { 'text': text }
  }, function(err, response) {
    if (err) {
      console.log(err);
      deferred.reject(err);
    } else {
      deferred.resolve(response);
    }
  });
  return deferred.promise;

};

initializeService();
