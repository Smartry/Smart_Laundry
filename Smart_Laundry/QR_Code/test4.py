import pyzbar.pyzbar as pyzbar
import cv2

cap = cv2.VideoCapture(0)

i = 0
while (cap.isOpened()):
    ret, img = cap.read()

    if not ret:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    decoded = pyzbar.decode(gray)

    for d in decoded:
        print(d.data)

    cv2.imshow('img', img)
    key = cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()