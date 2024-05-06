import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("/home/shree/Downloads/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-ml-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "6":
        {
            "name": "Nachiket Patil",
            "major": "IT",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "8":
        {
            "name": "Swaraj Patil",
            "major": "IT",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "5":
        {
            "name": "Wasim Naikawadi",
            "major": "IT",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "7":
        {
            "name": "Manas Paratane",
            "major": "IT",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:58:34"
        },
        "4":
        {
            "name": "Dr. Pravin Futane",
            "major": "HOD IT",
            "starting_year": 2010,
            "total_attendance": 100,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)