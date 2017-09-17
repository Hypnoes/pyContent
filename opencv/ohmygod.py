import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
img = cap.read()
# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, color=(255,0,0))

# Print all default params
print(f"Threshold: {fast.getInt('threshold')}")
print(f"nonmaxSuppression: {fast.getBool('nonmaxSuppression')}")
print(f"neighborhood: {fast.getInt('type')}")
print(f"Total Keypoints with nonmaxSuppression: {len(kp)}")

cv2.imwrite('fast_true.png',img2)

# Disable nonmaxSuppression
fast.setBool('nonmaxSuppression',0)
kp = fast.detect(img,None)

print(f"Total Keypoints without nonmaxSuppression: {len(kp)}")

img3 = cv2.drawKeypoints(img, kp, color=(255,0,0))

cv2.imwrite('fast_false.png',img3)
