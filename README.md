

# 🖐️ Gesture-Based Virtual Whiteboard

## 📌 Overview

The Gesture-Based Virtual Whiteboard is a real-time computer vision application that allows users to draw and interact with a digital canvas using hand gestures captured through a webcam. The system enables touchless drawing by tracking finger movements and translating them into drawing actions, eliminating the need for physical input devices.

---

## 🚀 Features

* Real-time hand tracking using a webcam
* Gesture-based drawing on a virtual canvas
* Color selection using finger gestures
* Eraser functionality
* Clear screen option
* Smooth and responsive drawing
* Touch-free human–computer interaction

---

## 🛠️ Technologies Used

* Python 3.10
* OpenCV
* MediaPipe
* NumPy

---

## ⚙️ System Requirements

* Webcam (built-in or external)
* Windows OS
* Python 3.10.x

---

## 📦 Installation

```bash
git clone https://github.com/your-username/Gesture-Based-Virtual-Whiteboard.git
cd Gesture-Based-Virtual-Whiteboard
pip install opencv-python mediapipe numpy
pip install protobuf==3.20.3
```

---

## ▶️ How to Run

```bash
python VirtualDrawing.py
```

Press **q** to exit the application.

---

## 🧠 Working Principle

MediaPipe is used to detect hand landmarks in real time. Specific finger positions are mapped to actions such as drawing, color selection, erasing, and clearing the canvas. OpenCV handles video processing and rendering of the virtual whiteboard interface.

---

## 🎓 Academic Relevance

This project is suitable for MSc IT / Computer Science final-year projects and demonstrates practical applications of computer vision and gesture recognition.

---

## 🔮 Future Enhancements

* Multi-hand gesture support
* Undo and redo functionality
* Save drawings as images
* Performance optimization using lightweight models

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* MediaPipe by Google
* OpenCV community
