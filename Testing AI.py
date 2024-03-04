# import file thu vien
import cv2

# Lưu file thuat toán Haar Cascade Frontal Face để tham khao
alg = "haarcascade_frontalface_default.xml"

# passing the algorithm to OpenCV
haar_cascade = cv2.CascadeClassifier(alg)

# Dung camera de nhan dien khuon matc
cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    text = "Face not detected"

# Đầu vào từ thế giới thực có nhiều màu sắc nhưng trong định dạng BGR. BGR là viết tắt của blue, green và red (xanh, xanh lá và đỏ). Điều này sẽ khiến ứng dụng thị giác máy phải xử lý rất nhiều thứ. Do vậy, để giảm bớt khối lượng quy trình, chúng ta sử dụng định dạng màu xám.
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)

# Khi bạn phát hiện ra khuôn mặt, bạn sẽ nhận được 4 tọa độ. Khi nhận diện đc khuôn mặt thì sẽ vẽ hình vuông với màu rgb
    for (x, y, w, h) in face:
        text = "Face Detected"
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Hiện chữ treen ảnh
    print(text)
    image = cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

# Hiển thị cửa sổ với tiêu đề Face Detection và hình ảnh. Sử dụng phương thức waitkey() để hiển thị cửa sổ trong 10 mili giây và kiểm tra một lần nhấn phím. Nếu người dùng nhấn phím Esc (Giá trị ASCII 27), hãy thoát khỏi vòng lặp.
    cv2.imshow("Face Detection", image)
    key = cv2.waitKey(10)

    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()