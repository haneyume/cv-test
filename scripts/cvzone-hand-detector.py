import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    hands, image = detector.findHands(frame)

    cv2.imshow("Hand Detector", image)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
