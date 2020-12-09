# EE542-a-smart-garage-system
## Purpose:
This file is a source code for a smart garage charging system written in Python. It is triggered by a motion sensor to capture car image by Raspberry Pi Model B+. Then, by going through a pre-trained machine learning model, it can analyzes the plate number in the image and send plate number to Node-Red, which will redirect the number to AWS IoT Analytics later. In the AWS EC2, a virtual machine will keep getting updated from the AWS IoT Analytics to monitor the entering and exiting of the car in the garage. Once the car exits garage, it will send a SMS of receipts, including vehicle plate number, parking time and parking fees, to the users.

## Required Materials:
1. Raspberry Pi Model B+ Board
2. Raspberry Pi Camera Module V2 8MP 1080P
3. HC-SR501 Pir Motion IR Sensor Body Module Infrared for Arduino Raspberry Pi
4. Three Female-to-Female Wires

## Hardware Setup:
1. Montion Sensor:
Raspberry Pi Pin Layer: https://www.electronicwings.com/raspberry-pi/raspberry-pi-gpio-access
Raspberry Pi Pir Sensor Pin Layer: https://raspberry-valley.azurewebsites.net/Connecting-the-PIR-Sensor/
Based on the two assignment documents above, connect Pir sensor with Raspberry Pi. In our code, connect Vcc in Pir with pin2 in Pi. Connect Gnd with pin6 in Pi. Connect Signal with pin7(GPIO4) in Pi.
2. Camera:
Insert camera to the camera port in Raspberry Pi
3. Raspberry Pi:
Download OS from Raspberry official website and install it in Pi.
Download VNCViewer to desktop.
Connect Pi with desktop by Enternet wire.
Open VNCViwer. Enter local: raspberrypi.local. Enter user name: pi. Enter password: raspberry


## Module 1(Raspberry-Pi):
### motionsensor.py:
#### function:
It is the main file for source code. By running this file, it can detect if there is a car go through the motion sensor. It will also call subsequent functions.

### image.py:
#### prerequisites: 
Enable Raspberry Pi Camera before running.
#### function:
It is called by motionsensor.py and it can capture image by camera and save the image with 1920 and 1080 resolutions as "picuture.jpg" in the current folder.

### openalpr_ocr.py:
#### prerequisites: 
Install requests, based64 and json library.
#### function:
It is called by motionsensor.py and it can send the image to openalpr and find the plate number in image. Openalpr is a website which can analyze the plate number in the image by using machile learning with a high accuracy. 
#### variables:
status: it can be either "Exiting" or "Entering" dependent on whehter this camera is set in exit or entrance of the
garage.
secret_key: secret_key in your openalpr account in the CarCheckAPI section.

### upload.py:
#### prerequisites:
Install requests and time library.
#### function:
It is called by openalpr_ocr.py and it can upload the plate number to Node-Red.
#### variables:
url: link of Node-Red for uploading data

## Module 2(Node-Red):
### node-red flow.txt:
#### prerequisites:
Create a AWS IoT thing and get its url link.
Download corresponding certificate, private key, and CA certificate and upload them to the Node-red http request TLS configuration.
Make sure permission is allowed to upload data to Node-Red.
#### function:
This file can be imported to Node-Red to create the data flow from Raspberry Pi to Node-Red to AWS IoT thing.
#### variable:
url: link of AWS IoT thing for uploading data


## Module 3(AWS-Cloud):
### Parking.py:
#### prerequisites:
Create AWS IoT Analytics resources including channel, pipeline, datestore, and dataset.
Create an IoT rule to forward messages received by the IoT thing to IoT Analytics.
Open a notebook instance in AWS Sagemaker and configure its IAM role to get dataset content.
Add a new user to AWS IAM, set permission policy to allow AWS SNS service and download keyid and secret key.
Open AWS SNS and set message type to tranctional.
Install botos3 and pandas library.
#### function:
This file is compiled in an AWS SageMaker notebook instance. It can keep accessing the data in the AWS IoT Analytics dataset to see if there is new data added. If new data is detected and it has a status with "Exiting", program
will search the entering time of the vehicle and send a SMS to the user of the vehicle based on a predefined dictionary.
#### variable:
dataset: name of dataset in AWS IoT Analytics
dict: dictionary that stores the users' phone number and vehicle number. Key: vehicle plate number. Value: vehicle's contact number.
aws_access_key_id: keyid in IAM new user.
aws_secret_access_key: secret key in IAM new user.


## Conclusion:
In order to make sure that the entire source code can work. Make sure you compile all three modules mentioned above.


## Alternative for Plate Number Detection:
The plate number detection is used by a program from third-party. It is highly accurate but there will be a little amount of cost. A py file in Raspberry-Pi provides an alternative method with no cost. However, this method is not recommended because of low accuracy. If you want to use the method, compile realtime.py instead of motionsensor.py. Once the realtime.py is running, you can press the “s” key in the keyboard to crop an image and run the plate number detection. The subsequential program works the same as the old program.
### prerequisites:
Install pytesseract, imutils, cv2, PIL and smtplib library.
