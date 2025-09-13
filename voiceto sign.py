import os
import cv2
import time
import speech_recognition as sr
import subprocess
#  Speech Recognition Function
def speech_to_text(filename=None):
    recognizer = sr.Recognizer()

    try:
        if filename:
            with sr.AudioFile(filename) as source:
                audio = recognizer.record(source)
        else:
            with sr.Microphone() as source:
                print("🎤 Speak something...")
                audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        print(f"✅ Recognized Text: {text}")
        return text

    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError:
        print("❌ Could not request results from speech recognition service.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    return ""

#  Cartoon effect for a frame
def cartoonize_frame(frame):
    color = cv2.bilateralFilter(frame, 9, 75, 75)
    for _ in range(2):
        color = cv2.bilateralFilter(color, 9, 75, 75)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(gray, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

#  Play cartoonized video
def play_cartoon_video(path):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print(f"❌ Error opening video: {path}")
        return
    print(f"🎬 Playing: {os.path.basename(path)}")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cartoon_frame = cartoonize_frame(frame)
        cv2.imshow("Cartoon Sign Language", cartoon_frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

#  Text to Cartoon Sign Language Video
def text_to_cartoon_sign(text,video_dir=r'D:\Final year project\project\speechto sign\project\isl'):
    print(f"📝 Processing Text: {text}")
    custom_phrases = {
        "what is your name": "What is your Name",
        "good afternoon": "Good afternoon",
        "good morning": "Good morning",
        "thank": "Thank you",
        "take care":"take care"
    }

    text = text.lower()
    for phrase, filename in custom_phrases.items():
        if phrase in text:
            path = os.path.join(video_dir, f"{filename}.mp4")
            if os.path.exists(path):
                play_cartoon_video(path)
            else:
                print(f"[⚠️] Currently training on: {filename}")
            text = text.replace(phrase, "")

    for word in text.split():
        filename = f"{word.capitalize()}.mp4"
        path = os.path.join(video_dir, filename)
        if os.path.exists(path):
            play_cartoon_video(path)
        else:
            print(f"[⚠️] Currently training on : {word}")

        time.sleep(0.5)

#  Menu Loop
def main_menu():
    while True:
        print("\n==============================")
        print(" Sign Language Recognition System")
        print("==============================")
        print("1. Sign Language to Voice")
        print("2. Voice to Sign Language")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("🔧 Sign Language to Voice.")
            os.system("python main.py")
            subprocess.run(["python", "main.py"])
        elif choice == '2':
            text = speech_to_text()
            if not text:
                text = input("📝 Or type the sentence manually: ")
            if text:
                text_to_cartoon_sign(text)
        elif choice == '3':
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice. Please try again.")
            

#  Entry Point
if __name__ == "__main__":
    main_menu()
