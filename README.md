# 🧠 EmoSort-AI 😄 😡 😐 😢

EmoSort-AI is an end-to-end Deep Learning project that **automatically classifies and segregates facial images based on emotions**.  
Users can upload a **single folder containing mixed-emotion images**, and the system will **separate them into emotion-wise folders** such as `Happy`, `Sad`, `Angry`, and `Neutral`.

This project demonstrates a complete **ML pipeline** — from data preprocessing and CNN model training to prediction and automated file organization.

---

## 🚀 Features

- 📂 Upload a folder containing mixed emotion images
- 🧠 CNN-based facial emotion recognition
- 🗂️ Automatically sorts images into emotion-specific folders
- 🔁 End-to-end training + prediction pipeline
- 💻 Command-line based (Web App coming next)
- 📦 Clean and modular code structure

---

## 🧠 Emotions Supported

- 😄 Happy  
- 😡 Angry  
- 😐 Neutral  
- 😢 Sad  

(Extendable to more emotions)

---

## 📁 Project Structure

EmoSort-AI/
│
├── data/
│ ├── Angry/
│ ├── Happy/
│ ├── Neutral/
│ └── Sad/
│
├── notebooks/
│ └── experimentation.ipynb
│
├── src/
│ ├── preprocess.py # Image loading & preprocessing
│ ├── model.py # CNN model architecture
│ ├── train.py # Model training script
│ └── train_and_predict.py # Predict & auto-sort images
│
├── emosort_model.h5 # Trained CNN model
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/joyboy2001/EmoSort-AI.git
cd EmoSort-AI
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
🏋️ Training the Model (Optional)
If you want to retrain the model with your own dataset:

python src/train.py
This will:

Load images from data/

Train a CNN

Save the model as emosort_model.h5

🔮 Predict & Auto-Sort Images (MAIN FEATURE)
📂 Input
A folder containing mixed emotion images, for example:

mixed_images/
├── img1.jpg
├── img2.jpg
├── img3.jpg
▶️ Run Prediction & Sorting
python src/train_and_predict.py mixed_images/
📁 Output
Emotion-wise folders will be created automatically:

sorted_output/
├── Happy/
├── Sad/
├── Angry/
└── Neutral/
Each image is moved into the correct folder based on prediction.

🧪 Sample Output
Predicted Emotion : Happy
Confidence        : 0.87

Image moved to → sorted_output/Happy/
🛠 Tech Stack
Python

TensorFlow / Keras

OpenCV

NumPy

CNN (Convolutional Neural Networks)

📈 Future Enhancements
🌐 Convert into a Web App (Flask / FastAPI / Streamlit)

📤 Drag-and-drop folder upload

📊 Prediction confidence visualization

☁️ Cloud deployment

📱 Mobile-friendly UI

👨‍💻 Author
Sudeep J
Final Year CSE (AI & ML)
GitHub: https://github.com/joyboy2001

⭐ If you like this project
Give it a ⭐ on GitHub — it really helps!
