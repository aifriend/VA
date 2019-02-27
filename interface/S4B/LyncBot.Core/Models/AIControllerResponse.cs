using System;
using System.Collections.Generic;

namespace LyncBot.Core
{
    public class AIControllerResponse
    {
        public AIControllerAnswer answer { get; set; }

        public AIControllerResponse()
        {
            this.answer = new AIControllerAnswer();
        }

        public AIControllerResponse(AIControllerAnswer ans)
        {
            this.answer = ans;
        }
    }

    public class AIControllerAnswer
    {
        public string next { get; set; }
        public List<AIControllerResponseParams> question { get; set; }
        public string session { get; set; }

        public AIControllerAnswer()
        {
            this.next = "";
            this.question = new List<AIControllerResponseParams>();
            this.session = "";
        }

        public AIControllerAnswer(string next, List<AIControllerResponseParams> question, string session)
        {
            this.next = next;
            this.question = question;
            this.session = session;
        }
    }

    public class AIControllerResponseParams
    {
        public string id { get; set; }
        public string transcript { get; set; }
        public string type { get; set; }

        public AIControllerResponseParams()
        {
            this.id = "";
            this.transcript = "";
            this.type = "";
        }

        public AIControllerResponseParams(string id, string trans, string type)
        {
            this.id = id;
            this.transcript = trans;
            this.type = type;
        }
    }
}
