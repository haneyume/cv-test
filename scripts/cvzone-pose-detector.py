import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)
detector = PoseDetector()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    image = detector.findPose(frame)
    # hands, image = detector.findPosition(frame, bboxWithHands=True)

    cv2.imshow("Pose Detector", image)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
