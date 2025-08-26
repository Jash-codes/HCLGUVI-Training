import random
import pywhatkit as p
otp = random.randint(100000, 999999)
phone_number = "+918939299158"  
message = f"Your OTP is: {otp}"
p.sendwhatmsg_instantly(phone_no=phone_number, message=message)
print("OTP sent:", otp)
