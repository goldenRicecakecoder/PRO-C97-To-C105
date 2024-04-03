import cv2


img = cv2.imread("solar-system.jpg")


font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
font_color = (255, 255, 255)


cv2.putText(img, "Mercury", (50, 450), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Venus", (150, 450), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Earth", (250, 450), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Mars", (350, 450), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Jupiter", (450, 450), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Saturn", (550, 450), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Uranus", (650, 450), font, font_scale, font_color, font_thickness)
cv2.putText(img, "Neptune", (750, 450), font, font_scale, font_color, font_thickness)

cv2.imshow("output", img)
cv2.waitKey(0)


cv2.imwrite("Solar_systemwithname.jpg", img)