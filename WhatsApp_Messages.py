from dotenv import load_dotenv
import requests
import os
from translations import Langs
from PIL import Image

load_dotenv()

class WhatsApp_Messages():
    def __init__(self, cost_per_passenger = 15):
        self.url = f"https://graph.facebook.com/v22.0/{os.getenv("PHONE_ID")}/messages"
        self.cost_per_passenger = cost_per_passenger

    def send_welcome_message(self, number):
        try:
            headers = {
                "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}",
                "Content-Type": "application/json",
            }
            data = {
                "messaging_product": "whatsapp",
                "to": f"+{number}",
                "type": "template",
                "template": {"name": "hello_world", "language": {"code": "en_US"}},
            }

            res = requests.post(self.url, headers=headers, json=data)
            print(f"res of welcome message: {res.text}")
            return res
        except Exception as error:
            raise Exception(f"Error in send_welcome_message = {error}")
        
    def send_select_language_list(self, number):
        try:
            headers = {
                "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}",
                "Content-Type": "application/json",
            }
            data = {
                "messaging_product": "whatsapp",
                "to": f"+{number}",
                "type": "interactive",
                "interactive": {
                    "type": "list",
                    "body": {"text": "Select Language"},
                    "action": {
                        "sections": [
                            {
                            "title": "Languages",
                            "rows": [
                                { "id": "Arabic", "title": "Arabic" },
                                { "id": "English", "title": "English" },
                                { "id": "Urdu", "title": "Urdu" },
                                { "id": "Turkish", "title": "Turkish" },
                                { "id": "French", "title": "French" },
                            ]
                            }
                        ],
                        "button": "Languages List",
                    }
                },
            }
            res = requests.post(self.url, headers=headers, json=data)
            return res
        except Exception as error:
            raise Exception(f"Error in send_select_language = {error}")
        
    def send_select_language_int(self, number):
        try:
            headers = {
                "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}",
                "Content-Type": "application/json",
            }
            data = {
                "messaging_product": "whatsapp",
                "to": f"+{number}",
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {"text": "Select Language"},
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {"id": "Arabic", "title": "Arabic"},
                            },
                            {
                                "type": "reply",
                                "reply": {"id": "English", "title": "English"},
                            },
                            {
                                "type": "reply",
                                "reply": {"id": "Urdu", "title": "Urdu"},
                            },
                            {
                                "type": "reply",
                                "reply": {"id": "Turkish", "title": "Turkish"},
                            },
                            {
                                "type": "reply",
                                "reply": {"id": "French", "title": "French"},
                            },
                        ]
                    },
                },
            }
            res = requests.post(self.url, headers=headers, json=data)
            return res
        except Exception as error:
            raise Exception(f"Error in send_select_language = {error}")
    
    def send_select_destination(self, number, lang):
        try:
            headers = {
                "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}",
                "Content-Type": "application/json",
            }
            data = {
                "messaging_product": "whatsapp",
                "to": f"+{number}",
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {"text": Langs[lang]["destination_msg"]},
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {"id": "Prophet’s Mosque", "title": Langs[lang]["destinations"][0]},
                            },
                            {
                                "type": "reply",
                                "reply": {"id": "Quba Mosque", "title": Langs[lang]["destinations"][1]},
                            },
                        ]
                    },
                },
            }
            res = requests.post(self.url, headers=headers, json=data)
            return res
        except Exception as error:
            raise Exception(f"Error in send_select_destination = {error}")
    
    def send_text_message(self, number, msg): #used for passengers prompt, 
        try:
            headers = {
                "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}",
                "Content-Type": "application/json",
            }
            data = {
                "messaging_product": "whatsapp",
                "to": f"+{number}",
                "type": "text",
                "text": {
                    "preview_url": 1 == 1,
                    "body": msg
                },
            }
            res = requests.post(self.url, headers=headers, json=data)
            return res
        except Exception as error:
            raise Exception(f"Error in send_text_message -> {msg} = {error}")
    
    def location_req_msg(self, number, lang):
        try:
            headers = {
                "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}",
                "Content-Type": "application/json",
            }
            data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "type": "interactive",
                "to": f"+{number}",
                "interactive": {
                    "type": "location_request_message",
                    "body": {
                        "text": Langs[lang]["location_prompt"]
                    },
                    "action": {
                        "name": "send_location"
                    }
                }
            }
            res = requests.post(self.url, headers=headers, json=data)
            return res
        except Exception as error:
            raise Exception(f"Error in location_req_msg = {error}")
    
    def send_nearest_ap(self, number, lang, ap_location):
        try:
            headers = {
                "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}",
                "Content-Type": "application/json",
            }
            data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "location",
                "location": {
                    "latitude": ap_location["latitude"],
                    "longitude": ap_location["longitude"],
                    "name": Langs[lang]["assembly_point"]
                }
            }
            # data = {
            #     "messaging_product": "whatsapp",
            #     "recipient_type": "individual",
            #     "to": f"+{number}",
            #     "type": "text",
            #     "text": {
            #         "body": Langs[lang]["assembly_point"].format(google_maps_link=link)
            #     }
            # }
            res = requests.post(self.url, headers=headers, json=data)
            return res
        except Exception as error:
            raise Exception(f"Error in send_nearest_ap = {error}")
    
    def send_summary(self, number, name, lang, destination, passengers, google_maps_link, booking_status):
        try:
            total_cost = self.cost_per_passenger * passengers
            headers = {
                "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}",
                "Content-Type": "application/json",
            }
            data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": f"+{number}",
                "type": "text",
                "text": {
                    # "preview_url": google_maps_link,
                    "body": Langs[lang]["summary"].format(
                        name=name,
                        destination=destination,
                        passengers=passengers,
                        google_maps_link=google_maps_link,
                        total_cost=total_cost,
                        booking_status=booking_status
                    )
                }
            }
            res = requests.post(self.url, headers=headers, json=data)
            return res, total_cost
        except Exception as error:
            raise Exception(f"Error in send_summary = {error}")
    
    def send_cc_msg(self, number, lang):
        try:
            headers = {
                "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}",
                "Content-Type": "application/json",
            }
            data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": f"+{number}",
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {
                        "text": Langs[lang]["cc_msg"]
                    },
                    "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "confirm",
                                "title": Langs[lang]["cc_options"][0]
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "cancel",
                                "title": Langs[lang]["cc_options"][1]
                            }
                        }
                    ]
                    }
                }
            }
            res = requests.post(self.url, headers=headers, json=data)
            return res
        except Exception as error:
            raise Exception(f"Error in send_cc_msg = {error}")
        
    def upload_qr_img(self, img_path):
        media_url = f"https://graph.facebook.com/v22.0/{os.getenv("PHONE_ID")}/media"
        try:
            headers = {
                "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}"
            }
            data = {
                "messaging_product": "whatsapp",
                "type": "image/png",
                "is_reusable": True
            }
            files = {
                "file": (img_path, open(img_path, "rb"), "image/png")
            }
            res = requests.post(media_url, headers=headers, data=data, files=files)
            print(f"res of upload: {res.json()}")
            if res.status_code == 200:
                img_id = res.json().get("id")
                return img_id
            else:
                raise Exception(f"Error in upload_qr_img = {res.text}")
        except Exception as error:
            raise Exception(f"Error in upload_qr_img = {error}")

    def send_qr_code(self, number, msg, img_link):
        try:
            headers = {
                "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}",
                "Content-Type": "application/json",
            }
            data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": f"+{number}",
                "type": "image",
                "image": {
                    "link": img_link,
                    "caption": msg
                }
            }
            res = requests.post(self.url, headers=headers, json=data)
            return res
        except Exception as error:
            raise Exception(f"Error in send_qr_code = {error}")
        
    # def download_media(self, img_id):
    #     try:
    #         media_url = f"https://graph.facebook.com/v17.0/{img_id}"
    #         headers = {
    #             "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}"
    #         }
    #         res = requests.get(media_url, headers=headers)
    #         return res
    #     except Exception as error:
    #         raise Exception(f"Error in send_text_mesend_qr_codessage = {error}")