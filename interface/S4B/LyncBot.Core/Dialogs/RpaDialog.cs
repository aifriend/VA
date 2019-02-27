using System;
using System.Threading.Tasks;
using Microsoft.Bot.Builder.Dialogs;
using Microsoft.Bot.Connector;
using System.Net;
using Newtonsoft.Json;
using System.Collections.Generic;
using System.IO;
using System.Configuration;

namespace LyncBot.Core.Dialogs
{
    [Serializable]
    public class RpaDialog : IDialog<object>
    {
        public static Models.Token token = null;

        public Task StartAsync(IDialogContext context)
        {
            //Random rnd = new Random();
            //int sessionId = rnd.Next(1, 1000000);
            //SetSession(context, sessionId.ToString("D6"));

            context.Wait(MessageReceivedAsync);

            return Task.CompletedTask;
        }

        private async Task MessageReceivedAsync(IDialogContext context, IAwaitable<object> result)
        {
            var activity = await result as Activity;

            string userEmail = activity.From.Id.Split(new string[] { ":" }, StringSplitOptions.RemoveEmptyEntries)[1];

            string question = activity.Text;

            //string answer = CallAIController(question, userEmail);
            string answer = UtilsToken.UtilsWebService.GetAnswerAPIGateway(question, userEmail);

            await context.PostAsync(answer);

            context.Wait(MessageReceivedAsync);
        }

        /// <summary>
        /// This method calls AI_Controller and get response.
        /// </summary>
        /// <param name="question"></param>
        /// <param name="session"></param>
        /// <returns></returns>
        private string CallAIController(string question, string session)
        {
            string responseString = "";

            var query = question.Trim();

            //string url = @"http://52.178.176.50:8090/get_answer?q=" + Uri.EscapeUriString(question);

            //string url = @"http://52.178.176.50:8090/get_answer";
            string url = ConfigurationManager.AppSettings["ControllerUrl"];

            //Console.WriteLine("URL: " + url);

            Uri uriBase = new Uri(url);     //Máquina Linux Azure

            try
            {
                /*
                using (WebClient client = new WebClient())
                {
                    client.Encoding = System.Text.Encoding.UTF8;

                    //responseString = client.DownloadString(uriBase);

                    AIControllerRequest req = new AIControllerRequest(question, session, "");
                    string reqJson = JsonConvert.SerializeObject(req);

                    string responseJson = client.UploadString(url, reqJson);

                    if (responseJson == null)
                    {
                        responseString = "En este momento no puedo atenderle, inténtelo de nuevo más tarde";
                    }
                    else
                    {
                        //responseString = tokenizeResponse(responseString);
                        responseString = processResponse(responseJson);
                    }
                }*/

                var httpWebRequest = (HttpWebRequest)WebRequest.Create(url);
                httpWebRequest.ContentType = "application/json";
                httpWebRequest.Method = "POST";

                using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
                {
                    AIControllerRequest req = new AIControllerRequest(query, session, "");
                    string reqJson = JsonConvert.SerializeObject(req);

                    Console.WriteLine("[" + session + "] " + query);

                    streamWriter.Write(reqJson);
                    streamWriter.Flush();
                    streamWriter.Close();
                }

                var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
                using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
                {
                    var responseJson = streamReader.ReadToEnd();

                    if (responseJson == null)
                    {
                        responseString = "En este momento no puedo atenderle, inténtelo de nuevo más tarde";
                    }
                    else
                    {
                        //responseString = tokenizeResponse(responseString);
                        responseString = ProcessResponse(responseJson);
                    }
                }
            }
            catch (WebException ex)
            {
                Console.WriteLine("\n" + ex.Message + "\n" + ex.StackTrace);

                if (ex.Status == WebExceptionStatus.ProtocolError)
                {
                    if (ex.Response != null)
                    {
                        HttpWebResponse httpResponse = (HttpWebResponse)ex.Response;

                        //Si el StatusCode == 401 utilizamos el mensaje de salida del AIController
                        if (httpResponse.StatusCode == HttpStatusCode.Unauthorized)
                        {
                            responseString = "Lo siento, no está autorizado a acceder a este recurso";
                        }
                    }
                }
                else
                {
                    responseString = "En este momento no puedo atenderle, inténtelo de nuevo más tarde.";
                }
            }
            catch (Exception ex2)
            {
                Console.WriteLine("\n" + ex2.Message + "\n" + ex2.StackTrace);

                responseString = "En este momento no puedo atenderle, inténtelo de nuevo más tarde.";
            }

            return WebUtility.HtmlDecode(responseString);
        }

        /// <summary>
        /// Process response obtained from AI_Controller
        /// </summary>
        /// <param name="respJson">Json obtained</param>
        /// <returns>Message Obtained from JSON. transcript node</returns>
        public static string ProcessResponse(string respJson)
        {
            string resp = "";

            try
            {
                AIControllerResponse respObj = JsonConvert.DeserializeObject<AIControllerResponse>(respJson);

                if (respObj != null && respObj.answer != null && respObj.answer.question != null)
                {
                    if (respObj.answer.question.Count == 1)
                    {
                        if (!string.IsNullOrWhiteSpace(respObj.answer.question[0].transcript))
                        {
                            resp = respObj.answer.question[0].transcript;
                        }
                        else  //Respuesta vacía
                        {
                            resp = "(Respuesta Vacía)";
                        }
                    }
                    else if (respObj.answer.question.Count > 1)
                    {
                        resp = "";
                        foreach (AIControllerResponseParams line in respObj.answer.question)
                            resp += line.transcript + "\n";
                    }
                    else  //Count == 0
                    {
                        resp = "En este momento no puedo atenderle, inténtelo de nuevo más tarde. Disculpe las molestias";
                    }
                }
                else
                {
                    resp = "En este momento no puedo atenderle, inténtelo de nuevo más tarde. Disculpe las molestias.";
                }
            }
            catch (Exception ex)
            {
                resp = "En este momento no puedo atenderle, por favor inténtelo de nuevo más tarde. Disculpe las molestias.";
                Console.WriteLine(ex.Message);
                Console.WriteLine(ex.StackTrace);
            }

            return resp;
        }

        /*
        private string tokenizeResponse(string resp)
        {
            string response = "";

            //Parche para cuando el AIController no devuelve ninguna respuesta
            if (resp.Trim().Equals("") || resp.Trim().Equals("1$") || resp.Trim().Equals("2$") || resp.Trim().Equals("3$"))
            {
                return "Por el momento no puedo contestar a su pregunta/petición, disculpe las molestias.\nActualmente puedo ayudarle a:\n * Encontrar respuestas a preguntas frecuentes \n * Buscar información sobre una selección de documentación genérica \n * Lanzar robots RPA (disponible el robot Extensión de Proveedores) ";
            }
            //Fin Parche

            if (resp.StartsWith("1$"))  //Respuesta directa
            {
                response = resp.Substring(2);
            }
            else if (resp.StartsWith("2$") || resp.StartsWith("3$"))   //Varias alternativas
            {
                string[] tokens = resp.Split(new char[] { '$' }, StringSplitOptions.RemoveEmptyEntries);

                response = tokens[1];

                if (tokens.Length > 2)
                {
                    for (int i = 2; i < tokens.Length; i++)
                    {
                        response += tokens[i].Trim() + "\n";
                    }
                }
            }
            else if (resp.StartsWith("$0$"))   //Excepción
            {
                response = resp.Substring(3);
            }
            else
            {
                response = resp;
            }

            return response;
        }
        */

        private void SetSession(IDialogContext context, string sess)
        {
            context.PrivateConversationData.SetValue<string>("session", sess);
        }

        private string GetSession(IDialogContext context)
        {
            string sess = "";

            if (!context.PrivateConversationData.TryGetValue<string>("session", out sess))
            {
                sess = "0";
            }

            return sess;
        }
    }
}