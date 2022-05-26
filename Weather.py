from http import server
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText

#get weather data
def Get_Weather_Data():
    driver = webdriver.Chrome('C://Users/bdcsw/Downloads/chromedriver_win32/chromedriver.exe')
    driver.get("https://www.accuweather.com/en/in/bengaluru/204108/current-weather/204108") 

    temperature = driver.find_elements_by_xpath("//body/div[1]/div[5]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]")
    temperature_data = []
    for temp in range(len(temperature)):
        temperature_data.append(temperature[temp].text)
    Temperature = "Temperature: "+ temperature_data[0]
    print(Temperature)

    time = driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/p[1]")
    time_data = []
    for t in range(len(time)):
        time_data.append(time[t].text)
    Time = "Time: "+ time_data[0]
    print(Time)
 
    wind = driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]")
    wind_data = []
    for w in range(len(wind)):
        wind_data.append(wind[w].text)
    Wind = "Wind: "+ wind_data[0]
    print(Wind)

    wind_gusts = driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]")
    windgusts_data = []
    for wg in range(len(wind_gusts)):
        windgusts_data.append(wind_gusts[wg].text)
    Wind_Gusts = "Wind gusts: "+windgusts_data[0]
    print(Wind_Gusts)

    humidity = driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[3]/div[1]/div[3]/div[2]")
    humidity_data = []
    for h in range(len(humidity)):
        humidity_data.append(humidity[h].text)
    Humidity = "Humidity: " +humidity_data[0]
    print(Humidity)
    
    pressure = driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]")
    pressure_data = []
    for p in range(len(pressure)):
        pressure_data.append(pressure[h].text)
    Pressure = "Pressure: " +pressure_data[0]
    print(Pressure)

    

    Weather = Temperature + "\n" + Time + "\n" + Wind + "\n" + Wind_Gusts + "\n" + Humidity + "\n" + Pressure
    return Weather


Weather = Get_Weather_Data()


To_ = "aditimanjrekar2@gmail.com"
From_ = "aditimanjrekar2@gmail.com"
msg = MIMEText(Weather)
msg['Subject'] = 'Weather Data From Aditi - Task 1'
msg['From'] = 'aditimanjrekar2@gmail.com'
msg['To'] = 'aditimanjrekar2@gmail.com'

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("aditimanjrekar2@gmail.com", "aditi@1203")
server.sendmail(To_, From_, msg.as_string())
server.quit()

    
    





