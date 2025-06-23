# Pnumonia-Detection-from-XRays
Pnumonia Detection from XRays using CNN
# 🫁 Automatic Pneumonia Detection from Chest X-Rays

This project implements an automatic pneumonia detection system using deep learning techniques on chest X-ray images. It leverages convolutional neural networks (CNNs) to classify images as either **Normal** or **Pneumonia**, enabling early and accurate diagnosis.

## 📌 Project Overview

Pneumonia is a serious respiratory infection that requires prompt diagnosis and treatment. Radiologists typically use chest X-rays to detect it, but manual interpretation is time-consuming and prone to variability. This project aims to automate the detection process using machine learning to assist healthcare professionals and improve efficiency.

## 🔍 Dataset

The model is trained and evaluated using the **Chest X-Ray Images (Pneumonia) dataset** provided by [Kaggle](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia). It consists of:

- **Train Set**: 5,216 images (Normal / Pneumonia)
- **Validation Set**: 16 images
- **Test Set**: 624 images

Images are grayscale and categorized into:
- `NORMAL`
- `PNEUMONIA` (viral or bacterial)

## 🛠️ Features

- Image preprocessing and augmentation
- CNN-based classification
- Model evaluation: Accuracy, Confusion Matrix, Precision, Recall, F1-Score

## 🚀 Technologies Used

- Python
- TensorFlow / Keras
- NumPy, Pandas, Matplotlib, Seaborn
- Scikit-learn

## 📈 Model Performance

| Metric      | Value     |
|-------------|-----------|
| Accuracy    | 91.34%    |
| Precision   | 94.7%     |
| Recall      | 95.1%     |
| F1-Score    | 94.9%     |

*(Values vary based on architecture and hyperparameters)*

## 🧪 Data set

Download the dataset from [Kaggle](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) and place it in the `./data/` folder.


---

**Made with ❤️ for early diagnosis and improved healthcare.**

