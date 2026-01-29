import os
import numpy as np
from preprocess import load_data
from model import build_model

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def main():
    print("Starting EmoSort AI training pipeline...")
    X, y = load_data(DATA_DIR)

    X = X.reshape(-1, 48, 48, 1) / 255.0

    model = build_model()
    model.summary()

    model.fit(X, y, epochs=5, batch_size=2)
    model.save("emosort_model.h5")

    print("Model training complete and saved.")

if __name__ == "__main__":
    main()
