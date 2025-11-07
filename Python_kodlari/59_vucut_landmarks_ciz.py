import cv2
import mediapipe as mp

mp_pose=mp.solutions.pose
mp_drawing=mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)

with mp_pose.Pose(static_image_mode=False,
                  model_complexity=2,
                  min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:
    
    while cap.isOpened():
        ret,frame=cap.read()
        
        if not ret:
            print("Kamera acilmadi")
            break
        
        frame=cv2.flip(frame,1)
        rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=pose.process(rgb_frame)
        
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)
        

        cv2.imshow("Vücut Landmarks",frame)
        if cv2.waitKey(1) & 0xFF==27:
            break

cap.release()
cv2.destroyAllWindows()
