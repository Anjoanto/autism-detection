import mediapipe as mp
import numpy as np
import cv2
import time
import pandas as pd
import csv

capture_duration = 10
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0,(640,480))

start_time = time.time()

tracker = cv2.legacy.TrackerMOSSE_create()
tracker = cv2.TrackerCSRT_create()
success, img = cap.read()
bbox = cv2.selectROI("Image", img, False)
tracker.init(img, bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x,y), ((x+w),(y+h)), (255, 0, 255), 3)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


while( int(time.time() - start_time) < capture_duration):
    success, img = cap.read()

    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Lost", (75, 75), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    if success==True:
        out.write(img)
        cv2.imshow('image', img)
        cv2.waitKey(1)
    else:
        break
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)

                f = open("test.csv", "a", newline="")  # CONVERTION TO CSV STARTS HERRE TILL FCLOSE
                tup1 = (cx, cy)
                writer = csv.writer(f)
                writer.writerow(tup1)
                f.close()

            cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

cap.release()
out.release()
cv2.destroyAllWindows()

exec(open('convertcsv.py').read())