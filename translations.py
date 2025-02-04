Langs = {
    "english": {
        "introduction": "Welcome to Jawlah, a service providing easy and comfortable electric cart transportation between the Prophet’s Mosque and Quba Mosque.",
        "destination_msg": "Please choose your destination:", 
        "destinations": [
            "Prophet’s Mosque",
            "Quba Mosque"
        ],
        "passengers_prompt": "How many passengers? (Enter any number)\nNumber of passengers: n\nTotal cost: 15 SAR × n = (total) SAR",
        "total_cost": "Total cost = {total_cost} SAR",
        "location_prompt": "Please share your current location so we can find the nearest gathering point.",
        "assembly_point": "Your nearest pickup point.",
        "cc_msg": "Confirm your booking now:",
        "cc_options": [
            "Confirm", 
            "Cancel"
        ],
        "confirmation": "Your reservation is confirmed and now Active.\nThank you for using Jawlah!",
        "cencellation": "Your reservation has been canceled.\nThank you for reaching out!",
        "summary": "*Booking Summary:*\nName: {name}\nDestination: {destination}\nNo. of Passengers: {passengers}\nPickup Point: {google_maps_link}\nTotal Cost: {total_cost}\nBooking Status: {booking_status}",
        "qr_code": "Here is your booking QR code:"
    },
    "arabic": {
        "introduction": "مرحباً بك في جولة، الخدمة التي تتيح لك التنقل بسهولة وراحة باستخدام عربات كهربائية لنقلك من وإلى المسجد النبوي ومسجد قباء",
        "destination_msg": "فضلاً اختر وجهتك:", 
        "destinations": [
            "المسجد النبوي",
            "مسجد قباء"
        ],
        "passengers_prompt": "كم عدد الركاب؟ (يمكنك إدخال أي عدد)\nعدد الركاب: n\nالتكلفة الإجمالية: 15 ريال × n = (المجموع) ريال سعودي",
        "total_cost": "التكلفة الإجمالية = {total_cost} ريال سعودي",
        "location_prompt": "فضلاً شارك موقعك الحالي لتحديد أقرب نقطة تجمع.",
        "assembly_point": "تم استلام موقعك.\nأقرب نقطة تجمع لعربة الغولف هي",
        "cc_msg": "لتأكيد الحجز:",
        "cc_options": [
            "تأكيد", 
            "إلغاء"
        ],
        "confirmation": "تم تأكيد الحج\nحالة الحجز: نشط (Active)\nشكراً لاستخدامك خدمة جولة\nنتمنى لك رحلة موفقة!",
        "cencellation": "تم إلغاء الحجز\nشكراً لتواصلك معنا",
        "summary": "*Booking Summary:*\nName: {name}\nDestination: {destination}\nNo. of Passengers: {passengers}\nPickup Point: {google_maps_link}\nTotal Cost: {total_cost}\nBooking Status: {booking_status}",
        "qr_code": "هذا هو باركود الحجز الخاص بك:"
    }
}

langs_list = [ "english", "arabic", "urdu", "turkish", "french" ]
dests_list = [ "Prophet’s Mosque", "Quba Mosque" ]
cc_list = ["confirm", "cancel"]