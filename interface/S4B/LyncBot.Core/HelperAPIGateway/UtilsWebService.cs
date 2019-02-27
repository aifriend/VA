using LyncBot.Core.Dialogs;
using LyncBot.Core.Models;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Formatting;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace LyncBot.Core.UtilsToken
{
    public static class UtilsWebService
    {

        /// <summary>
        /// This method obtain operation token from API Gateway
        /// </summary>
        /// <returns>Operation Token on string type</returns>
        public static Token GetTokenAPIGateway()
        {
            //string url = ConfigurationManager.AppSettings["ApiGatewayUrlToken"];
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            Console.WriteLine("Obteniendo token de seguridad del API Gateway");

            Token token = null;

            string baseAddress = ConfigurationManager.AppSettings["ApiGatewayUrlToken"];

            using (var client = new HttpClient(new HttpClientHandler
            {
                ClientCertificateOptions = ClientCertificateOption.Automatic
            }))

            {



                var form = new Dictionary<string, string>
                {
                    {"grant_type", "client_credentials"},
                    {"client_id",  ConfigurationManager.AppSettings["ApiGatewayClientIDToken"]},
                    {"client_secret",  ConfigurationManager.AppSettings["ApiGatewayClientSecretToken"]}
                };

                try
                {
                    var tokenResponse = client.PostAsync(baseAddress, new FormUrlEncodedContent(form)).Result;
                    token = tokenResponse.Content.ReadAsAsync<Token>(new[] { new JsonMediaTypeFormatter() }).Result;
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Error obtiendo token de seguridad", ex.Message);
                }
            }

            return token;

        }


        /// <summary>
        /// This method obtain operation token from API Gateway
        /// </summary>
        /// <param name="question"></param>
        /// <param name="userEmail"></param>
        /// <returns>Response string</returns>
        public static string GetAnswerAPIGateway(string question, string userEmail)
        {
            string responseString = string.Empty;
            Token tok = null;

            string query = question.Trim();

            //Calling method to get Token            
            if (Core.Dialogs.RpaDialog.token == null)
            {
                //log.Debug("Token Ok");
                Console.WriteLine("No existe Token.");
                tok = GetTokenAPIGateway();

                if (!string.IsNullOrEmpty(tok.AccessToken))
                {
                    Console.WriteLine("Token Obtenido correctamente");
                    Core.Dialogs.RpaDialog.token = tok;
                }
                else
                {
                    Console.WriteLine("No se ha podido obtener el token");
                }
            }
            else
            {
                Console.WriteLine("Ya existe Token");
            }

            string url = ConfigurationManager.AppSettings["ApiGatewayUrlAnswer"];
            Console.WriteLine("Realizando llamada al API Gateway");


            try
            {
                var client = new HttpClient(
                    new HttpClientHandler
                    {
                        ClientCertificateOptions = ClientCertificateOption.Automatic
                    })
                {
                    BaseAddress = new Uri(url)
                };
                client.DefaultRequestHeaders.Accept.Clear();
                client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
                client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", Core.Dialogs.RpaDialog.token.AccessToken);
                ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

                try
                {
                    AIControllerRequest req = new AIControllerRequest(query, userEmail, "");
                    string reqJson = JsonConvert.SerializeObject(req);

                    Console.WriteLine("[" + userEmail + "] \"" + query + "\"");

                    HttpResponseMessage result = client.PostAsJsonAsync(url, req).Result;

                    string stringContent = string.Empty;
                    HttpContent content = null;
                    switch (result.StatusCode)
                    {
                        #region Frecuently Used
                        case HttpStatusCode.OK:
                            content = result.Content;
                            stringContent = content.ReadAsStringAsync().Result;
                            Console.WriteLine(result.StatusCode);
                            Console.WriteLine(stringContent);
                            responseString = RpaDialog.ProcessResponse(stringContent);
                            break;
                        case HttpStatusCode.InternalServerError:
                            responseString = "En este momento no puedo atenderle, inténtelo de nuevo más tarde.";
                            content = result.Content;
                            stringContent = content.ReadAsStringAsync().Result;
                            Console.WriteLine(result.StatusCode);
                            Console.WriteLine(stringContent);
                            //responseString = RpaDialog.ProcessResponse(stringContent);
                            break;
                        case HttpStatusCode.NoContent:
                            break;
                        case HttpStatusCode.Unauthorized:
                            Console.WriteLine("401 Unauthorized. Token caducado, volviendo a obtener token");
                            Core.Dialogs.RpaDialog.token = null;
                            GetAnswerAPIGateway(query, userEmail);
                            break;
                        case HttpStatusCode.BadRequest:
                        case HttpStatusCode.Forbidden:
                        case HttpStatusCode.NotFound:
                        case HttpStatusCode.NotImplemented:
                        case HttpStatusCode.BadGateway:
                        case HttpStatusCode.ServiceUnavailable:
                            responseString = "En este momento no puedo atenderle, inténtelo de nuevo más tarde.";
                            content = result.Content;
                            stringContent = content.ReadAsStringAsync().Result;
                            Console.WriteLine(result.StatusCode);
                            Console.WriteLine(stringContent);
                            //responseString = RpaDialog.ProcessResponse(stringContent);
                            break;

                        #endregion

                        #region Not frecuently used

                        case HttpStatusCode.Continue:
                            break;
                        case HttpStatusCode.Created:
                            break;
                        case HttpStatusCode.Accepted:
                            break;
                        case HttpStatusCode.MethodNotAllowed:
                            break;
                        case HttpStatusCode.RequestTimeout:
                            break;
                        case HttpStatusCode.Conflict:
                            break;
                        case HttpStatusCode.Gone:
                            break;
                        case HttpStatusCode.UnsupportedMediaType:
                            break;
                        case HttpStatusCode.ExpectationFailed:
                            break;
                            #endregion
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine("\n" + ex.Message + "\n" + ex.StackTrace);
                    Console.WriteLine("Error realizando la llamada al get_answer del API Gateway. " + ex.Message);
                    responseString = "En este momento no puedo atenderle, inténtelo de nuevo más tarde.";
                }
            }
            catch (Exception exc)
            {
                Console.WriteLine("\n" + exc.Message + "\n" + exc.StackTrace);
                responseString = "En este momento no puedo atenderle, inténtelo de nuevo más tarde.";
            }

            return WebUtility.HtmlDecode(responseString);

        }

    }
}
