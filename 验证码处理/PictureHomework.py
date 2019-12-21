import os
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd

def splitimage(img_name,rownum=1, colnum=5, dstpath="pictures"):
    img = Image.open(img_name)
    w, h = img.size
    if rownum <= h and colnum <= w:
        print('Original image info: %sx%s, %s, %s' % (w, h, img.format, img.mode))
        print('开始处理图片切割, 请稍候...')
        s = os.path.split(img_name)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]

        num = 1
        rowheight = h // rownum
        colwidth = w // colnum
        file_list = []
        for r in range(rownum):
            index = 0
            for c in range(colnum):
                factor = []
                # (left, upper, right, lower)
                # box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                if index<1:
                    colwid = colwidth+6
                elif index<2:
                    colwid = colwidth + 1
                elif index < 3:
                    colwid = colwidth

                box = (c * colwid, r * rowheight, (c + 1) * colwid, (r + 1) * rowheight)
                print(colwid,rowheight)
                newfile = os.path.join(dstpath, basename + '_' + str(num) + '.jpg')
                file_list.append(newfile)
                plt_img = img.crop(box)
                plt.imshow(plt_img)
                plt.axis("off")
                plt.show()
                img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.jpg' ))
                num = num + 1
                index+=1
                factor.append(r)
                factor.append(c)
                factor.append(rowheight)
                factor.append(colwid)
                total.append(factor)
        for f in file_list:
            print(f)
    print(total)

#--------------------main（）-----------------------
images = os.listdir('pictures')
images = [os.path.join('pictures',image) for image in images if image.endswith('.jpg')]
print(images)
total = []
imgs = []
i1r = []
i1c = []
i1h = []
i1w = []
i2r = []
i2c = []
i2h = []
i2w = []
i3r = []
i3c = []
i3h = []
i3w = []
i4r = []
i4c = []
i4h = []
i4w = []
i5r = []
i5c = []
i5h = []
i5w = []
for img in images:
    imgs.append(img.split(os.sep)[-1])
    splitimage(img)
for i in range(len(total)):
    if i%5 == 0:
        i1r.append(total[i][0])
        i1c.append(total[i][1])
        i1h.append(total[i][2])
        i1w.append(total[i][3])
    if i%5 == 1:
        i2r.append(total[i][0])
        i2c.append(total[i][1])
        i2h.append(total[i][2])
        i2w.append(total[i][3])
    if i%5 == 2:
        i3r.append(total[i][0])
        i3c.append(total[i][1])
        i3h.append(total[i][2])
        i3w.append(total[i][3])
    if i%5 == 3:
        i4r.append(total[i][0])
        i4c.append(total[i][1])
        i4h.append(total[i][2])
        i4w.append(total[i][3])
    if i%5 == 4:
        i5r.append(total[i][0])
        i5c.append(total[i][1])
        i5h.append(total[i][2])
        i5w.append(total[i][3])

data=pd.DataFrame({'picture':imgs,
                   'y1':i1r,'y2':i1c,'y3':i1h,'y4':i1w,
                   'y5':i2r,'y6':i2c,'y7':i2h,'y8':i2w,
                   'y9':i3r,'y10':i3c,'y11':i3h,'y12':i3w,
                   'y13':i4r,'y14':i4c,'y15':i4h,'y16':i4w,
                   'y17':i5r,'y18':i5c,'y19':i5h,'y20':i5w
                   }) 
data.to_csv('picture.csv',index=False,sep=',')     
