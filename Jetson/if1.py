
from ultralytics import YOLO
#from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

model = YOLO('yolov8n.pt')  # load an official model
model = YOLO('C:/Users/Sean/VEsmart_cooler_AI_train001/best.pt')  # load a custom trained

results = model.predict(source='0', show = True, conf=0.5)
print(results)

#CMD LINE: yolo predict model=C:\Users\Sean\VEsmart_cooler_AI_train001/best.pt source='0'
