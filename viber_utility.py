
import requests
import json
from datetime import datetime, timedelta

class  SendViberAlert():
    def __init__(self, viber_auth_token, sender_id):
        self.viber_auth_token = viber_auth_token
        self.sender_id = sender_id
        self.receiver_id = sender_id
        self.message_type = "text"
        self.min_api_version = 1

    def send_message(self, message_content):
        url = "https://chatapi.viber.com/pa/post"
        headers = {
            "X-Viber-Auth-Token": self.viber_auth_token,
            "Content-Type": "application/json"
        }

        payload = {
            "from": self.sender_id,
            "receiver": self.receiver_id,
            "type": self.message_type,
            "min_api_version": self.min_api_version
        }

        if self.message_type == "text":
            payload["text"] = message_content

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            print(f"Response content: {response.text}")
            return {"status": "error", "message": str(e), "details": response.text}
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error occurred: {e}")
            return {"status": "error", "message": str(e)}
        except requests.exceptions.Timeout as e:
            print(f"Timeout error occurred: {e}")
            return {"status": "error", "message": str(e)}
        except requests.exceptions.RequestException as e:
            print(f"An unexpected request error occurred: {e}")
            return {"status": "error", "message": str(e)}
        except ValueError as e:
            print(f"Message content error: {e}")
            return {"status": "error", "message": str(e)}

    def get_viber_account_info(self):
        url = "https://chatapi.viber.com/pa/get_account_info"
        headers = {
            "X-Viber-Auth-Token": self.viber_auth_token,
            "Content-Type": "application/json" 
        }

        try:
            response = requests.post(url, headers=headers)
            response.raise_for_status() 
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            print(f"Response content: {response.text}")
            return {"status": "error", "message": str(e), "details": response.text}
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error occurred: {e}")
            return {"status": "error", "message": str(e)}
        except requests.exceptions.Timeout as e:
            print(f"Timeout error occurred: {e}")
            return {"status": "error", "message": str(e)}
        except requests.exceptions.RequestException as e:
            print(f"An unexpected request error occurred: {e}")
            return {"status": "error", "message": str(e)}
        
