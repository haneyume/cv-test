import cv2

ip_address = "192.168.0.100"
url = "http://" + ip_address + ":8080/video"

cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    cv2.imshow("Image", frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
