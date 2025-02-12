from concurrent.futures import ThreadPoolExecutor
from Flow import Flow
import time

staff_number = "923359950161"
scan_msg = "Salam Alykom\nI would like to book a Cart from Jawlah"
flow = Flow(staff_number, scan_msg)
number = "923359950161"

with ThreadPoolExecutor() as executor:
    while True:
        try:
            # e1 = executor.submit(flow.process_new_customers)
            e2 = executor.submit(flow.handle_conv_flow)
            # print(e1)
            print(e2)
            time.sleep(3)
        except Exception:
            if Exception == KeyboardInterrupt:
                flow.client.close()
                print("Stopping execution...")

#-----------------------------------------------------------------

# from Flow import Flow
# import urllib.parse
# from dotenv import load_dotenv
# import os
# load_dotenv()

# staff_number = "923359950161"
# scan_msg = "Salam Alykom\nI would like to book a Cart from Jawlah"
# flow = Flow(staff_number, scan_msg)
# message = urllib.parse.quote(scan_msg)
# data = f"https://wa.me/{os.getenv("PHONE_NUMBER")}?text={message}"
# img_path = "/Users/traveler/Desktop/VSCODEs/Cart Booking/initial_qr_code.png"
# logo_path =  "/Users/traveler/Desktop/VSCODEs/Cart Booking/logo.png"
# flow.generate_qr_code(data, img_path)

#-----------------------------------------------------------------

# +923359950161
# +923200577069

# from WhatsApp_Messages import WhatsApp_Messages
# wa_msg = WhatsApp_Messages(15)
# number="923359950161"

# flow = Flow(number)
# ap = flow.get_nearest_ap()
# msg = f"Nearest Pickup Point:\n{ap["link"]}"
# print(msg)
# res = wa_msg.send_text_message(number, msg)
# print(res)
# print(res.json())

# # res = wa_msg.send_select_language_list(number)

# img_link="https://cart-booking-serve.vercel.app/uploads/image.png"
# message = f"Booking QR Code:"
# print(message)
# res = wa_msg.send_qr_code(number, message, img_link)
# print(res.text)
# print(res)
# img_path = "/Users/traveler/Desktop/VSCODEs/Cart Booking/qr_codes/679a6cfe00f0a8211748ba4a.png"
# img_id = wa_msg.upload_qr_img(img_path)
# print(f"img_id: {img_id}")
# res = wa_msg.send_qr_code(number, img_link)
# print(res)
# print(res.text)
# res = wa_msg.download_media(img_id)
# print(res.json())

# # ="938964078418613"

# from dotenv import load_dotenv
# import requests
# import os
# from translations import Langs
# from PIL import Image

# load_dotenv()

# media_url = f"https://graph.facebook.com/v22.0/{9651909331508358}?debug=all"
# headers = {
#     "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"
# }
# res = requests.get(media_url, headers=headers)
# print(res)
# print(res.json())  # Should return metadata about the image
