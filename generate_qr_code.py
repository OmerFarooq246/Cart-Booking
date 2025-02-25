import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse
from dotenv import load_dotenv
import os
load_dotenv()
from PIL import Image
import qrcode

def generate_qr_code(data, img_path, logo_path=None, logo_scale=0.2):
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


client = MongoClient(
    os.getenv("MONGO_URI"), 
    server_api=ServerApi('1'), 
    tls=True, tlsCAFile=certifi.where()
)
DB = client["Cart_Booking"]
main_number = DB.Numbers.find_one({ "type": "main" })

scan_msg = "Salam Alykom\nI would like to book a Cart from Jawlah"
message = urllib.parse.quote(scan_msg)
data = f"https://wa.me/+{main_number}?text={message}"
img_path = "./initial_qr_code_logo_test.png"
logo_path =  "./logo.png"
generate_qr_code(data, img_path, logo_path)