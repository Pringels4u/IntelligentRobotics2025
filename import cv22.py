import cv2
import numpy as np

# VERVANG DIT door de naam van jouw bestand:
bestandsnaam = "test_foto.jpg" 

# Laad de afbeelding
frame = cv2.imread(bestandsnaam)

# Controleer of het laden is gelukt
if frame is None:
    print(f"Fout: Kan {bestandsnaam} niet vinden in de map.")
else:
    # --- Jouw detectie logica ---
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    
    # Laat het resultaat zien
    cv2.imshow("Grijswaarden", gray)
    cv2.imshow("Canny Edges", edges)
    
    print("Druk op een toets om af te sluiten...")
    cv2.waitKey(0) # Wacht oneindig tot je een toets indrukt
    cv2.destroyAllWindows()