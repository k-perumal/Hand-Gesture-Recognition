import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model
import pyttsx3
import time
import os

model = load_model('./asl_model_mobilenetv2.h5')

class_names=[
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'nothing','space'
             ]

engine = pyttsx3.init()
last_spoken = ""
identified=[]
last_prediction_time = 0

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.6)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
prediction_interval = 10
frame_count = 0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Get bounding box coordinates
            h, w, _ = frame.shape
            landmark_array = np.array([[lm.x * w, lm.y * h] for lm in hand_landmarks.landmark])
            x_min, y_min = np.min(landmark_array, axis=0).astype(int)
            x_max, y_max = np.max(landmark_array, axis=0).astype(int)

            padding = 30
            x_min = max(x_min - padding, 0)
            y_min = max(y_min - padding, 0)
            x_max = min(x_max + padding, w)
            y_max = min(y_max + padding, h)

            roi = frame[y_min:y_max, x_min:x_max]

            # Only predict every N frames
            if frame_count % prediction_interval == 0 and roi.size > 0:
                img = cv2.resize(roi, (224, 224))
                img = img.astype("float32") / 255.0
                img = np.expand_dims(img, axis=0)

                pred = model.predict(img, verbose=0)
                class_idx = np.argmax(pred)
                
                predicted_class = class_names[class_idx]

                # Speak only if new prediction and enough time has passed
                if predicted_class != last_spoken and time.time() - last_prediction_time > 1.5:
                    identified.append(predicted_class)
                    engine.say(f"The sign is {predicted_class}")
                    engine.runAndWait()
                    last_spoken = predicted_class
                    last_prediction_time = time.time()
                    print(identified)

           
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

    cv2.putText(frame, f"Prediction: {last_spoken}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("ASL with Mediapipe", frame)
    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
