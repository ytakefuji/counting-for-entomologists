from PIL import Image,ImageEnhance as ie
import sys

img = Image.open(sys.argv[1])
w,h=img.size
img=img.rotate(270,expand=False)
img = img.resize((756,int(756*h/w)), Image.ANTIALIAS)
img=ie.Brightness(img)
eimg=img.enhance(1.9)
eimg=eimg.crop((100,10,650,550))
eimg.save("p.png") 
