# Counting the number of dead bugs for entomologists
<pre>
Counting the number of dead bugs or insect corpses on a plane is a very 
time-consuming task. 
The proposed approach is based on BLOB. The term "BLOB" stands for "Binary Large Object".
Without machine learning, the Python program (pillbug_coun.py) can count the number of objects in a picture.
The conventional machine learning needs to collect and annotate a variety of images which is a time-consuming task.

This repository shows how to use a Python program (pillbug_count.py) 
for novice users to automatically calculate the number of dead bugs or 
the number of insect corpses on a plane for entomologists.

In order to run pillbug_count.py, you should see the following repository 
for installing the necessary libraries:
<a href="https://github.com/ytakefuji/python-novice"> How to install libraries</a>

1. To install an executable Python environment on your operating system 
   (Windows, Mac, Linux), 
   download a Miniconda3 .sh file or .exe file for Python3.8 or Python3.7 
   from the following site:
   https://docs.conda.io/en/latest/miniconda.html
2. Double-click Miniconda3 .exe file or run the following bash command on your terminal:
   $ bash Miniconda3XXX.sh
3. You need to install opencv libray, type the following pip command for installation:
   $ pip install opencv-python
4. To run pillbug_count.py, run the following command for testing:
   $ python pillbug_count.py pillbug.png
</pre>
<img src='result1.png' height=246 width=1031>
<img src='result2.png' height=380 width=366>
<pre>
   $ python pillbug_count.py flies.png
</pre>
<img src='flies.png' height=200 width=300><img src='gray.png' height=200 width=300>
<img src='blur.png' height=200 width=300><img src='edges.png' height=200 width=300>
<img src='r.png' height=200 width=300>
You should resize an original picture for counting the number of dead bugs. 
Or you should tune the Canny coefficient.

# Tuning parameters for counting in general
pillbug_count.py is shown as follows:
<pre>
import cv2,sys
if len(sys.argv)<2: 
 print("enter figure name")
 sys.exit()

img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
blurred = cv2.GaussianBlur(blurred, (7,7), 0)

cv2.imshow("grey scale", gray)
cv2.imwrite("gray.png", gray)
cv2.imshow("blurred", blurred)
cv2.imwrite("blur.png", blurred)
coeff=int((blurred.max()-blurred.min())/100)
if coeff==1: coeff=1 
else: coeff=3
outline = cv2.Canny(blurred, 0, 75*coeff)
outline= cv2.GaussianBlur(outline, (3,3), 0)
cv2.imshow("The edges", outline)
cv2.imwrite("edges.png", outline)
(_, cnts, _) = cv2.findContours(outline, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#version4
#( cnts, _)=cv2.findContours(outline,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)
cv2.putText(img,str(len(cnts)),(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
cv2.imshow("Result", img)
cv2.imwrite("r.png",img)
print("%i blobs" % len(cnts))
cv2.waitKey(0)
</pre>

# Resizing a picture
<pre>
The most important tuning point lies in the size of a picture containing the target objects.
The following Python program can be used for resizing the picture (p.jpg: 4032x3024).
This program is tuned for a smartphone.
resize.py can convert p.jpg: 4032x3024 to p.png: 550 x 540.
p.jpg was taken by my smartphone. resize.py is to generate the resized p.png file from p.jpg.
$ python resize.py p.jpg
</pre>
resize.py can be changed by modifying integer 756 in img = img.resize((756,int(756*h/w)), Image.ANTIALIAS).
<pre>
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

</pre>
# Tune Canny coefficient
<pre>
You should tune and change Canny coefficient instead of "75". 
outline = cv2.Canny(blurred, 0, 75*coeff)
</pre>
