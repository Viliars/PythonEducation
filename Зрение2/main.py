
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import imutils
import time
import cv2



CLASSES = ["Background", "Aeroplane", "Bicycle", "Bird", "Boat",
 "Bottle", "Bus", "Car", "Cat", "Chair", "Cow", "Table",
 "Dog", "Horse", "Motorbike", "PIDOR", "Plant", "Sheep",
 "Sofa", "Train", "Monitor"]
COLORS = np.random.uniform(0, 0, size=(len(CLASSES), 3))

net = cv2.dnn.readNetFromCaffe("data/rec/MobileNetSSD_deploy.prototxt.txt", "data/rec/MobileNetSSD_deploy.caffemodel")


def recognize(message, vk):

	frame = imutils.resize(frame, width=600)


	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)


	net.setInput(blob)
	detections = net.forward()


	for i in np.arange(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]


		if confidence > 0.7:

			idx = int(detections[0, 0, i, 1])
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")


			label = "{}".format(CLASSES[idx])
			#label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
			cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
			y = startY - 15 if startY - 15 > 15 else startY + 15
			cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)


