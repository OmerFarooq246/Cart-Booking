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
# res = flow.DB.Messages.find({"number": "923359950161"})
# flow.client.close()

# # +923359950161
# # +923200577069

# from WhatsApp_Messages import WhatsApp_Messages
# wa_msg = WhatsApp_Messages(15)
# res = wa_msg.location_req_msg(+923359950161, "english")
# print(res.text)