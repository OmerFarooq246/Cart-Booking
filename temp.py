from Flow import Flow
from translations import langs_list, Langs, cc_list, dests_list, locations_list

scan_msg = "Salam Alykom\nI would like to book a Cart from Jawlah"
flow = Flow(scan_msg)

ap = flow.get_nearest_ap(24.489074707031, 39.699295043945)
print(ap)