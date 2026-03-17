import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model

st.title("Sign Language Detection")

model = load_model("sign_model.keras")
st.write(model.input_shape)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

frame_placeholder = st.empty()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    ret, frame = cap.read()

    if not ret:
        break

    img = cv2.resize(frame, (64, 64))
    img = img / 255.0
    img = img.reshape(1, 64, 64, 3)

    prediction = model.predict(img)
    letter = alphabet[np.argmax(prediction)]

    frame_placeholder.image(frame, channels="BGR")

    st.write("Predicted Letter:", letter)

cap.release()