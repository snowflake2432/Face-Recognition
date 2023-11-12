import cv2


face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


video = cv2.VideoCapture(0)
frame = video.read()
def detect(video):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for (x,y,w,h) in faces:
        cv2.rectangle(video, (x, y), (x + w, y + h), (134, 123, 232), 5)
        cv2.putText(video, 'Face', (x, y), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
    return faces
while True:
    tf,frame = video.read()
    faces = detect(frame)
    cv2.imshow("Face Detection",frame)
    if cv2.waitKey(1) & 0xFF == ord('t'):
        break

video.release()
cv2.destroyAllWindows()