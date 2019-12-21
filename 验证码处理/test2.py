import qrcode


img=qrcode.make("http://49.235.19.187:5000/")

img.save("test.png")

