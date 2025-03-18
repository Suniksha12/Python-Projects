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