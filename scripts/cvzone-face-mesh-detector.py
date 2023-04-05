import cv2
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=2)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    image, faces = detector.findFaceMesh(frame)

    cv2.imshow("Face Mesh Detector", image)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
