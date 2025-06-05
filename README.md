# 🕶️ AI Glasses Filter

This is a small computer vision project that uses facial detection to apply virtual glasses to a user's face in real time or from a photo.

It serves as an introductory portfolio piece in the field of:
- Computer Vision
- Virtual Augmentation (VA)
- Face Landmark Detection
- Interactive AI Interfaces

---

## ✨ Demo Features

- Upload or use webcam to provide a face image.
- Choose from **3 different glasses models**.
- Real-time detection of face and eye landmarks using MediaPipe.
- Virtual overlay of the selected glasses on your face.
- Clean Gradio-based interface.

---

## 🖼️ Interface Preview

| Webcam Input | Glasses Overlay | Selection |
|--------------|------------------|-----------|
| ![webcam](assets/demo_webcam.png) | ![glasses](assets/demo_glasses.png) | ![selector](assets/demo_selector.png) |

*(Note: Add screenshots to `assets/` folder to show examples)*

---

## 🚀 Run it locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-glasses-filter.git
cd ai-glasses-filter
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python main.py
```

Then open the link provided by Gradio in your browser.


---

## 🧠 Tech Stack

- Python
- OpenCV
- MediaPipe – for face/eye landmark detection
- Gradio – for fast and interactive web UI

---

## 📌 Notes

- This is a simple portfolio project, not optimized for production.
- Only the first detected face is processed.
- You can easily expand it to support live video streaming or more filters.

---

## 🧑‍💻 Author

**L. Suarez**  
[LinkedIn](https://www.linkedin.com/in/d-s-3973261b3) — [Portfolio](https://dsuarez.myportfolio.com/work) — [GitHub](https://github.com/L0L4-chan)

---

## 📜 License

MIT License – feel free to fork, improve, and share!
