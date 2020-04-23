# Raspberry Pi People Recognition

## Introduction

Here will be presented Raspberry Pi project where RPi camera recognize people and save people amount to the Postgre database.
Will be shown how project was realized and also explanations and advices for realization.

## Accessing the camera using OpenCV

To access the Raspberry Pi camera we use OpenCV library. 

Check camera.py

Firstly we need to install Python library for camera and OpenCV library. 
```
pip3 install picamera
pip3 install opencv-python
```
For Python 3
```
pip install picamera
pip install opencv-python
```
For Python 2

And try this sample code to get know if your camera is working.
```
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32

capture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

def main():
    for frame in camera.capture_continuous(capture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Window", image)
        key = cv2.waitKey(1) & 0xFF
        capture.truncate(0)
        if key == ord("q"):
            break
    cv2.destroyAllWindows()
    
      
if __name__ == '__main__':
  main()
```
If in program appears import error
```
ImportError: libjasper.so.1: cannot open shared object file: No such file or directory
```
Try this operations in console
```
pip3 install opencv-python
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4
sudo apt-get install python3-pyqt5
```

These errors appear in Python 3.7+ versions and if these methods did not help then try other method
Install the certain open cv version 4.1.0.25
```
sudo pip3 install opencv-contrib-python==4.1.0.25
```
## People recognition

## Postgree

To add our data in Postgree sql we need to create a table in database and some code which will communicate with database.

Database dump can be found in database_dump.sql

In code we need following:

Install Postgree library

```
pip3 install psycopg2
```

Check sample_insert.py to get know how to insert data in Postgree table

Postgree library import
```
import psycopg2
```

Connect to the database
```
connection = psycopg2.connect(user="",
                                  password="",
                                  host="",
                                  port="",
                                  database="")

cursor = connection.cursor()
```

Database query
```
postgres_insert_query = """ INSERT INTO public.people_record (amount, datetime) VALUES (%s,%s)"""
record_to_insert = (2, "21/04/2020 22:55")
```

Send data
```
cursor.execute(postgres_insert_query, record_to_insert)
connection.commit()
```
Destroy the connection

```
cursor.close()
connection.close()
```
