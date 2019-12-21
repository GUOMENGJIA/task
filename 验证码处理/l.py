import cv2
import numpy as np
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片

import os


def cut_picture(imagepath, name):
    l = list()
    n = list()
    n.append(name)
    l.append(n)

    # 得到图像的灰度图像
    gray = cv2.imread(imagepath, 0)
    img = cv2.imread(imagepath)

    blur = cv2.medianBlur(gray, 3)# 对图像进行中值滤波
    ret, th = cv2.threshold(blur, 175, 255, cv2.THRESH_BINARY) #将图片二值化，thresh1为目标图像
    contours, hierarchy = cv2.findContours(th, 2, 2) #得到最小外接矩形

    for cnt in contours:
        t = list()
        x, y, w, h = cv2.boundingRect(cnt)
        if x != 0 and y != 0 and w * h >= 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (234, 53, 57, 255), 2)
            t.append(x)
            t.append(y)
            t.append(w)
            t.append(h)
            l.append(t)
    path="newpictures/"+name
    cv2.imwrite(path, img)
    return l

def showImages(path):
    files=os.listdir(path)
    for file in files:
        filepath=path+'/'+file
        p = mpimg.imread(filepath)
        plt.imshow(p)  # 显示图片
        plt.show()

if __name__=="__main__":
    path = "pictures"
    pictures = list()
    for file in os.listdir(path):
        filepath=path+'/'+file
        pictures.append(cut_picture(filepath, file))
    csv = open("result.csv",'w')
    np.savetxt("result.csv",pictures,delimiter="," ,fmt = "%s")
    csv.close()
    showImages("newpictures")




