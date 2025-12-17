import cv2
import mediapipe as mp
import numpy as np
import time
import math

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

canvas = np.zeros((720, 1280, 3), dtype=np.uint8)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)]
color_names = ["Blue", "Green", "Red", "Eraser"]
current_color = None

brush_thickness = 6
eraser_thickness = 50

prev_x, prev_y = 0, 0
still_start_time = None
drawing_active = False
still_threshold = 15
required_still_time = 2

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    frame[:80, :] = (50, 50, 50)

    for i, color in enumerate(colors):
        cv2.rectangle(frame, (50 + i * 150, 20), (180 + i * 150, 70), color, -1)
        cv2.putText(frame, color_names[i], (60 + i * 150, 65),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.rectangle(frame, (700, 20), (850, 70), (0, 0, 0), -1)
    cv2.putText(frame, "CLEAR", (725, 65),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.rectangle(frame, (880, 20), (1030, 70), (0, 0, 255), -1)
    cv2.putText(frame, "EXIT", (920, 65),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark
            h, w, _ = frame.shape

            ix, iy = int(lm[8].x * w), int(lm[8].y * h)

            fingers_up = lm[8].y < lm[6].y and lm[12].y > lm[10].y

            if iy < 80:
                for i in range(len(colors)):
                    if 50 + i * 150 < ix < 180 + i * 150:
                        current_color = colors[i]
                        drawing_active = False
                        still_start_time = None

                if 700 < ix < 850:
                    canvas[:] = 0

                if 880 < ix < 1030:
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()

            if fingers_up and current_color is not None:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = ix, iy
                    still_start_time = time.time()
                else:
                    move_dist = distance((prev_x, prev_y), (ix, iy))
                    if move_dist < still_threshold:
                        if still_start_time is None:
                            still_start_time = time.time()
                        elif time.time() - still_start_time >= required_still_time:
                            drawing_active = True
                    else:
                        still_start_time = None
                        drawing_active = False

                if drawing_active:
                    thickness = eraser_thickness if current_color == (0, 0, 0) else brush_thickness
                    cv2.line(canvas, (prev_x, prev_y), (ix, iy), current_color, thickness)

                prev_x, prev_y = ix, iy
            else:
                prev_x, prev_y = 0, 0
                drawing_active = False
                still_start_time = None

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    frame = cv2.addWeighted(frame, 1, canvas, 1, 0)
    cv2.imshow("Gesture Virtual Whiteboard", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
