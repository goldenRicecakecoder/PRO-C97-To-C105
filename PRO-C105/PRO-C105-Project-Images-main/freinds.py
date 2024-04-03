import os
import cv2

path = "C:/Users/danie/Downloads/PRO-C105-Project-Images-main/PRO-C105-Project-Images-main/Images"
Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    
    if ext.lower() in ['.jpg', '.jpeg', '.png']:
        file_name = f"{path}/{file}"
        Images.append(file_name)

count = len(Images)
frame = cv2.imread(Images[0])
width, height, channels = frame.shape
size = (width, height)
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(count):
    img = cv2.imread(Images[i])
    out.write(img)

print("Done")

out.release()
