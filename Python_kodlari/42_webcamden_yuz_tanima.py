import cv2

cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier(r"haar_cascade_dosyalari\frontal_face.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame=cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Webcam Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break