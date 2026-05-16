# YOLOv8 Obstacle Detection System

A real-time obstacle detection system built using **YOLOv8** and trained on a custom obstacle detection dataset.  
This project detects multiple real-world objects such as vehicles, pedestrians, road obstacles, traffic signs, poles, stairs, dustbins, and more.

The system is deployed using **FastAPI** and provides an interactive browser-based interface for obstacle detection.

---

# 🚀 Live Demo

👉 [Hugging Face Demo](https://huggingface.co/spaces/isamadafridi/obstacle_detection)

---

# 📂 Dataset

Dataset used for training:

👉 [Obstacle Detection Dataset (Kaggle)](https://www.kaggle.com/datasets/abtinzandi/obstacle-detection-dataset)

### Dataset Statistics
- 25 object classes
- Real-world outdoor obstacle images
- Annotated bounding boxes
- YOLO format annotations
- Suitable for autonomous navigation systems

---

# 🧠 Model Architecture

This project uses **YOLOv8** for object detection.

### Model Variant
- **YOLOv8n** (Nano version)

### Why YOLOv8n?
YOLOv8n was selected because it provides:
- Fast inference speed
- Lightweight architecture
- Low memory usage
- Real-time detection capability
- Easy deployment

---

# ⚙️ Training Configuration

| Parameter | Value |
|---|---|
| Model | YOLOv8n |
| Epochs | 50 |
| Image Size | 512 × 512 |
| Batch Size | 8 |
| Optimizer | MuSGD |
| Framework | PyTorch |
| GPU | Tesla T4 |

---

# 🔥 Data Augmentation

The model was trained using YOLOv8 built-in augmentations:

- Mosaic augmentation
- Horizontal flip
- HSV color augmentation
- Translation augmentation
- Scaling augmentation
- Blur augmentation
- CLAHE enhancement

These augmentations improve model robustness and generalization.

---

# 📈 Model Performance

| Metric | Score |
|---|---|
| mAP50 | 0.902 |
| mAP50-95 | 0.728 |
| Precision | 0.884 |
| Recall | 0.834 |

---

# ✨ Features

- Real-time obstacle detection
- Multi-class object detection
- FastAPI backend
- Interactive frontend
- YOLOv8 inference
- Upload and analyze images
- Lightweight deployment

---

# 🌐 Tech Stack

## Backend
- FastAPI
- Python
- Ultralytics YOLOv8

## Frontend
- HTML5
- CSS3
- JavaScript

## Deep Learning
- PyTorch
- YOLOv8

---

# 📁 Project Structure

```bash
project/
│
├── best.pt
├── main.py
├── index.html
├── requirements.txt
├── static/
├── uploads/
└── README.md
```

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/isamadafridi/obstacle-detection
cd your-repository-name
```

---

# 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI Server

```bash
uvicorn main:app --reload
```

Server will start at:

```bash
http://127.0.0.1:8000
```

---

# 🧪 Sample Inference

```python
from ultralytics import YOLO

model = YOLO("best.pt")

results = model.predict(
    source="image.jpg",
    conf=0.25,
    save=True
)
```

---

# 🌍 Deployment

This project is deployed on Hugging Face Spaces.

👉 [Live Application](https://huggingface.co/spaces/isamadafridi/obstacle_detection)

---

# 🚀 Future Improvements

- Video stream detection
- Webcam integration
- TensorRT optimization
- Mobile deployment
- Edge AI optimization
- Real-time surveillance system

---

# 👨‍💻 Developer

## Abdul Samad

📧 Email: isamadafridi@gmail.com

---

# 📜 License

This project is intended for educational and research purposes.
