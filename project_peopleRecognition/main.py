import time
import cv2
import psycopg2
from config import config
import numpy as np
import datetime

cap = cv2.VideoCapture(0)


postgres_insert_query = """ INSERT INTO public.people_record (amount, datetime) VALUES (%s,%s)"""

face_cascade_path = '/home/pi/Desktop/project_peopleRecognition/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)

time.sleep(0.1)

def main():
    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for rect in faces:
            print(len(faces))
            (x, y, w, h) = rect
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            record_to_insert = [len(faces), datetime.datetime.now()]
            postgre_insert(postgres_insert_query, record_to_insert)
            time.sleep(2)


        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
    #   key Esc
        if key == 27: 
            break

    cap.release()
    cv2.destroyAllWindows()  
    
      
def postgre_insert(query, record):
    connection = False
    try:
        params = config()
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        cursor.execute(query, record)
        connection.commit()
        print("Data sent successfully")
        print("Found people: " + str(record[0]) + ". Time: " + str(record[1]))
    except (Exception, psycopg2.Error) as error:
        print ("Connection fails", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("Connection closed")

    
def nothing(x):
    pass


if __name__ == '__main__':
  main()