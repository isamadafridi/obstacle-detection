# main.py

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import numpy as np
import cv2
import uvicorn

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load YOLO model
model = YOLO("best.pt")


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Read image
    contents = await file.read()

    np_arr = np.frombuffer(contents, np.uint8)

    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Run prediction
    results = model.predict(image, conf=0.25)

    detections = []

    for box in results[0].boxes:

        cls_id = int(box.cls[0])

        confidence = float(box.conf[0])

        x1, y1, x2, y2 = box.xyxy[0].tolist()

        detections.append({
            "class": model.names[cls_id],
            "confidence": round(confidence, 2),
            "bbox": [x1, y1, x2, y2]
        })

    return JSONResponse({
        "detections": detections
    })


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)