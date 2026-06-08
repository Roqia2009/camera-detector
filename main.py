import cv2
import requests
import numpy as np
from ultralytics import YOLO
import time

TELEGRAM_TOKEN = "8949424119:AAEIuo1bYrMUE7ohqdrdharpU-3MhDPk59Y"
CHAT_ID = "8556427970"

# متغيرات للتحكم في وقت إرسال الرسائل (مثلاً يبعت رسالة كل 10 ثواني كحد أقصى لو العربية لسه واقفة)
last_alert_time = 0
alert_cooldown = 10  # بالثواني

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Aleart was sent to telegram")
        else:
            print(f"problem with your bot: {response.text}")
    except Exception as e:
        print(f"Error sending to Telegram: {e}")

model = YOLO("yolo11n.pt")

video_path = "video.mp4"
cap = cv2.VideoCapture(video_path)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('parking_result.mp4', fourcc, fps, (frame_width, frame_height))

parking_zone = [(100, 200), (400, 200), (500, 500), (50, 500)]
pts = np.array(parking_zone, np.int32)
pts = pts.reshape((-1, 1, 2))

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model.predict(source=frame, classes=[2, 7], verbose=False)

    car_inside_zone = False

    cv2.polylines(frame, [pts], isClosed=True, color=(255, 0, 0), thickness=2)

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        
        center_x = int((x1 + x2) / 2)
        center_y = int(y2)

        is_inside = cv2.pointPolygonTest(pts, (center_x, center_y), False)

        if is_inside >= 0:
            car_inside_zone = True
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
        else:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    if car_inside_zone:
        current_time = time.time()
        print("ALERT: Vehicle detected in the prohibited parking zone!")
        cv2.putText(frame, "ALERT: ZONE OCCUPIED!", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        
        if current_time - last_alert_time > alert_cooldown:
            msg = "ALERT: Vehicle detected in the prohibited parking zone!"
            send_telegram_message(msg)
            last_alert_time = current_time

    out.write(frame)

cap.release()
out.release()