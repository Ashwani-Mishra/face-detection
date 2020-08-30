import cv2
face_cascde = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    _,frame =cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascde.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.rectangle(frame,(x,y -40),(x+w,y),(51,51,255),-2)
        cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    cv2.imshow("Face Detection",frame)
    if cv2.waitKey(13)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()