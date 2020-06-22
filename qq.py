import cv2

img = cv2.imread(r"image\QQ1.png", 0)
cv2.imshow("01", img)
# imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("02", imggray)
imgblur = cv2.medianBlur(img, 5)
cv2.imshow("03", imgblur)
cv2.waitKey(0)