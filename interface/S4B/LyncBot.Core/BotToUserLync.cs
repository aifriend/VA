using Microsoft.Bot.Builder.Dialogs.Internals;
using Microsoft.Bot.Builder.Internals.Fibers;
using Microsoft.Bot.Connector;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace LyncBot.Core
{
    public class BotToUserLync: IBotToUser
    {
        private IMessageActivity toBot;
        private Func<string, Task> _callback;

        public BotToUserLync(IMessageActivity toBot, Func<string, Task> callback)
        {
            SetField.NotNull(out this.toBot, nameof(toBot), toBot);
            _callback = callback;
        }

        public IMessageActivity MakeMessage()
        {
            return this.toBot;
        }

        public async Task PostAsync(IMessageActivity message, CancellationToken cancellationToken = default(CancellationToken))
        {
            await _callback(message.Text);
        }
    }
}
