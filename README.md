# slack-messages
Slack messages made easy. Send slack messages to channels from you backend api etc.

## install
```bash
pip install slack-messages
```

## Examples
Send a message
```bash
from slack_messages import SlackMessages, ErrorPostingMessage, ErrorFetchingChannels

slack = SlackMessages("<Access Token>")
res = slack.send_message(channel_name="my-chan", message="Hello!")
```

### Errors
```bash
from slack_messages import SlackMessages, ErrorPostingMessage, ErrorFetchingChannels
try:
    slack = SlackMessages("<Access Token>")
    res = slack.send_message(channel_name="my-chan", message="Hello!")
except (ErrorFetchingChannels, ErrorPostingMessage) as err:
  # handle errors
```