import time

import cv2

from reachy_mini import ReachyMini

_FACE_CASCADE = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def find_largest_face(frame):
    """Return the (x, y) pixel center of the largest detected face, or None."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = _FACE_CASCADE.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60)
    )
    if len(faces) == 0:
        return None
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    return (x + w // 2, y + h // 2)


with ReachyMini() as mini:
    print("Connected to Reachy Mini! Tracking faces via camera (Ctrl+C to stop)...")
    try:
        while True:
            frame = mini.media.get_frame()
            if frame is None:
                time.sleep(0.05)
                continue

            face = find_largest_face(frame)
            if face is not None:
                x, y = face
                print(f"Face at pixel ({x}, {y})")
                mini.look_at_image(x, y, duration=0.3)
            else:
                print("No face detected")

            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
