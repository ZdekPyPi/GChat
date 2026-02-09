import requests
import json
import urllib3
from gchat.uikit import UiCard

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class GChat:
    def __init__(self, webhook: str):
        self.webhook = webhook
        self.headers = {"Content-Type": "application/json; charset=UTF-8"}

    def send_card(self, card: UiCard, replaces=[]):  # [("{body}","meu conteudo!")]
        payload = json.dumps(card.render())
        for rp in replaces:
            payload = payload.replace(rp[0], rp[1])

        payload = {"cardsV2": [json.loads(payload)]}

        response = requests.post(
            self.webhook, json=payload, headers=self.headers, timeout=30, verify=False
        )
        response.raise_for_status()
