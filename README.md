# 🤖 Hand Gesture Recognition for Sign Language Communication

the project translates American Sign Language (ASL) gestures into text/speech and vice versa using Deep Learning and Computer Vision. This system improves communication for hearing-impaired individuals using a real-time bidirectional interface.

This project is part of our **Final Year Engineering Curriculum** and aims to bridge the communication gap between hearing-impaired and hearing individuals using **Deep Learning**, **Computer Vision**, and **Gesture Recognition**.

---

## 👥 Team Members

- **DHARMA DEVI K** – Final Year Student, B.Tech - Information Technology  
  Arulmigu Meenakshi Amman College of Engineering  
  GitHub: [@DHARMA DEVI K](https://github.com/DHARMADEVIKEERTHI)

- **PERUMAL K** – Final Year Student, B.Tech - Information Technology  
  Arulmigu Meenakshi Amman College of Engineering  
  GitHub: [@PERUMAL K](https://github.com/k-perumal)
  
---

## 📂 Dataset Access

Due to file size limits on GitHub, the dataset used for training and testing is hosted on Google Drive.

📥 **[Click here to download the dataset for Hand Sign](https://drive.google.com/drive/folders/1yBXH6Zrcep7F0jpB7UOyxJzoYoiOcU8m)**

📥 **[Click here to download the dataset for Voice Process](https://drive.google.com/drive/folders/1jl_iy0CRS4hsVlHD5J_RLnauXqvP7NwH)**

> ⚠️ Make sure to download and extract the dataset into the project directory before training or testing the model.

---

## 📌 Project Highlights

- 🔤 **ASL Gesture to Text/Speech**: Recognizes 28 hand gestures using a trained MobileNetV2 model and translates them into readable text and audio.
- 🗣️ **Voice to Sign Animation**: Converts spoken English words to corresponding sign language animations using cartoon-based characters.
- 🎥 **Real-Time Hand Tracking**: Uses MediaPipe for efficient hand landmark detection from webcam feed.
- 🛠️ **Command-Line Interface**: A simple menu-driven CLI for smooth interaction and testing.

---

## 🗂️ Folder Structure
├── asl_model_mobilenetv2.h5 # Trained model for ASL recognition

├── data_collect.py # Script to collect gesture images

├── train.py # Model training script

├── main.py # Main execution: ASL gesture to text/speech

├── voiceto sign.py # Voice input converted to animated sign output

├── requirements.txt # Python dependencies

├── Hand Gesture Recognition Report.pdf # Detailed project documentation

├── PPT.pptx # Presentation slide deck

└── README.md # Project description (this file)

## 1. Install Dependencies

pip install -r requirements.txt

## 2. Run the Application

### To collect your own gesture data
python data_collect.py

### To train your own model
python train.py

### To recognize gestures and convert to text/speech
python main.py

### To convert voice to sign animation
python "voiceto sign.py"

## 🧠 Technologies Used
Python

TensorFlow / Keras

OpenCV

MediaPipe

MobileNetV2

pyttsx3 (Text-to-Speech)

## 📊 Results
Accuracy: 90%+ on test dataset of 28 ASL signs.

Real-time classification with smooth webcam performance.

Lightweight model deployable on standard devices.

## ✨ Future Enhancements
Add more gesture classes for complete ASL vocabulary.

Include multi-hand and dynamic gesture recognition.

Mobile/web deployment with TensorFlow Lite or ONNX.

## 📜 License
This repository is for academic and educational purposes only. Please contact us for permission before using it in commercial projects.

## 🙌 Acknowledgment
This project was completed as part of the final semester coursework under the guidance of faculty at Arulmigu Meenakshi Amman College of Engineering.

---

Let me know your Google Drive link and team members if you'd like me to insert them directly into this file. Or if you want a `.md` file to upload, I can generate that too.
