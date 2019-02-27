'use strict';

module.exports = function (Client) {

  Client.disableRemoteMethodByName("upsert");                               // disables PATCH /Clients
  Client.disableRemoteMethodByName("find");                                 // disables GET /Clients
  Client.disableRemoteMethodByName("replaceOrCreate");                      // disables PUT /Clients
  Client.disableRemoteMethodByName("create");                               // disables POST /Clients

  Client.disableRemoteMethodByName("prototype.updateAttributes");           // disables PATCH /Clients/{id}
  Client.disableRemoteMethodByName("findById");                             // disables GET /Clients/{id}
  Client.disableRemoteMethodByName("exists");                               // disables HEAD /Clients/{id}
  Client.disableRemoteMethodByName("replaceById");                          // disables PUT /Clients/{id}
  Client.disableRemoteMethodByName("deleteById");                           // disables DELETE /Clients/{id}

  Client.disableRemoteMethodByName('prototype.__get__accessTokens');        // disable GET /Clients/{id}/accessTokens
  Client.disableRemoteMethodByName('prototype.__create__accessTokens');     // disable POST /Clients/{id}/accessTokens
  Client.disableRemoteMethodByName('prototype.__delete__accessTokens');     // disable DELETE /Clients/{id}/accessTokens

  Client.disableRemoteMethodByName('prototype.__findById__accessTokens');   // disable GET /Clients/{id}/accessTokens/{fk}
  Client.disableRemoteMethodByName('prototype.__updateById__accessTokens'); // disable PUT /Clients/{id}/accessTokens/{fk}
  Client.disableRemoteMethodByName('prototype.__destroyById__accessTokens');// disable DELETE /Clients/{id}/accessTokens/{fk}

  Client.disableRemoteMethodByName('prototype.__count__accessTokens');      // disable  GET /Clients/{id}/accessTokens/count

  Client.disableRemoteMethodByName("prototype.verify");                     // disable POST /Clients/{id}/verify
  Client.disableRemoteMethodByName("changePassword");                       // disable POST /Clients/change-password
  Client.disableRemoteMethodByName("createChangeStream");                   // disable GET and POST /Clients/change-stream

  Client.disableRemoteMethodByName("confirm");                              // disables GET /Clients/confirm
  Client.disableRemoteMethodByName("count");                                // disables GET /Clients/count
  Client.disableRemoteMethodByName("findOne");                              // disables GET /Clients/findOne

  //Client.disableRemoteMethodByName("login");                                // disables POST /Clients/login
  //Client.disableRemoteMethodByName("logout");                               // disables POST /Clients/logout

  Client.disableRemoteMethodByName("resetPassword");                        // disables POST /Clients/reset
  Client.disableRemoteMethodByName("setPassword");                          // disables POST /Clients/reset-password
  Client.disableRemoteMethodByName("update");                               // disables POST /Clients/update
  Client.disableRemoteMethodByName("upsertWithWhere");                      // disables POST /Clients/upsertWithWhere

};
