// var whitelist = [
//   'https://api.us.apiconnect.ibmcloud.com/',
//   'https://us.apiconnect.ibmcloud.com'
// ];
// module.exports = {
//   "initial": {
//     "cors": {
//       "params": {
//         "origin": function (origin, callback) {
//           console.log('checkin cors in middleware.local');
//           console.log(origin);
//           if (whitelist.indexOf(origin) !== -1) {
//             callback(null, true);
//           } else {
//             callback(new Error('Not allowed by CORS'));
//           }
//         }
//       }
//     }
//   }
// };