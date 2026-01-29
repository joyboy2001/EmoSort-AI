import os
import cv2
import numpy as np

IMG_SIZE = 48
LABELS = ["Angry", "Happy", "Neutral", "Sad"]

def load_data(data_dir):
    X, y = [], []

    for label in LABELS:
        path = os.path.join(data_dir, label)
        print(f"Loading {label} from {path}")

        if not os.path.exists(path):
            print(f"⚠️ Skipping missing folder: {path}")
            continue

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if image is None:
                continue
            image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
            X.append(image)
            y.append(LABELS.index(label))

    return np.array(X), np.array(y)
