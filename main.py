import streamlit as st
st.set_page_config("ThingSpeak - Cloud",layout="wide")
codee = '''
LED Blinking:
------------

import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) 
while True: 
 GPIO.output(11, GPIO.HIGH) 
 sleep(1) 
 GPIO.output(11, GPIO.LOW) 
 sleep(1) 

****************************************************************************


LED ON_OFF Serial Display:
-------------------------


import RPi.GPIO as GPIO
import time

LED_PIN = 17 


GPIO.setwarnings(False) 


GPIO.setmode(GPIO.BCM) 


GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)  

        
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)  

except KeyboardInterrupt:
    
    GPIO.cleanup()
    print("Program terminated and GPIO cleaned up.")


**************************************************************************

Pi Camera Enter the number of Picture to take options:
-----------------------------------------------------

from picamera2 import Picamera2, Preview
from time import sleep
from libcamera import Transform

picam2 = Picamera2()


no = int(input("Enter the number of photos to take :"))

picam2.start_preview(Preview.QTGL, transform=Transform(hflip=True, vflip=True))

picam2.start()
for i in range(1,no+1):
    
    picam2.start_and_capture_file(f"/home/project/Pictures/new_image_{i}.jpg")
    sleep(2)
picam2.stop_preview()
picam2.close()


*************************************************************************
Pi Camera take Picture:
----------------------


import time
from picamera2 import Picamera2, Preview
picam = Picamera2()
config = picam.create_preview_configuration()
picam.configure(config)
picam.start_preview(Preview.QTGL)
picam.start()
time.sleep(2)
picam.capture_file("test-python.jpg")
picam.close()


****************************************************************************
Pi Camera take Video:
--------------------

from libcamera import Transform
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
import RPi.GPIO as GPIO
from time import sleep

picam2 = Picamera2()
sensorpin=11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorpin,GPIO.IN)
video_config = picam2.create_video_configuration()
picam2.configure(video_config)


while True:
    if GPIO.input(sensorpin) == 0:
        encoder = H264Encoder(10000000)
        picam2.start_preview(Preview.QTGL, transform=Transform(hflip=True, vflip=True))
        picam2.start_recording(encoder, 'myvideo.h264')
        sleep(5)
        picam2.stop_recording()
        picam2.stop_preview()
        
    else:
        print('No object detected')
    sleep(2)


*******************************************************************************

IR Camera take Picture:
----------------------

from picamera2 import Picamera2, Preview
from time import sleep
from libcamera import Transform
import RPi.GPIO as GPIO

picam2 = Picamera2()
sensorpin=11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorpin,GPIO.IN)
while True:
    if GPIO.input(sensorpin) == 0:
        picam2.start_preview(Preview.QTGL, transform=Transform(hflip=True, vflip=True))
        picam2.start()
        picam2.start_and_capture_file(f"/home/project/Pictures/ir_cap_img.jpg")
        sleep(2)
        picam2.stop_preview()
        picam2.stop()
        
    else:
        print('No object detected')
    sleep(2)



************************************************************************************

IR Sensor with take Video:
-------------------------


from libcamera import Transform
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
import RPi.GPIO as GPIO
from time import sleep

picam2 = Picamera2()
sensorpin=11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorpin,GPIO.IN)
video_config = picam2.create_video_configuration()
picam2.configure(video_config)


while True:
    if GPIO.input(sensorpin) == 0:
        encoder = H264Encoder(10000000)
        picam2.start_preview(Preview.QTGL, transform=Transform(hflip=True, vflip=True))
        picam2.start_recording(encoder, 'myvideo.h264')
        sleep(5)
        picam2.stop_recording()
        picam2.stop_preview()
        
    else:
        print('No object detected')
    sleep(2)



***********************************************************************************
IR Sensor with LED On_Off:
-------------------------


import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(18,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(17,IO.IN) #GPIO 14 -> IR sensor as input
while 1:
    if(IO.input(17)==True): #object is far away
        
        IO.output(18,False) # Green led OFF
    if(IO.input(17)==False): #object is near
        IO.output(18,True) #Green led ON
        

**************************************************************************************

Install adafruit-circuitpython-dht 11 & 22:
------------------------------------------


>>>python3 -m venv VE1

>>>source VE1/bin/activate


>>>python3 -m pip install adafruit-circuitpython-dht


pip install RPi.GPIO  (for Linux os all)

sudo apt-get install libgpiod2   (for linux os 11 only)



>>>python3 dht11.py


By Using Run from Terminal with source path

(VE1) pi@raspi:~/Downloads $ python dht11.py


PIN CONFIG:

PIN 2 VCC
PIN 6 GND
PIN 11 DATA PIN




DHT 11 Temperature & Humidity Sensor Py Code:
--------------------------------------------


import time
import adafruit_dht
import board

dht_device = adafruit_dht.DHT11(board.D17)

while True:
    try:
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32

        humidity = dht_device.humidity

        print("Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(temperature_c, temperature_f, humidity))
    except RuntimeError as err:
        print(err.args[0])		

    time.sleep(2.0)



***************************************************************************************


DHT 22 Temperature & Humidity Sensor Py Code:
--------------------------------------------


import time
import adafruit_dht
import board

dht_device = adafruit_dht.DHT22(board.D17)

while True:
    try:
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32

        humidity = dht_device.humidity

        print("Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(temperature_c, temperature_f, humidity))
    except RuntimeError as err:
        print(err.args[0])		

    time.sleep(2.0)


***************************************************************************************

THINGSPEAK
#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

// Replace with your network credentials
const char* ssid = "m01";
const char* password = "12345678";

// Replace with your ThingSpeak API key
String apiKey = "INMKRPG1ND53G3P0";
const char* server = "http://api.thingspeak.com/update?";

// DHT settings
#define DHTPIN 4       // GPIO connected to DHT11 (e.g., GPIO4)
#define DHTTYPE DHT11  // DHT 11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();  // Celsius

  // Check if reading was successful
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    delay(2000);
    return;
  }

  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" °C, Humidity: ");
  Serial.print(h);
  Serial.println(" %");

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String url = String(server) + "api_key=" + apiKey + "&field1=" + String(t) + "&field2=" + String(h);
    http.begin(url);

    int httpResponseCode = http.GET();

    if (httpResponseCode > 0) {
      Serial.print("Data sent successfully. Response code: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("Error sending data. HTTP response code: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  } else {
    Serial.println("WiFi not connected.");
  }

  delay(15000);  // ThingSpeak accepts updates every 15 seconds
}



**************************************************************************************

LDR Sensor for Py Code:
----------------------


# Example Code: Interfacing LDR with Raspberry Pi
# Iotbyhvm.ooo - Explore TechBytes

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Pin Definitions
ldr_threshold = 1000
LDR_PIN = 18
LIGHT_PIN = 11

def readLDR(PIN):
    reading = 0
    GPIO.setup(LDR_PIN, GPIO.OUT)
    GPIO.output(LDR_PIN, False)
    time.sleep(0.1)
    GPIO.setup(LDR_PIN, GPIO.IN)

    # Count until pin reads HIGH
    while not GPIO.input(LDR_PIN):
        reading += 1

    return reading

def switchOnLight(PIN):
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)

def switchOffLight(PIN):
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, False)

# Main Loop
try:
    while True:
        ldr_reading = readLDR(LDR_PIN)
        print(f"LDR Reading: {ldr_reading}")

        if ldr_reading < ldr_threshold:
            switchOnLight(LIGHT_PIN)
        else:
            switchOffLight(LIGHT_PIN)

        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO pins on exit


*************************************************************************************


MQTT Pi & ESP2 :
---------------

MQTT Between Pi and ESP32


Raspberry Pi :


Run the following commands : 
* Open a terminal and run : 
ifconfig
* Note the ip address in wlan0 section (Eg 172.168.134.35)
* sudo apt install mosquitto mosquitto-clients
* sudo systemctl status mosquito
* sudo systemctl enable mosquitto.service
* sudo nano /etc/mosquitto/mosquitto.conf
(Open the File and add the below content to the last line)
listener 1883
allow_anonymous true

* Install paho package by the command : sudo apt install python3-paho-mqtt
* The code to be run in Raspberry Pi is given below:

Python Code in Pi:
-----------------


import paho.mqtt.client as mqtt

broker_address="192.168.173.114" // ip of the mobile device we noted from ifconfig command
client=mqtt.Client("PiClient")
client.connect(broker_address)

def on_message(client,userdata,message):
    print("Message received"+message.payload.decode("utf-8"))
    client.publish("ESP32/Acknowledgement","Message received from from ESP32, sent from Pi")

client.on_message=on_message
client.subscribe("ESP32/Temperaturedataread")
client.loop_start()
while True:
    pass



Run the code using the run button in thonny, no need cli commands.

In ESP32 :
----------

1. Copy and paste the ESP32 Code into the IDE 
2. Change the wifi SSID and Password with the name of your wifi and password(hotspot)
3. Replace the ip address in the code with the ip address noted before
4. Ensure that PubSubClient.h package is installed else install it in arduino IDE
5. Upload the code into ESP32


Once the ESP32 is connected to the network and successfully connected to the MQTT Client 
In Raspberry pi , Run the following commands in a terminal : 

#no need to use this cli command, we have written a py script to subscribe and publish
To visualize the data arrived at RPI Broker, execute the below command
mosquitto_sub -d -t ESP32/Temperaturedataread


In the terminal you can see a message being transmitted and acknowledgement being received.


Modified ESP 32 Code : 
#include <WiFi.h>
#include <PubSubClient.h>

#define Ledpin 13
#define IRpin 14

// WIFI credentials
const char* ssid = "ssid";
const char* password = "password";

// MQTT Broker IP address
const char* mqtt_server = "192.168.173.114";

char tempString[20];  // Buffer to hold the message
WiFiClient espClient;
PubSubClient client(espClient);

// Callback function when a message is received
void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.println(topic);
  
  // Create a temporary string to hold the message
  String messageTemp;
  for (int i = 0; i < length; i++) {
    messageTemp += (char)message[i];
  }

  Serial.print("Message: ");
  Serial.println(messageTemp);

  // Check if the received topic is the acknowledgment topic
  if (String(topic) == "ESP32/Acknowledgement") {
    Serial.println("Acknowledgment received from Raspberry Pi!");
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(Ledpin, OUTPUT);
  pinMode(IRpin, INPUT);

  // Connect to WiFi
  Serial.println("Connecting to WiFi");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Connected to WiFi with IP: ");
  Serial.println(WiFi.localIP());

  // Setup MQTT client and set callback
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  // Connect to the MQTT broker
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
    if (client.connect("espClient")) {
      Serial.println("Connected to MQTT broker");
      client.subscribe("ESP32/Acknowledgement");  // Subscribe to acknowledgment topic
    } else {
      Serial.print("Failed to connect, state: ");
      Serial.println(client.state());
      delay(2000);
    }
  }
}

void loop() {
  // Ensure the MQTT client stays connected and processes incoming messages
  client.loop();

  bool IRstatus = digitalRead(IRpin);
  if (IRstatus == true) {
    digitalWrite(Ledpin, LOW);  // Turn off the LED
    strcpy(tempString, "LED OFF");
  } else {
    digitalWrite(Ledpin, HIGH);  // Turn on the LED
    strcpy(tempString, "LED ON");
  }

  // Publish the status to the MQTT topic
  client.publish("ESP32/Temperaturedataread", tempString);


  delay(2000);
}


*************************************************************************************

Web Browser for ESP32 Code:
---------------------------

#include <WiFi.h>
#include <HTTPClient.h>
const char* ssid = "wifi_name";
const char* password = "pswd";
void setup() {
Serial.begin(115200);
WiFi.begin(ssid, password);
Serial.println("Connecting");
while(WiFi.status() != WL_CONNECTED) {
delay(500);
Serial.print(".");
}
Serial.println("");
Serial.print("Connected to WiFi network with IP Address: ");
Serial.println(WiFi.localIP());
Serial.println("Timer set to 5 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");
}
void loop() {
if(WiFi.status()== WL_CONNECTED){
HTTPClient http;
http.begin("http://192.168.243.153:8000/get-sensor?temperature=243");
int httpCode = http.GET();
if (httpCode > 0) { 
String payload = http.getString();
Serial.println(httpCode);
Serial.println(payload);
}
else {
Serial.println("Error on HTTP request");
}
http.end();
}else{
}
delay(10000);
}




Pi code for Web Browser:  (app.py)
-----------------------


from flask import Flask, request


app = Flask(__name__)
l = []


@app.route('/')
def index():
    return 'OK', 200


@app.route('/get-sensor', methods=['GET'])
def data():
    if request.method == 'GET':
        args = request.args
        temperature = args.get('temperature')
        l.append(temperature)
        return temperature
    else:
        return 'Wrong'


@app.route('/get')
def data1():
    sensor_data = '<ul>'
    for item in l:
        sensor_data += f'<li>{item}</li>'
    sensor_data += '</ul>'
    return sensor_data


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')


*********************************************************************************

i 2 c for Py Code:
-----------------


# Raspberry Pi Master for Arduino Slave
from smbus import SMBus
addr = 0x8 # bus address
bus = SMBus(1)
numb = 1
print ("Enter 1 for ON or 0 for OFF")
while numb == 1:
ledstate = input(">>>> ")
if ledstate == "1":
bus.write_byte(addr, 0x1) # switch it on
elif ledstate == "0":
bus.write_byte(addr, 0x0) # switch it off
else:
numb = 0


i 2 c for Arduino Uno Code:
--------------------------


// Include the Wire library for I2C
#include <Wire.h>
  const int ledPin = 13;
  void setup() 
  {
    Wire.begin(0x8);
    Wire.onReceive(receiveEvent);
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);
  }
// Function that executes whenever data is received from master
    void receiveEvent(int n) 
  {
    while (Wire.available()) 
    { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    digitalWrite(ledPin, c);
  }
}
  void loop() 
  {
    
    delay(100);
}


-------------------------------
SEMAPHORE 
------------------------------
#include<stdio.h>
#include<freertos/FreeRTOS.h>
#include<freertos/task.h>
#include "freertos/semphr.h"

SemaphoreHandle_t mySemaphore;

void setup(){
	Serial.println("setup");
	Serial.begin(9600);
	if(mySemaphore==NULL){
		mySemaphore=xSemaphoreCreateBinary();
		if(mySemaphore!=NULL){
			xSemaphoreGive( (mySemaphore) );
		}
	}
	xTaskCreate(TaskLed, "Led", 10000, NULL, 1 ,NULL);
	xTaskCreate(TaskBlink, "BLINK", 10000, NULL, 1, NULL);
	digitalWrite(7,LOW);
	digitalWrite(8,LOW);
}
void loop(){}
void TaskLed(void *params){
	(void) params;
	pinMode(8,OUTPUT);
	for(;;){
		if(xSemaphoreTake(mySemaphore, (TickType_t)10)!=pdTRUE){
			Serial.println("waiting inside taskled for semaphore");
			digitalWrite(8,LOW);
		}
		else{
			Serial.println("semaphore in taskled");
			digitalWrite(8,HIGH);
			delay(5000);
			xSemaphoreGive(mySemaphore);
			delay(1000);
		}
	}
}

void TaskBlink(void *params){
	(void) params;
	pinMode(7,OUTPUT);
	for(;;){
		if(xSemaphoreTake(mySemaphore, (TickType_t)10)!=pdTRUE){
			Serial.println("Waiting inside blink for semaphore");
			digitalWrite(7,LOW);
		}
		else{
			digitalWrite(7,HIGH);
			delay(5000);
			xSemaphoreGive(mySemaphore);
			delay(1000);
		}
	}
	
}


-------------------------------------
TaskHandle
-------------------------------------
#include<Arduino.h>
#include<freertos/FreeRTOS.h>
#include<freertos/task.h>
TaskHandle_t xHandle1,xHandle2;

#define rled 4
#define gled 5

void setup(){
	pinMode(rled, OUTPUT);
	pinMode(gled, OUTPUT);
	Serial.begin(9600);
	xTaskCreate(taskOne, "TaskOne",10000,NULL,1,&xHandle1);
	Serial.println("\nsetup done....");
}

void loop(){
	delay(1000);
}

void taskOne(void *parameter){
	int i=0;
	Serial.println("\nHello from task1");
	while(i<4){
		if(i==2){
			xTaskCreate(taskTwo, "TaskTwo",10000, NULL, 2, &xHandle2);
		}
		digitalWrite(rled, HIGH);
		digitalWrite(gled, LOW);
		Serial.println(i);
		vTaskDelay(pdMS_TO_TICKS(5000));
		i++;
	}
	Serial.println("Ending Task 1");
	vTaskDelete(NULL);
}
 
void taskTwo(void *parameter){
	int i=0;
	Serial.println("\nHello from task2");
	while(i<4){
		Serial.print("Task2");
		digitalWrite(rled, LOW):
		digitalWrite(gled, HIGH);
		Serial.println(i);
		vTaskDelay(pdMS_TO_TICKS(1000));
		i++;
	}
	Serial.println("Ending task 2");
	vTaskDelete(NULL);
}
'''
st.code(codee)
