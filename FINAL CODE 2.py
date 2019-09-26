import json, requests
import urllib.request
import time 
print("---Welcome to NASA Polar quest---\n\n")
time.sleep(2)
print("Choose a polar quest region\n")
time.sleep(1)
print("1) The Arctic\n\nThe Arctic is a polar region located at the northernmost part of Earth. The Arctic consists of the Arctic Ocean, adjacent seas, and parts of Alaska (United States), Finland, Greenland (Denmark), Iceland, Northern Canada, Norway, Russia and Sweden. Land within the Arctic region has seasonally varying snow and ice cover, with predominantly treeless permafrost (permanently frozen underground ice)-containing tundra. Arctic seas contain seasonal sea ice in many places.\n\n ")
time.sleep(1)
print("2) The Antartic\n\nThe Antartic is Earth's southernmost continent. It contains the geographic South Pole and is situated in the Antarctic region of the Southern Hemisphere, almost entirely south of the Antarctic Circle, and is surrounded by the Southern Ocean. At 14,200,000 square kilometres (5,500,000 square miles), it is the fifth-largest continent and nearly twice the size of Australia. At 0.00008 people per square kilometre, it is by far the least densely populated continent. About 98% of Antarctica is covered by ice that averages 1.9 km (1.2 mi; 6,200 ft) in thickness,[5] which extends to all but the northernmost reaches of the Antarctic Peninsula. \n")
choice1=int(input("\n Enter your choice:"))
if choice1 == 1:
   latitude = 76
   longitude = 100
elif choice1 == 2:
   latitude = -82
   longitude = -135

print("Hello Adventurer, would you like to analyze:\n1) PAST WEATHER AT YOUR DESTINATION?\n2) PRESENT WEATHER AT YOUR DESTINATION?\n3) FUTURE WEATHER AT YOUR DESTINATION? ")
choice2=int(input("\n Enter your choice:"))
if choice2 == 1:
    print("\nHello adventurer, please enter the day of your quest:")
    YYYY=str(input("\n Enter the year[1971-present]:"))
    MM=str(input("\n Enter the month [1-12]:")) 
    DD=str(input("\n Enter the date [1-31]:"))
    HH=str(input("\n Enter the hour [01-24]:"))
    MI=str(input("\n Enter the minutes [0-60]:"))
    SS=str(input("\n Enter the seconds [0-60]:"))
    #r1 = requests.get("https://api.darksky.net/forecast/428cd4ae2c1240d3512b738a94989431/" + str(latitude) + "," + str(longitude) + "," + "2015-03-14T05:30:40")
    r1 = requests.get("https://api.darksky.net/forecast/428cd4ae2c1240d3512b738a94989431/" + str(latitude)+ "," + str(longitude) + "," + YYYY + "-" + MM + "-" + DD + "T" + HH + ":" + MI + ":" + SS)
    data = r1.json()
    print("Day Weather was",data['currently']['summary'])
    print("Night weather was ",data['currently']['icon'])
    print("UV Index was ",data['currently']['uvIndex'])
elif choice2 == 2: 
    r = requests.get("https://api.darksky.net/forecast/428cd4ae2c1240d3512b738a94989431/" + str(latitude) + "," + str(longitude) + "?" + "units=si")
    data2 = r.json()
    print("Temperature is ",data2['currently']['temperature'],"C")
    print("Wind Speed is ",data2['currently']['windSpeed'],"mph")
else:
    r2 = requests.get("https://api.darksky.net/forecast/428cd4ae2c1240d3512b738a94989431/" + str(latitude) + "," + str(longitude) + "?" + "units=si")
    data2 = r2.json()
    print("Weather forecast:",data2['daily']['summary'])
    print("Terrain:",data2['daily']['icon'])



