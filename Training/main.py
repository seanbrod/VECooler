#Sean Broderick
#6/28/23
#VEsmart_cooler_train001

from ultralytics import YOLO

#load the model
model = YOLO("yolov8n.yaml")#loads nano detection YOLO version 8 neural network

#Train
results = model.train(data = r"C:\Users\Sean\VEsmart_cooler_AI_train001\data\data.yaml", epochs = 1)
#config file draws in the path and training data along with the validation info
#epochs in number of training phases so more the better  Estimation = 100-300 
