import cv2
import numpy as np

# 1. Vervang de URL door de naam van je videobestand
video_pad = "parkourredtape.mp4" 
cap = cv2.VideoCapture(video_pad)

if not cap.isOpened():
    print(f"Kan de video '{video_pad}' niet openen. Check de bestandsnaam!")
    exit()

while True:
    ret, frame = cap.read()
    
    # Als de video afgelopen is, stopt de loop
    if not ret:
        print("Einde van de video of kan frame niet lezen.")
        break

    # --- Jouw originele detectie logica (onveranderd) ---
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    # Toon het resultaat
    cv2.imshow("Line Highlight - Video Test", frame)
    cv2.imshow("Wat de robot ziet (Edges)", edges)

    # 'q' om te stoppen, of pas de '1' aan om de video te vertragen
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()