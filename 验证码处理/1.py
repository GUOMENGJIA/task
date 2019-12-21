import os

images = os.listdir('pictures')
for i in range(len(images)):
    images[i]='pictures/'+images[i]
#    print(images[i])
imgs=[]
for img in images:
    imgs.append(img.split(os.sep)[-1])
print(imgs)