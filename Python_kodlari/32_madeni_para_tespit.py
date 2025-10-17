import cv2
import numpy as np

cap = cv2.VideoCapture(1)  
referans_yaricap=None
while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera verisi alinamadi.")
        break

    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(gri, (5, 5), 0)
    
    edges = cv2.Canny(blur, 50, 150)

    circles = cv2.HoughCircles(
        edges,
        cv2.HOUGH_GRADIENT,
        dp=1.2,           # Çözünürlük oranı
        minDist=40,       # İki daire merkezi arasındaki minimum mesafe
        param1=50,        # Canny üst eşiği
        param2=40,        # Daire tespit hassasiyeti
        minRadius=30,     # En küçük yarıçap
        maxRadius=120     # En büyük yarıçap
    )

    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for (x, y, r) in circles[0, :]:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 2)   
            cv2.circle(frame, (x, y), 2, (0, 0, 255), 3) 
            if referans_yaricap is None:
                referans_yaricap = r
                print(f"Referans alindi: {referans_yaricap} piksel")
            else:
                oran = r / referans_yaricap
                if abs(oran - 1.00) < 0.05:
                    cv2.putText(frame, "1 TL", (x-10, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                elif abs(oran - 0.90) < 0.05:
                    cv2.putText(frame, "50 krs", (x-10, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                elif abs(oran - 0.80) < 0.05:
                    cv2.putText(frame, "25 krs", (x-10, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                elif abs(oran - 0.72) < 0.05:
                    cv2.putText(frame, "10 krs", (x-10, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)   

    cv2.imshow("Para Tespiti", frame)

    if cv2.waitKey(20) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()
