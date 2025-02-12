from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
import requests
from WhatsApp_Messages import WhatsApp_Messages
from translations import langs_list, Langs, cc_list, dests_list, locations_list
from datetime import datetime
import qrcode
import numpy as np
from PIL import Image

'''
customer.status = 
    - new: wlcome message sent
    - start: reply to welcome message found
    - lang: select lang sent
    - dest: destination prompt sent
    - psgr: passenger promt sent
    - loct: location prompt sent
    - coca: confirmation/cancelation message sent
    - done: flow of conv completed
'''


load_dotenv()
wa_msg = WhatsApp_Messages(15)

class Flow:
    def __init__(self, staff_number, scan_msg):
        self.client = MongoClient(os.getenv("MONGO_URI"), server_api=ServerApi('1'), tls=True, tlsCAFile=certifi.where())
        self.DB = self.client["Cart_Booking"]
        self.staff_number = staff_number
        self.scan_msg = scan_msg

    def init_conv(self, number):
        try:
            res = self.handle_conv_init(number)
        except Exception as error:
            print("error in init_conv:", error)

    # def handle_conv_init(self, number):
    #     try:
    #         res = self.DB.Cutomers.find_one({ "number" : number })
    #         if res:
    #             if res["status"] == "done":
    #                 entry = {
    #                     "number": number,
    #                     "name": res["name"],
    #                     "status": "lang"
    #                 }
    #                 res = self.DB.Cutomers.insert_one(entry)
    #                 res = wa_msg.send_select_language_list(number)
    #             else:
    #                 print("Process Failure, New Conv init with previous not done")
    #         else:
    #             entry = {
    #                 "number": number,
    #                 "status": "new"
    #             }
    #             res = self.DB.Cutomers.insert_one(entry)
    #             res = wa_msg.send_welcome_message(number)
    #     except Exception as error:
    #         print(f"Error in handle_conv_init = {error}")

    # def process_new_customers(self): #meant to run continuously in a separate thread
    #     try:
    #         msgs = self.DB.Messages.find({ "read": False })
    #         if msgs:
    #             for msg in msgs:
    #                 number = msg["from"]
    #                 new_customer = list(self.DB.Cutomers.find({ "number" : number, "status": "new" }))
    #                 print(f"new_customer: {new_customer}")
    #                 if new_customer:
    #                     if len(new_customer) > 1:
    #                         print("Process Failure, More than one NEW entries for a number")
    #                     else:
    #                         new_customer = new_customer[0]
    #                         print(f"new_customer: {new_customer}")
    #                         print("reply to welcome msg found")
    #                         name = msg["msg"]
    #                         res = wa_msg.send_select_language_list(number)
    #                         res = self.DB.Cutomers.update_one({ "_id": new_customer["_id"] }, { "$set": { "name": name, "status": "lang" } })
    #                         res = self.DB.Messages.update_one({ "_id": msg["_id"] }, { "$set": { "read": True } })
    #         else:
    #             print("no unread messages")
    #     except Exception as error:
    #         print(f"Error in process_new_customers = {error}")

    def handle_conv_flow(self):
        try:
            msgs = self.DB.Messages.find({ "read": False })
            if msgs:
                for msg in msgs:
                    res = self.DB.Messages.update_one({ "_id": msg["_id"] }, { "$set": { "read": True } })
                    number = msg["from"]
                    # customer_list = list(self.DB.Cutomers.find({ "number" : number, "status": { "$ne": "new" } }))
                    customer_list = list(self.DB.Cutomers.find({ "number" : number}))
                    
                    if msg["type"] == "text":
                        if msg["msg"] == self.scan_msg:
                            print(f"new scan found: +{number}")
                            result = self.DB.Cutomers.update_many({"number": number}, {"$set": {"status": "done"}})
                            new_conv_msg = "Starting a new booking, previous one has been cancelled."
                            res = wa_msg.send_text_message(number, new_conv_msg)
                            print(res.json())
                            entry = {
                                "number": number,
                                "status": "lang"
                            }
                            res = self.DB.Cutomers.insert_one(entry)
                            res = wa_msg.send_select_language_list(number)
                            print(res.json())
                            print("handled new scan")
                            continue
                    
                    print(f"customer_list: {customer_list}")
                    if customer_list:
                        customer_start = list(filter(lambda item: item["status"] == "start", customer_list))
                        customer_lang = list(filter(lambda item: item["status"] == "lang", customer_list))
                        customer_dest = list(filter(lambda item: item["status"] == "dest", customer_list))
                        customer_psgr = list(filter(lambda item: item["status"] == "psgr", customer_list))
                        customer_loct = list(filter(lambda item: item["status"] == "loct", customer_list))
                        customer_coca = list(filter(lambda item: item["status"] == "coca", customer_list))
                        if len(customer_start) > 1:
                                print("Process Failure, More than one START entries for a number")
                                continue
                        if len(customer_lang) > 1:
                                print("Process Failure, More than one LANG entries for a number")
                                continue
                        if len(customer_dest) > 1:
                                print("Process Failure, More than one DEST entries for a number")
                                continue
                        if len(customer_psgr) > 1:
                                print("Process Failure, More than one PSGR entries for a number")
                                continue
                        if len(customer_loct) > 1:
                                print("Process Failure, More than one LOCT entries for a number")
                                continue
                        if len(customer_coca) > 1:
                                print("Process Failure, More than one COCA entries for a number")
                                continue
                        
                        for customer in customer_list:
                            if customer["status"] == "start":
                                res = wa_msg.send_select_language_list(number)
                                res = self.DB.Cutomers.update_one({ "_id": customer["_id"] }, { "$set": { "status": "lang" } })
                            elif customer["status"] == "lang":
                                selected_lang = msg["msg"].lower()
                                if selected_lang not in langs_list:
                                    print("sending lang emaphasis msg")
                                    select_lan_emphasis = "Please select language from the list"
                                    res = wa_msg.send_text_message(number, select_lan_emphasis)
                                else:
                                    res = self.DB.Cutomers.update_one({ "_id": customer["_id"] }, { "$set": { "lang": selected_lang } })
                                    res = wa_msg.send_text_message(number, Langs[selected_lang]["introduction"])
                                    res = wa_msg.send_select_destination(number, selected_lang)
                                    res = self.DB.Cutomers.update_one({ "_id": customer["_id"] }, { "$set": { "status": "dest" } })
                            elif customer["status"] == "dest":
                                type = msg["type"]
                                selected_dest = msg["msg"]
                                if type == "interactive" and selected_dest in dests_list:
                                    res = self.DB.Cutomers.update_one({ "_id": customer["_id"] }, { "$set": { "dest": selected_dest } })
                                    res = wa_msg.send_text_message(number, Langs[customer["lang"]]["passengers_prompt"])
                                    res = self.DB.Cutomers.update_one({ "_id": customer["_id"] }, { "$set": { "status": "psgr" } })
                                else:
                                    print("sending dest emaphasis msg")
                                    loct_emphasis = "Please select destination"
                                    res = wa_msg.send_text_message(number, loct_emphasis)
                            elif customer["status"] == "psgr":
                                psgr_no_txt = msg["msg"]
                                try:
                                    psgr_no = int(psgr_no_txt)
                                except Exception as e:
                                    print("sending psgr emaphasis msg")
                                    psgr_emphasis = "Please enter a number"
                                    res = wa_msg.send_text_message(number, psgr_emphasis)
                                    continue
                                res = self.DB.Cutomers.update_one({ "_id": customer["_id"] }, { "$set": { "psgr": psgr_no } })
                                total_cost_msg = Langs[customer["lang"]]["total_cost"].format(total_cost = psgr_no * wa_msg.cost_per_passenger)
                                res = wa_msg.send_text_message(number, total_cost_msg)
                                res = wa_msg.location_req_msg(number, customer["lang"])
                                res = self.DB.Cutomers.update_one({ "_id": customer["_id"] }, { "$set": { "status": "loct" } })
                            elif customer["status"] == "loct":
                                try:
                                    if (isinstance(msg["msg"], dict)):
                                        location = msg["msg"]
                                        lati = location["latitude"]
                                        long = location["longitude"]
                                        ap_location = self.get_nearest_ap(lati, long)
                                        ap_maps_link = f"https://www.google.com/maps?q={ap_location[0]},{ap_location[1]}"
                                        loc_obj = {
                                            "link": ap_maps_link,
                                            "latitude": ap_location[0],
                                            "longitude": ap_location[1],
                                        }
                                        print(f"loc_obj= {loc_obj}")
                                        print(f"loc_obj[link]: {loc_obj["link"]}")
                                        ap_msg = f"{Langs[customer["lang"]]["assembly_point"]}\n{ap_maps_link}"
                                        res = wa_msg.send_text_message(number, ap_msg)
                                        res, total_cost = wa_msg.send_summary(number, customer["lang"], customer["dest"], customer["psgr"], loc_obj["link"], "Awaiting Confirmation")
                                        res = wa_msg.send_cc_msg(number, customer["lang"])
                                        updates = {
                                            "status": "coca",
                                            "nearest_ap": loc_obj,
                                            "location": location,
                                            "total_cost": total_cost
                                        }
                                        res = self.DB.Cutomers.update_one({ "_id": customer["_id"] }, { "$set": updates })
                                    else:
                                        print("sending loct emaphasis msg")
                                        loct_emphasis = "Please send your location"
                                        res = wa_msg.send_text_message(number, loct_emphasis)
                                except Exception as e:
                                    print(f"exception caught in loc: {e}")
                                    print("sending loct emaphasis msg")
                                    loct_emphasis = "Please send your location"
                                    res = wa_msg.send_text_message(number, loct_emphasis)
                                    continue
                            elif customer["status"] == "coca":
                                result = msg["msg"]
                                if result not in cc_list:
                                    print("sending coca emaphasis msg")
                                    loct_emphasis = "Please select confirm or cancel"
                                    res = wa_msg.send_text_message(number, loct_emphasis)
                                else:
                                    if result == "confirm":
                                        booking = {
                                            "customer_id": customer["_id"],
                                            "number": customer["number"],
                                            "language": customer["lang"],
                                            "destination": customer["dest"],
                                            "passengers": customer["psgr"],
                                            "total_cost": customer["total_cost"],
                                            "location": customer["location"],
                                            "ap_point": customer["nearest_ap"],
                                            "status": "active",
                                            "timestamp": datetime.now(),
                                        }
                                        booking_id = self.DB.Bookings.insert_one(booking).inserted_id
                                        res = wa_msg.send_text_message(number, Langs[customer["lang"]]["confirmation"])
                                        qrUrl = self.send_booking_id(booking_id)
                                        res = wa_msg.send_qr_code(number, Langs[customer["lang"]]["qr_code"], qrUrl)
                                        #sending booking details to staff member
                                        self.send_details_staff(booking)
                                    # else:
                                        # res = wa_msg.send_text_message(number, Langs[customer["lang"]]["cencellation"])
                                    res = self.DB.Cutomers.update_one({ "_id": customer["_id"] }, { "$set": { "status": "done" } })
                            else:
                                print(" -- unkown status found --")
            else:
                print(f"no in progress convs found")

        except Exception as error:
            print(f"Error in handle_conv_flow = {error}")

    def send_booking_id(self, booking_id):
        try:
            serve_url = f"{os.getenv("SERVE")}/api/generate_qr"
            data = {
                "booking_id": str(booking_id)
            }
            res = requests.post(serve_url, json=data)
            qrUrl = res.json()["qrUrl"]
            print(f"res of send_booking_id: {qrUrl}")
            return f"{os.getenv("SERVE")}{qrUrl}"
        except Exception as error:
            print(f"error in send_booking_id: ", error)

    def send_details_staff(self, booking):
        details_dict = {
            "number": booking["number"],
            "destination": booking["destination"],
            "passengers": booking["passengers"],
            "total cost": booking["total_cost"],
            "cutomer location": f"https://www.google.com/maps?q={booking["location"]["latitude"]},{booking["location"]["longitude"]}",
            "pickup point": booking["ap_point"]["link"],
            "time": booking["timestamp"].strftime("%H:%M, %d %B %Y")
        }
        details = self.dict_to_string(details_dict)
        res = wa_msg.send_text_message(self.staff_number, details, preview=False)

    def get_nearest_ap(self, lati, long):
        try:
            all_locations = locations_list
            all_locations.append([long, lati])
            base_url = os.getenv("FOOT_WALKING_URL")
            key = os.getenv("OPEN_ROUTE_KEY")
            headers = {
               'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
                'Authorization': key,
                'Content-Type': 'application/json; charset=utf-8'
            }
            body = {
                "locations": all_locations,
                "destinations": [len(all_locations)-1],
                "metrics":["distance"]
            }
            res = requests.post(base_url, json=body, headers=headers)
            print(f"res of get_nearest_ap = {res.json()["distances"]}")
            distances = np.array(res.json()["distances"]).squeeze()
            print(f"distances: {distances}")
            min_index = np.argmin(distances[:-1])
            print(f"min_index: {min_index}")
            min_loc = locations_list[min_index]
            print(f"min_loc: {min_loc}")
            return min_loc
        except Exception as error:
            print(f"error in get_nearest_ap: ", error)
    
    def dict_to_string(self, dict_obj):
        string = ""
        for key, value in dict_obj.items():
            print(f"vale: {value}")
            if isinstance(value, dict):
                string += f"{key}:\n{self.dict_to_string(value)}"
            else:
                string += f"{key}: {value}\n"
        return string
    
    def generate_qr_code(self, data, img_path, logo_path=None, logo_scale=0.2):
        try:
            qr = qrcode.QRCode(
                version=5,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
            if logo_path:
                logo = Image.open(logo_path)
                qr_width, qr_height = img.size
                max_logo_size = int(min(qr_width, qr_height) * logo_scale)  # 20% of QR code size
                logo = logo.resize((max_logo_size, max_logo_size), Image.LANCZOS)

                # Calculate logo position (center)
                logo_x = (qr_width - max_logo_size) // 2
                logo_y = (qr_height - max_logo_size) // 2

                # Paste logo onto QR code
                img.paste(logo, (logo_x, logo_y), logo)
            else:
                pass
            img.save(img_path)
        except Exception as error:
            print(f"error in generating qr code: ", error)