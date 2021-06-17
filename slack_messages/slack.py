from typing import Dict
import requests


class ErrorFetchingChannels(Exception):
    pass


class ErrorPostingMessage(Exception):
    pass


class SlackMessages:

    auth_headers: Dict

    post_message_url = "https://slack.com/api/chat.postMessage"
    conversations_list_url = "https://slack.com/api/conversations.list"

    def __init__(self, token: str):
        self.token = token
        self.auth_headers = {"Authorization": f"Bearer {self.token}"}

    def send_message(self, *, channel_name: str, message: str) -> Dict:
        channel_id = self._get_channel_id(channel_name)
        r = requests.post(
            self.post_message_url,
            headers={
                "Content-Type": "application/json",
                **self.auth_headers,
            },
            json={
                "channel": channel_id,
                "text": message,
            }
        )
        data = r.json()
        if not data["ok"]:
            raise ErrorPostingMessage(f"There was an error posting slack message: {data['error']}")
        return data

    def _get_channel_id(self, channel_name: str) -> str:
        r = requests.get(
            self.conversations_list_url,
            headers=self.auth_headers,
        )

        channels = r.json()["channels"]
        for c in channels:
            if c["name"] == channel_name:
                return c["id"]
        raise ErrorFetchingChannels("Error: Could not get a list of channels from your slack workspace.")
