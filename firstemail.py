import requests
import smtplib
response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=332001&date=11-05-2021")
print(response.text)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("sender@gmail.com", "*******")
server.sendmail("sender@gmail.com", "reciever@gmail.com", "wait")
server.quit()
