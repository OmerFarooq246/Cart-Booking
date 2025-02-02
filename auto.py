from concurrent.futures import ThreadPoolExecutor
from Flow import Flow
import time

flow = Flow()
flow.init_conv()
# flow.process_new_customers()

with ThreadPoolExecutor() as executor:
    while True:
        try:
            e1 = executor.submit(flow.process_new_customers)
            # e2 = executor.submit(flow.init_conv)
            e3 = executor.submit(flow.handle_conv_flow)
            print(e1)
            # print(e2)
            print(e3)
            time.sleep(3)
        except Exception:
            if Exception == KeyboardInterrupt:
                flow.client.close()
                print("Stopping execution...")

# flow = Flow()
# ap = flow.get_nearest_ap()
# # res = flow.DB.Messages.find({"number": "923359950161"})
# # flow.client.close()

# # +923359950161
# # +923200577069

# from WhatsApp_Messages import WhatsApp_Messages
# wa_msg = WhatsApp_Messages(15)
# number="923359950161"


# res = wa_msg.send_select_language_list(number)

# img_link="https://cart-booking-serve.vercel.app/uploads/image.png"
# message = f"Booking QR Code:\n{img_link}"
# res = wa_msg.send_text_message(number, message)
# print(res.text)
# img_path = "/Users/traveler/Desktop/VSCODEs/Cart Booking/qr_codes/679a6cfe00f0a8211748ba4a.png"
# img_id = wa_msg.upload_qr_img(img_path)
# print(f"img_id: {img_id}")
# res = wa_msg.send_qr_code(number, img_id)
# print(res)
# print(res.text)
# # res = wa_msg.download_media(img_id)
# # print(res.json())

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
