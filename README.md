# openCV_Projects-python-
# 🧠 OpenCV Projects – Python

This repository contains beginner-to-intermediate level projects built using Python and OpenCV for real-time image processing and computer vision tasks.

## 📁 Projects Included

### 1. 👤 Face Detection using Haar Cascade

Detects human faces in images or video streams using the Haar Cascade Classifier provided by OpenCV.

#### 🔍 Features
- Uses `haarcascade_frontalface_default.xml`
- Detects multiple faces in real time
- Draws rectangles around detected faces
- Can work with images or webcam feed

#### 📸 Sample Output
Faces are detected and highlighted with bounding boxes.

---

### 2. 🚶 Moving Object Detection

Detects and highlights moving objects in a video feed using frame differencing and contour detection.

#### 🔍 Features
- Detects motion by comparing frame differences
- Uses grayscale + Gaussian blur + contour detection
- Tracks and highlights moving objects in real-time
- Suitable for basic surveillance use cases

#### 📸 Sample Output
Objects in motion are highlighted with bounding boxes.

---

## 🛠️ Tech Stack

- Python
- OpenCV (cv2)
- Haar Cascade XML Classifiers
- Imutils

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have Python and OpenCV installed:

```bash
pip install opencv-python
