import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("D:/downloads/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-ml-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "22110225":
        {
            "name": "Nachiket Patil",
            "major": "IT",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "22110995":
        {
            "name": "Swaraj Patil",
            "major": "IT",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "22110092":
        {
            "name": "Wasim Naikawadi",
            "major": "IT",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "22111290":
        {
            "name": "Manas Paratane",
            "major": "IT",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:58:34"
        },
        "22110000":
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