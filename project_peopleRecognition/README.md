# People recognition

## Introduction

We will take code from examples to build the project on Python which find people amount on RPi camera and sends data to the Postgree database

## Database config

**config.py** file parses **database.ini** as database credentials. This was done for code convenience. In **main.py** this config is implemented in **postgre_insert** function.
```
params = config()
connection = psycopg2.connect(**params)
```

## How code works

1. Program gets frame from camera
2. Frame color changes to gray
3. Find faces using gray frame and face_cascade
4. Draw rectangles on faces
5. Send data to Postgre
6. Prints data in output


<details><summary>**Camera**</summary>
  
![Screenshot](https://github.com/alshap/RPi_camera_peopleRec/blob/master/images/screen1.png)

</details>

<details><summary>**Database**</summary>
  
![Screenshot](https://github.com/alshap/RPi_camera_peopleRec/blob/master/images/screen2.png)

</details>
