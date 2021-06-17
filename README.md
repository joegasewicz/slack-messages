# slack-messages
Slack messages made easy. Send slack messages to channels from you backend api etc.

## install
```bash
pip install slack-messages
```

## Examples
Send a message
```bash
slack = SlackMessages("<Access Token>")
res = slack.send_message(channel_name="my-chan", message="Hello!")
```
