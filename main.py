import cv2

image = cv2.imread("images1.jpg")
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh_img = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,51,9)

cnts = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

area_treshold = 1000
for cnt in cnts:
    if cv2.contourArea(cnt) > area_treshold:
        x,y,w,h = cv2.boundingRect(cnt)
        print(x,y,w,h)
        a=cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 3)
        #print("Count",cnt)
        #print('a',a)
        print("x",x)
        print("y", y)
        print("x+w", x+w)
        print("y+h", x+h)
        #cropped_image = image[y:y+h, x:x+w]
        cropped_image = image[40:, 200:]          #for image in right side of card
        #cropped_image = image[43:288, 203:269]
        #cropped_image = image[:150,:100]         #for image in left side of card
        cv2.imwrite("Cropped Image.jpg", cropped_image)
cv2.imshow("Image",cropped_image)
cv2.imshow("image", image)
cv2.waitKey()