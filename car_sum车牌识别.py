import cv2
import numpy as np

print("======================read image===================================")
# img = cv2.imread(r"image\physics161.jpg")
# cv2.imshow("01", img)
# cv2.waitKey(0)


# print("======================read video===================================")
# cap = cv2.VideoCapture(r"video\zxy_醒着做梦.mp4")
# # cap = cv2.VideoCapture(0) # 摄像头0,1分别为前置和后置摄像头
# cap.set(3,600)
# cap.set(4,480)
# cap.set(10,100)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("zxy", img)
#     if cv2.waitKey(1) & 0xFF ==ord('s'):
#         break

print("======================basic function===================================")
# img = cv2.imread(r"image\physics162.jpg")
# kernel = np.ones((5, 5), np.uint8)
#
# imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgblur = cv2.GaussianBlur(imggray, (7, 7), 0)
# imgcanny = cv2.Canny(img, 150, 200)
# imgDialation = cv2.dilate(imgcanny, kernel, iterations=1)
# imgEroded = cv2.erode(imgcanny,kernel,iterations=1)
#
# cv2.imshow("gray image", imggray)
# cv2.imshow("BLUR image", imgblur)
# cv2.imshow("canny image", imgcanny)
# cv2.imshow("dialation image", imgDialation)
# cv2.imshow("eroded image", imgEroded)
# cv2.waitKey(0)

print("======================骚操作===================================")
# img = cv2.imread(r"image\physics161.jpg")
# imgHor = np.hstack((img, img))
# imgVer = np.vstack((img, img))
# cv2.imshow("Horizontal", imgHor)
# cv2.imshow("Vorizontal", imgVer)
# cv2.waitKey(0)


