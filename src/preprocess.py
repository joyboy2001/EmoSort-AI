import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

IMG_SIZE = 48
CATEGORIES = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

def load_data(data_dir):
    X, y = [], []

    for label, category in enumerate(CATEGORIES):
        path = os.path.join(data_dir, category)
        for img in os.listdir(path):
            try:
                img_path = os.path.join(path, img)
                image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
                X.append(image)
                y.append(label)
            except Exception:
                pass

    X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1) / 255.0
    y = np.array(y)

    return train_test_split(X, y, test_size=0.2, random_state=42)
