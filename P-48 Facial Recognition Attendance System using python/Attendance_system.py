import face_recognition
import cv2
import numpy as np
import csv 
from datetime import datetime

video_capture = cv2.VideoCapture(0)

#Load known faces
suni_image = face_recognition.load_image_file("faces/suni.jpg")

#encoding making
suni_encoding = face_recognition.face_encodings(suni_image)[0]

rohan_iamge = face_recognition.load_image_file("faces/rohan.jpg")

#encoding image
rohan_encoding = face_recognition.face_encodings(rohan_iamge)[0]

known_face_encodings = [suni_encoding,rohan_encoding]
known_face_names = ["Suni","Rohan"]

#list of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

#Get the current date and time
now = datetime.now()
# current_date = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f= open(f"{current_date}.csv","w+" , newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25 , fy=0.25)
    