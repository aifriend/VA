'use strict';

var WatsonDiscoverySrv = require('../services/watson-discovery.service'),
  WatsonAssistantSrv = require('../services/watson-assistant.service'),
  CloudantDBSrv = require('../services/cloudant-db.service');

var NOTUNDERSTANDINGTEXT = 'No entiendo su pregunta';


module.exports = function (Message) {

  Message.assess = function (request, cb) {

    console.log('|||  Message :: assess');
    var apiResponse = {
      content: [],
      intent: '',
      confidence: -1,
      entities: []
      // score: -1
      // url: 'No url found',
      // highlight: ''
    };
    // var threshold = request.threshold;

    var hasResponse = false;

    WatsonAssistantSrv.message(request.query).then(function (response) {

      if (response.intents.length > 0) {
        apiResponse.intent = response.intents[0].intent;
        apiResponse.confidence = response.intents[0].confidence;
        hasResponse = true;
      }

      if (response.entities.length > 0) {
        response.entities.map(function (entity) {
          var entityText = response.input.text;
          apiResponse.entities.push({
            name: entity.entity,
            value: entityText.substring(entity.location[0], entity.location[1]),
            confidence: entity.confidence
          });
        });
      }

      console.log('------------------------');
      console.log(response.output);

      var texts = response.output.text;
      texts.map(function (text, index) {

        if (text !== NOTUNDERSTANDINGTEXT) {
          apiResponse.content.push(text);
        }
        if (index === (texts.length - 1)) {
          cb(null, apiResponse);
        }
      });
    });
  }

  Message.remoteMethod('assess', {
    accepts: { arg: 'request', type: 'Object' },
    returns: { arg: 'result', type: 'Object' }
  });

  Message.disableRemoteMethodByName("upsert");                               // disables PATCH /Messages
  Message.disableRemoteMethodByName("find");                                 // disables GET /Messages
  Message.disableRemoteMethodByName("replaceOrCreate");                      // disables PUT /Messages
  Message.disableRemoteMethodByName("create");                               // disables POST /Messages

  Message.disableRemoteMethodByName("prototype.updateAttributes");           // disables PATCH /Messages/{id}
  Message.disableRemoteMethodByName("findById");                             // disables GET /Messages/{id}
  Message.disableRemoteMethodByName("exists");                               // disables HEAD /Messages/{id}
  Message.disableRemoteMethodByName("replaceById");                          // disables PUT /Messages/{id}
  Message.disableRemoteMethodByName("deleteById");                           // disables DELETE /Messages/{id}

  Message.disableRemoteMethodByName("createChangeStream");                   // disable GET and POST /Messages/change-stream
  Message.disableRemoteMethodByName("confirm");                              // disables GET /Messages/confirm
  Message.disableRemoteMethodByName("count");                                // disables GET /Messages/count
  Message.disableRemoteMethodByName("findOne");                              // disables GET /Messages/findOne
  Message.disableRemoteMethodByName("update");                               // disables POST /Messages/update
  Message.disableRemoteMethodByName("upsertWithWhere");                      // disables POST /Messages/upsertWithWhere

  // Message.beforeRemote('assess', function(context, query, next) {
  //   console.log('--------------- BEFORE REMOTE : assess');
  //   next();
  // });

};
