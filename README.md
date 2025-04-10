# 🖱️ Virtual Mouse Using Hand Gestures

A real-time **Virtual Mouse** built using **Python**, **OpenCV**, and **MediaPipe**, allowing users to control the mouse pointer with hand gestures detected through a webcam. The project utilizes computer vision techniques to move the cursor and perform click actions without any physical mouse.

---

## 🎯 Features

- 🖐️ Detects hand and finger landmarks using **MediaPipe**
- 📷 Uses webcam input for real-time gesture tracking
- 🖱️ Controls mouse pointer movement with index finger
- 👆 Performs mouse clicks using thumb-index gesture

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV** – For image processing and webcam capture
- **MediaPipe** – For hand detection and tracking
- **PyAutoGUI** – For controlling mouse actions

---

## 🚀 How It Works

1. Captures video from the webcam.
2. Detects hand landmarks using MediaPipe.
3. Maps the position of the **index finger** to move the mouse cursor.
4. If **thumb and index finger tips come close**, it triggers a mouse **click**.

---

## 🧑‍💻 Code Snippet

```python
if abs(index_y - thumb_y) < 20:
    pyautogui.click()  # Left click
    pyautogui.sleep(1)
elif abs(index_y - thumb_y) < 100:
    pyautogui.moveTo(index_x, index_y)
```
---

## 🔧 Installation Steps

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/virtual-mouse-python.git
cd virtual-mouse-python
```

2. **Install the Dependencies**

```bash
pip install opencv-python mediapipe pyautogui
```

3. **Run the Script**

```bash
python virtual_mouse.py
```
---

## 📌 Requirements

1. Python 3.6+
2. Webcam
3. Installed packages: opencv-python, mediapipe, pyautogui

---

## ✨ Future Enhancements

1. Add support for drag and right-click gestures
2. Improve gesture smoothness using Kalman Filter
3. Build a GUI-based controller for calibration

---

## 📧 Contact

If you have any questions, suggestions, or feedback regarding this project, feel free to reach out:

**Joshita Gupta**  
📍 Faridabad, Haryana  
📧 Email: [joshita2016@gmail.com](mailto:joshita2016@gmail.com)  
🔗 LinkedIn: [https://www.linkedin.com/in/joshita-gupta](https://www.linkedin.com/in/joshita-gupta)  
💻 GitHub: [https://github.com/yourusername](https://github.com/joshita2407)

---

## 📜 License

This project is licensed under the **MIT License**.

You are free to:
- ✅ Use
- ✅ Modify
- ✅ Distribute
- ✅ Include in your projects (even commercially)

As long as you give appropriate credit to the original author.

---
