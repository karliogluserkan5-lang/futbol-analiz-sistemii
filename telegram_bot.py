import requests

class TelegramBot:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.base = f"https://api.telegram.org/bot{self.token}"
    
    def send_message(self, message):
        url = f"{self.base}/sendMessage"
        data = {"chat_id": self.chat_id, "text": message, "parse_mode": "HTML"}
        try:
            return requests.post(url, data=data).json()
        except:
            return None
