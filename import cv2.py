import cv2
import numpy as np

url = "http://192.168.1.165:8000"
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Kan de stream niet openen.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Geen frame ontvangen.")
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)


    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)

    # Draw lines on original frame
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            # Draw green line, thickness 3
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    cv2.imshow("Line Highlight", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()