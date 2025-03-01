# from concurrent.futures import ThreadPoolExecutor
from Flow import Flow
import time

scan_msg = "Salam Alykom\nI would like to book a Cart from Jawlah"
flow = Flow(scan_msg)

while True:
    try:
        flow.handle_conv_flow()
        time.sleep(3)
    except Exception:
        if Exception == KeyboardInterrupt:
            flow.client.close()
            print("Stopping execution...")

# with ThreadPoolExecutor() as executor:
#     while True:
#         try:
#             e1 = executor.submit(flow.handle_conv_flow)
#             print(e1)
#             time.sleep(3)
#         except Exception:
#             if Exception == KeyboardInterrupt:
#                 flow.client.close()
#                 print("Stopping execution...")