import os
import cv2
import numpy as np
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import csv
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd

data=list()

def separator_character(imagepath,name):
    coordinate=list()
    a=list()
    a.append(name)
    img = cv2.imread(imagepath)
    gray = cv2.imread(imagepath, 0)#参数为0表示灰度图像，参数为1表示彩色图像


    blur = cv2.medianBlur(gray, 3)  # 对图像进行中值滤波
    ret, th = cv2.threshold(blur, 175, 255, cv2.THRESH_BINARY)  # 将图片二值化，thresh1为目标图像
    contours, hierarchy = cv2.findContours(th, 2, 2)  # 得到最小外接矩形
    coordinate.append(name)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if x != 0 and y != 0 and w * h >= 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (234, 53, 57, 255), 2)
            coordinate.append((x,y,w,h))
            a.append(x)
            a.append(y)
            a.append(w)
            a.append(h)

    data.append(a)
    path = "process-pictures/" + name
    cv2.imwrite(path, img)

    return coordinate

def show(path):
    files=os.listdir(path)
    for file in files:
        filepath=path+'/'+file
        p = mpimg.imread(filepath)
        plt.imshow(p)  # 显示图片
        plt.show()


if __name__=="__main__":
    path="pictures"
    files=os.listdir(path)
    csv=list()

    for file in files:
        imagepath=path+'/'+file
        print(separator_character(imagepath, file))

    np.savetxt('reslut.csv', data, fmt='%s', delimiter=',')
    show("process-pictures")