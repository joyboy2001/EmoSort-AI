# EmoSort-AI 😄😡😐😢

An end-to-end **Emotion Classification System** using a **Convolutional Neural Network (CNN)** that detects human emotions from facial images. This project covers the complete ML lifecycle — **data preprocessing, model training, evaluation, and inference (prediction)**.

---

## 🚀 Project Overview

EmoSort-AI is designed to classify facial emotions into four categories:

* **Angry** 😠
* **Happy** 😄
* **Neutral** 😐
* **Sad** 😢

The system is implemented using **TensorFlow/Keras** and follows a clean, modular structure suitable for real-world ML projects and interviews.

---

## 🧠 Model Architecture

The CNN architecture includes:

* Convolution + ReLU layers
* MaxPooling layers
* Flatten layer
* Fully connected Dense layers
* Softmax output layer (4 classes)

**Input:** 48×48 grayscale facial images
**Output:** Emotion class probabilities

---

## 📂 Project Structure

```
EmoSort-AI/
│
├── data/
│   ├── Angry/
│   ├── Happy/
│   ├── Neutral/
│   └── Sad/
│
├── src/
│   ├── preprocess.py   # Data loading & preprocessing
│   ├── model.py        # CNN model definition
│   ├── train.py        # Training pipeline
│   └── predict.py      # Inference / prediction script
│
├── notebooks/
│   └── training.ipynb  # Experimentation notebook
│
├── emosort_model.h5    # Trained model
├── requirements.txt   # Dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/joyboy2001/EmoSort-AI.git
cd EmoSort-AI
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

> **Python version:** 3.10+ recommended

---

## 🏋️ Training the Model

Run the training pipeline:

```bash
python src/train.py
```

This will:

* Load images from `data/`
* Preprocess & normalize them
* Train the CNN
* Save the trained model as `emosort_model.h5`

---

## 🔮 Running Predictions (Inference)

Use the trained model to predict emotion from a new image:

```bash
python src/predict.py data/Happy/HAPPY.png
```

### ✅ Sample Output

```
Loading model...
Predicted emotion: Happy
```

---

## 📊 Results

* Successfully trained CNN model
* End-to-end pipeline from raw images → prediction
* Modular, reusable codebase

> Note: Accuracy can be improved further using data augmentation and larger datasets.

---

## 🧩 Key ML Concepts Demonstrated

* Image preprocessing
* CNN architecture design
* Model training & evaluation
* Saving/loading trained models
* Real-world inference pipeline

---

## 👨‍💻 Author

**Sudeep J**
Final Year CSE (AI & ML)
GitHub: [https://github.com/joyboy2001](https://github.com/joyboy2001)

---

## ⭐ Future Improvements

* Add webcam-based real-time emotion detection
* Increase dataset size
* Add data augmentation
* Deploy using FastAPI or Streamlit

---

⭐ If you like this project, give it a star on GitHub!
