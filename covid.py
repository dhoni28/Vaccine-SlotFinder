import requests
import time
from playsound import playsound
#dist = 395      
pincode = 400070
date = '03-07-2021'
#URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(dist, date)
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode, date)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def findAvailability():
    counter = 0
    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
    for each in data:
        if(each["available_capacity"] > 0 and each["min_age_limit"] == 18 and each["available_capacity_dose1"] > 0 and each["fee"] == '0'):
            counter += 1
            print(each["name"])
            print(each["pincode"])
            print(each["vaccine"])
            print(each["available_capacity_dose1"])
            print(each["available_capacity"])
            print(each["fee_type"])
            print(each["fee"])
            playsound('C:\\Users\\admin\\Documents\\TCS NQT\\Notific.mp3')
            return True
    if(counter == 0):
        print("No Available Slots")
        return False


while(findAvailability() != True):
    time.sleep(5)
    findAvailability()

i=0
#j=50
for i in range(0, 50000):
    findAvailability()
    i = i+1
    