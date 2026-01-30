# 🧠 EmoSort-AI 😄😡😐😢  
### Emotion-Based Image Segregation using Deep Learning

EmoSort-AI is an end-to-end **deep learning application** that automatically detects facial emotions from images and **segregates them into emotion-specific folders**.

Users can upload a **single folder containing mixed emotion images**, and EmoSort-AI analyzes each image using a trained CNN model and sorts them into individual folders such as **Angry, Happy, Neutral, and Sad**.

---

## 🚀 Project Overview

Manual sorting of facial emotion images is time-consuming and error-prone.  
EmoSort-AI solves this by providing an **automated, AI-driven pipeline** that:

- Analyzes facial expressions
- Predicts emotions using a CNN
- Automatically organizes images into emotion-wise directories

This project demonstrates **real-world application of computer vision and deep learning**, going beyond simple prediction to full automation.

---

## 🎯 Supported Emotions

- Angry 😠  
- Happy 😄  
- Neutral 😐  
- Sad 😢  

---

## 🧠 Model Architecture

The emotion classifier is built using a **Convolutional Neural Network (CNN)** with the following components:

- Convolutional layers with ReLU activation  
- MaxPooling layers  
- Flatten layer  
- Fully connected Dense layers  
- Softmax output layer  

**Input Size:** 48 × 48 facial images  
**Output:** Probability scores for each emotion class  

---

## 📂 Project Structure

```
EmoSort-AI/
│
├── data/                     # Training dataset (emotion-wise folders)
│   ├── Angry/
│   ├── Happy/
│   ├── Neutral/
│   └── Sad/
│
├── input_images/             # User uploads mixed emotion images here
│
├── sorted_images/            # AI-generated emotion-wise output folders
│
├── src/
│   ├── preprocess.py         # Image preprocessing & loading
│   ├── model.py              # CNN model definition
│   ├── train.py              # Model training pipeline
│   └── emosort_folder.py     # Folder-based emotion segregation logic
│
├── emosort_model.h5          # Trained CNN model
├── requirements.txt
├── .gitignore
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/joyboy2001/EmoSort-AI.git
cd EmoSort-AI

### 2️⃣ Install dependencies

pip install -r requirements.txt

> **Python version:** 3.10+ recommended

---

## 🏋️ Training the Model

Run the training pipeline:

```bash
python src/train.py
This will:

* Load images from `data/`
* Preprocess & normalize them
* Train the CNN
* Save the trained model as `emosort_model.h5`

---
📂 Emotion-Based Folder Segregation (Main Feature)

Step 1️⃣ Add Mixed Images

Place any number of facial images (with mixed emotions) into:
input_images/
Example:
input_images/
├── img1.jpg
├── img2.png
├── img3.jpeg

⸻

Step 2️⃣ Run EmoSort-AI
python src/emosort_folder.py

⸻

Step 3️⃣ Output

After execution, EmoSort-AI automatically creates:
sorted_images/
├── Angry/
├── Happy/
├── Neutral/
└── Sad/
Each image is:
	•	Analyzed by the CNN model
	•	Classified based on emotion
	•	Copied into the appropriate emotion folder

🖼 Sample Output
✔ img1.jpg → Happy (0.72)
✔ img2.png → Sad (0.65)
✔ img3.jpeg → Angry (0.81)

🎉 EmoSort-AI finished sorting images successfully!

📊 Key Results
	•	Fully automated emotion-based image segregation
	•	Clean, modular ML pipeline
	•	Practical use of CNNs in real-world automation
	•	Easily extendable to web and API-based applications

⸻

🛠 Tech Stack
	•	Python
	•	TensorFlow / Keras
	•	NumPy
	•	OpenCV / PIL
	•	Git & GitHub

⸻

🧩 Concepts Demonstrated
	•	Image preprocessing
	•	Convolutional Neural Networks (CNN)
	•	Model training & inference
	•	Batch prediction
	•	File system automation using AI
	•	End-to-end ML pipeline design

⸻

🔮 Future Enhancements
	•	Face detection before emotion classification
	•	Confidence threshold & “Uncertain” emotion category
	•	Web application using Flask / FastAPI / Streamlit
	•	REST API for emotion-based image sorting
	•	Improved accuracy with larger datasets

⸻

👨‍💻 Author

Sudeep J
Final Year CSE (AI & ML)
GitHub: https://github.com/joyboy2001

⸻

⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

