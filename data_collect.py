import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 28
dataset_size = 100

# Try using camera index 0, 1, or 2
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not access the webcam. Try changing the camera index.")
    exit()

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f"\n📸 Collecting data for class {j}")
    print("👉 Press 'Q' to start capturing images...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame. Is your camera free?")
            break

        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    print("✅ Starting capture...")

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame.")
            break

        resized_frame = cv2.resize(frame, (224, 224))  # ✅ Resize to 224x224
        cv2.imshow('frame', resized_frame)
        cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), resized_frame)

        counter += 1
        if cv2.waitKey(25) & 0xFF == ord('q'):
            print("⏹️ Capture interrupted.")
            break

    print(f"✅ Collected {counter} images for class {j}")

cap.release()
cv2.destroyAllWindows()
