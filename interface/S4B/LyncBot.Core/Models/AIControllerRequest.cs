using System;

namespace LyncBot.Core
{
    public class AIControllerRequest
    {
        public AIControllerRequestParams request { get; set; }

        public AIControllerRequest()
        {
            request = new AIControllerRequestParams("", "", "");
        }

        public AIControllerRequest(string trans, string sess, string conf)
        {
            request = new AIControllerRequestParams(trans, sess, conf);
        }
    }

    public class AIControllerRequestParams
    {
        public string transcription { get; set; }
        public string session { get; set; }
        public string confidence { get; set; }

        public AIControllerRequestParams()
        {
            this.transcription = "";
            this.session = "";
            this.confidence = "";
        }

        public AIControllerRequestParams(string trans, string sess, string conf)
        {
            this.transcription = trans;
            this.session = sess;
            this.confidence = conf;
        }
    }
}
