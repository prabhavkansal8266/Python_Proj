import requests
import json
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

city = input("Enter the name of the city \n")

url = f"https://api.weatherapi.com/v1/current.json?key=27aeb9544a454cb49ff51336252707&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
# print("The temperatur is ",wdic["current"]["temp_c"])
w = wdic["current"]["temp_c"]

speak(f"The current weather in {city} is is {w} degrees")
print("The temperature is ",wdic["current"]["temp_c"])