# sign_language_detection
# 🖐️ Sign Language Detection System

A real-time Sign Language Detection system that uses a deep learning model to recognize hand gestures and predict corresponding alphabet letters using a webcam.

## 🚀 Features

* 📷 Real-time webcam capture using OpenCV
* 🤖 Deep Learning model for gesture classification
* 🔤 Predicts English alphabet letters (A–Z)
* 🌐 Interactive UI built with Streamlit
* ⚡ Fast and lightweight implementation

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV**
* **TensorFlow / Keras**
* **NumPy**
* **Streamlit**

---

## 📂 Project Structure

```
├── app.py                # Main Streamlit application
├── sign_model.keras      # Trained deep learning model
├── part1.ipynb           # Model training notebook
└── README.md             # Project documentation
```

---

## ⚙️ How It Works

1. The webcam captures live video frames.
2. Each frame is resized to **64x64 pixels**.
3. The image is normalized and passed to the trained model.
4. The model predicts the hand gesture.
5. The predicted output is mapped to an alphabet (A–Z).
6. The result is displayed in real-time on the screen.

---

## 📥 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/sign-language-detection.git
cd sign-language-detection
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

*(If you don't have requirements.txt, install manually:)*

```bash
pip install streamlit opencv-python tensorflow numpy
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 Model Details

* Input Shape: `(64, 64, 3)`
* Model Type: Convolutional Neural Network (CNN)
* Output: 26 classes (A–Z alphabets)

---

## 📸 Output

* Live webcam feed displayed on screen
* Predicted alphabet shown in real-time

---

## 🔮 Future Improvements

* Add support for **words and sentences**
* Improve model accuracy with a larger dataset
* Add hand detection (MediaPipe) for better precision
* Deploy the app online (Streamlit Cloud / Hugging Face)
* Add voice output for detected letters

---

## 👩‍💻 Author

**Riya Dey**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
