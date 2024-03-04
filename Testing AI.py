import cv2

# loading the haar case algorithm file into alg variable
alg = "haarcascade_frontalface_default.xml"

# passing the algorithm to OpenCV
haar_cascade = cv2.CascadeClassifier(alg)

# capturing the video feed from the camera
cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    text = "Face not detected"

# convert each frame from BGR to Grayscale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces using Haar Cascade
    face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)

# draw a rectangle around the face and update the text to Face Detected
    for (x, y, w, h) in face:
        text = "Face Detected"
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# display the text on the image
    print(text)
    image = cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

# display the output window and press escape key to exit
    cv2.imshow("Face Detection", image)
    key = cv2.waitKey(10)

    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()