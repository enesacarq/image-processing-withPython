import cv2

cap = cv2.VideoCapture(r"resim_ve_videolar\yuruyus.mp4")

ret, first_frame = cap.read()
if not ret:
    print("Kamera acilamadi!")
    exit()

first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (21, 21), 0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    diff = cv2.absdiff(first_gray, gray)

    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue  
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Hareket Maskesi", thresh)
    cv2.imshow("Hareket Tespiti", frame)

    key = cv2.waitKey(30) & 0xFF
    if key == 27: 
        break

cap.release()
cv2.destroyAllWindows()
