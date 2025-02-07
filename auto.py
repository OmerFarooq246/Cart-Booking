from concurrent.futures import ThreadPoolExecutor
from Flow import Flow
import time

staff_number = "923359950161"

# WhatsApp chat link
whatsapp_url = "https://wa.me/+923359950161?text=Hello%20I%20need%20assistance"


# flow = Flow(staff_number)
# number = "923359950161"
# flow.init_conv(number)

# with ThreadPoolExecutor() as executor:
#     while True:
#         try:
#             e1 = executor.submit(flow.process_new_customers)
#             e2 = executor.submit(flow.handle_conv_flow)
#             print(e1)
#             print(e2)
#             time.sleep(3)
#         except Exception:
#             if Exception == KeyboardInterrupt:
#                 flow.client.close()
#                 print("Stopping execution...")

# flow = Flow()
# flow.send_booking_id("67a25c7a212d05c4aba5d919")
# ap = flow.get_nearest_ap()
# res = flow.DB.Messages.find({"number": "923359950161"})
# flow.client.close()

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
