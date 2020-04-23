from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import psycopg2
from config import config


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32

postgres_insert_query = """ INSERT INTO public.people_record (amount, datetime) VALUES (%s,%s)"""
record_to_insert = (2, "21/04/2020 22:55")

capture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)

def main():
    for frame in camera.capture_continuous(capture, format="bgr", use_video_port=True):
        cv2.namedWindow("Frame")
        cv2.createTrackbar("Neighbours", "Frame", 5, 20, nothing)

        image = frame.array
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        neighbours = cv2.getTrackbarPos("Neighbours", "Frame")
        faces = face_cascade.detectMultiScale(gray, 1.3, neighbours)
        for rect in faces:
            (x, y, w, h) = rect
            frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
        
        
        cv2.imshow("Frame", frame)
        cv2.imshow("Window", image)
        key = cv2.waitKey(1) & 0xFF
        capture.truncate(0)
        if key == ord("q"):
            break
    cv2.destroyAllWindows()
    
      
def postgre_insert():
    connection = False
    try:
        params = config()
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        print("Data sent successfully")

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