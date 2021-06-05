import cv2,sys
from time import sleep
canny=75
def main(f,canny):
 img = cv2.imread(f)
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
 outline = cv2.Canny(blurred, 0, int(canny)*coeff)
 outline= cv2.GaussianBlur(outline, (3,3), 0)
 cv2.imshow("The edges", outline)
 cv2.imwrite("edges.png", outline)
#(_, cnts, _) = cv2.findContours(outline, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#version4
 ( cnts, _)=cv2.findContours(outline,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
 cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)
 cv2.putText(img,str(len(cnts)),(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
 cv2.imwrite("r.png",img)
 cv2.imshow("Result", img)
 print("%i blobs" % len(cnts))
 sleep(2)
#cv2.waitKey(0)
 cv2.waitKeyEx(4000)
if len(sys.argv)==1: 
 print('image file is needed!')
 sys.exit()
if len(sys.argv)==2: f=sys.argv[1]
if len(sys.argv)==3: 
 f=sys.argv[1]
 canny=sys.argv[2]
main(f,canny)
