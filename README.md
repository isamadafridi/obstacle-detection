# YOLOv8 Obstacle Detection System

A real-time obstacle detection system built using **YOLOv8** and trained on a custom obstacle detection dataset.  
This project detects multiple real-world objects such as vehicles, pedestrians, road obstacles, traffic signs, poles, stairs, dustbins, and more.

The model is optimized for fast inference and deployed as an interactive web demo on Hugging Face Spaces.

---

## 🚀 Live Demo

👉 [Hugging Face Demo](https://huggingface.co/spaces/isamadafridi/obstacle_detection)

---

## 📂 Dataset

Dataset used for training:

👉 [Obstacle Detection Dataset (Kaggle)](https://www.kaggle.com/datasets/abtinzandi/obstacle-detection-dataset)

### Dataset Statistics
- 25 object classes
- Real-world outdoor obstacle images
- Annotated bounding boxes
- Suitable for autonomous navigation and assistive systems

### Classes
- Bike
- Building
- Car
- Person
- Stairs
- Traffic Sign
- Electrical Pole
- Road
- Motorcycle
- Dustbin
- Dog
- Manhole
- Tree
- Guard Rail
- Pedestrian Crosswalk
- Truck
- Bus
- Bench
- Traffic Cone
- Fire Hydrant
- Traffic Barrel
- Plant Pot
- Electrical Box
- Chair
- Bicycle Rack

---

# 🧠 Model Architecture

This project uses **YOLOv8** for object detection.

### Model Variant
- **YOLOv8n** (Nano version)

### Why YOLOv8n?
YOLOv8n was selected because it provides:
- Fast inference speed
- Low memory usage
- Lightweight deployment
- Real-time detection capability
- Suitable for browser and edge deployment

---

# ⚙️ Training Configuration

## Training Parameters

| Parameter | Value |
|---|---|
| Model | YOLOv8n |
| Image Size | 512 × 512 |
| Epochs | 50 |
| Batch Size | 8 |
| Optimizer | MuSGD |
| Framework | PyTorch |
| GPU | Tesla T4 |

---

# 🔥 Data Augmentation

The model was trained using built-in YOLOv8 augmentations:

- Mosaic augmentation
- Horizontal flipping
- HSV color augmentation
- Translation augmentation
- Scaling augmentation
- Blur augmentation
- CLAHE enhancement

These augmentations improve:
- Generalization
- Robustness
- Real-world detection performance

---

# 📈 Training Results

## Final Performance

| Metric | Score |
|---|---|
| mAP50 | 0.902 |
| mAP50-95 | 0.728 |
| Precision | 0.884 |
| Recall | 0.834 |

---

# ✨ Key Features

## Real-Time Detection
Fast obstacle detection with optimized YOLOv8 inference.

## Multi-Class Detection
Detects 25 different obstacle categories.

## Browser-Based Inference
Runs directly in the browser using:
- ONNX Runtime Web
- HTML5 Canvas
- JavaScript

## Lightweight Deployment
No backend server required for inference.

---

# 🌐 Deployment

The model was converted to ONNX format and deployed on:

👉 [Hugging Face Spaces](https://huggingface.co/spaces/isamadafridi/obstacle_detection)

### Deployment Stack
- HTML5
- CSS3
- Vanilla JavaScript
- ONNX Runtime Web

---

# 📦 Exporting YOLOv8 to ONNX

```python
from ultralytics import YOLO

model = YOLO("best.pt")

model.export(format="onnx")
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

# 📁 Project Structure

```bash
project/
│
├── best.onnx
├── index.html
├── app.js
├── styles.css
├── README.md
└── assets/
```

---

# 🚀 Future Improvements

- Video stream detection
- Webcam inference
- TensorRT optimization
- Mobile deployment
- Faster ONNX acceleration
- Depth estimation integration
- Assistive navigation system

---

# 👨‍💻 Developer

## Abdul Samad Afridi

📧 Email: isamadafridi@gmail.com

---

# 📜 License

This project is intended for educational and research purposes.
