import os




'''二值化图片'''
def get_most(arr):
    M, N = arr.shape[0], arr.shape[1]
    most=list()
    for i in range(M):
        most.append(stats.mode(arr[i])[0][0])
   # print("每一行的众数：",most)
    most = np.array(most,dtype=np.float)

    return most[0]

path="train/train"
files=os.listdir(path)

for i in arange(1,len(files)):

    image_path = path + '/' + files[i]
    image = Image.open(image_path).convert('L')
    image.save("./pil_pray/new"+files[i])
    most=int(get_most(np.array(image)))

    t=Image.open(image_path).convert('L').point(lambda x:255 if x >(most-10) and x<(most+10) else 0)
    t.save('./pil_0-1/new'+files[i])


'''切分图片'''
#保存
def save_images(image_list,img_name):
    name=img_name.split(".")[0]

    for i in range(len(image_list)):
        path=str(labels.index(name[i+3]))
        num=str(len(os.listdir('SeparateImages/'+path)))
        image_list[i].save('SeparateImages/'+path+ '/'+num+'.png', 'PNG')

def cutImage(image,name):
    width, height = image.size
    item_width = int(width / 5)
    box_list = []
    '''(0,0,30,30)(30,0,60,30)(60,0,90,30)(90,0,120,30)(120,0,150,30)'''
    for i in range(0, 5):
        box = (i * item_width, 0, (i + 1) * item_width, height)
        box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    save_images(image_list, name)

if __name__=="__main__":
    path="pil_0-1"
    files=os.listdir(path)
    i=0
    for file in files:
        image_path=path+'/'+file
        image = Image.open(image_path)
        cutImage(image,file)