from cvzone.FaceDetectionModule import FaceDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    image, bbox = detector.findFaces(frame)

    cv2.imshow("Face Detector", image)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
