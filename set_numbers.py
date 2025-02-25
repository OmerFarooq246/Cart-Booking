from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
import os

try: 
  main_number = "923359950161"
  staff_number = "923359950161"
  
  client = MongoClient(
    os.getenv("MONGO_URI"), 
    server_api=ServerApi('1'), 
    tls=True, tlsCAFile=certifi.where()
  )
  DB = client["Cart_Booking"]

  DB.Numbers.delete_many({})
  DB.Numbers.insert_many(
    [{
      "number": main_number,
      "type": "main"
    },
    {
      "number": staff_number,
      "type": "staff"
    }]
  )
  client.close()
except Exception as error:
  print(f"error in set_numbers: {error}")