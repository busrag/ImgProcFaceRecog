import cv2
import random
import numpy as np

#img = cv2.imread("kids2.jpg")

#image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def add_noise (img) :
    row, col = img.shape

    number_of_pixels = random.randint(5000, 10000)
    for i in range (number_of_pixels) :
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord] [x_coord] = 255

    number_of_pixels = random.randint(5000, 10000)
    for i in range (number_of_pixels) :
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord] [x_coord] = 0


    return img

img = cv2.imread('kids2.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('orijinal goruntu', img)
image = add_noise(img)
cv2.imshow('gurultulu goruntu', image )
cv2.waitKey(0)

median_filtre = cv2.medianBlur(image,5)
cv2.imshow('Medyan filtre sonucu Blurred', median_filtre)
cv2.waitKey()


face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
yuzler = face_cascade.detectMultiScale(median_filtre, 2.3)
print("goruntude tespit edilen yuz sayisi= " f"{len(yuzler)}")

for x, y, width, height, in yuzler:
    cv2.rectangle(median_filtre, (x,y), (x + width , y + height), color=(0,0,255), thickness=2)
    cv2.imshow("sonuc", median_filtre)

cv2.waitKey()

