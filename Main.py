#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import os
import pickle
import time

import numpy as np
import cv2
import face_recognition
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime

# Import LED matrix libraries
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text

cred = credentials.Certificate("/home/shree/Downloads/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-ml-default-rtdb.firebaseio.com/",
    'storageBucket': "facerecognition-ml.appspot.com"
})

bucket = storage.bucket()

# Initialize LED matrix device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)

cap = cv2.VideoCapture(0)
address = "https://10.184.21.163:8080/video"
cap.open(address)
cap.set(3, 640)
cap.set(4, 480)

# Load the encoding file
print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encode File Loaded")

# Variable to store previously printed student ID
prev_student_id = None

# Function to display text on LED matrix
# Function to display single-digit number on LED matrix
def display_digit(digit):
    with canvas(device) as draw:
        text(draw, (0, 0), str(digit), fill="white")
        time.sleep(1)

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    if faceCurFrame:
        for encodeFace in encodeCurFrame:
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                student_id = str(studentIds[matchIndex])
                if student_id != prev_student_id:
                    print("Student ID:", student_id)
                    display_digit(student_id)
                    prev_student_id = student_id

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
