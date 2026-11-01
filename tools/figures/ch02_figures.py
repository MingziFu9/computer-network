# 第 2 章配图（编者用）：先运行 labs/ch02 的四个实验，再运行本脚本

import cv2, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["WenQuanYi Zen Hei"]; plt.rcParams["axes.unicode_minus"]=False
from pathlib import Path; R=str(Path(__file__).resolve().parents[2])+"/"
D=R+"labs/data/images/"; L=R+"labs/ch02/"
O=R+"docs/chapters/02-image-processing/images/"
rgb=lambda im: cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
def grid(ims, titles, path, rows, cols, size, gray=()):
    fig,ax=plt.subplots(rows,cols,figsize=size)
    for a,im,t,i in zip(np.ravel(ax),ims,titles,range(99)):
        if im.ndim==2: a.imshow(im,cmap="gray",vmin=0,vmax=255)
        else: a.imshow(rgb(im))
        a.set_title(t,fontsize=12); a.axis("off")
    plt.tight_layout(); plt.savefig(O+path,dpi=110,bbox_inches="tight"); plt.close()
# 1 geometry
lane=cv2.imread(D+"lane_yellow.jpg"); h,w=lane.shape[:2]
roi=lane[h//2+50:,:]
small=cv2.resize(lane,(320,180))
M=cv2.getRotationMatrix2D((w/2,h/2),15,1.0); rot=cv2.warpAffine(lane,M,(w,h))
flip=cv2.flip(lane,1)
grid([lane,roi,cv2.resize(small,(w,h),interpolation=cv2.INTER_NEAREST),rot,flip,cv2.cvtColor(lane,cv2.COLOR_BGR2GRAY)],
 ["原图 960×540","裁剪：只留下半部分 960×220","缩放：320×180（放大显示能看到格子）","旋转 15°","左右翻转","转灰度"],"geometry.jpg",2,3,(13,5.2))
# 2 HSV channels
hsv=cv2.cvtColor(lane,cv2.COLOR_BGR2HSV)
grid([lane,(hsv[:,:,0].astype(float)*1.4).astype(np.uint8),hsv[:,:,1],hsv[:,:,2]],["原图","H 色调（越亮越偏蓝紫）","S 饱和度（黄线最亮，鲜艳）","V 亮度（白线、黄线、天空都亮）"],"hsv_channels.jpg",2,2,(10,6))
# 3 night fix
n=cv2.imread(D+"drive_night.jpg")
grid([n,cv2.imread(L+"lab2_2_bright.jpg"),cv2.imread(L+"lab2_2_equal.jpg"),cv2.imread(L+"lab2_2_clean.jpg")],
 ["① 原图：平均亮度 24","② 亮度×2+20：平均 64.9，天空“过曝”","③ 直方图均衡化：平均 93.3，噪点也变明显","④ 再做中值滤波：噪点少了"],"night_fix.jpg",4,1,(10,13))
# 4 filters
city=cv2.imread(D+"drive_city.jpg")[150:330,380:700]
rng=np.random.default_rng(0)
noisy=city.copy(); m=rng.random(noisy.shape[:2])
noisy[m<0.04]=0; noisy[m>0.96]=255
g=np.clip(city.astype(float)+rng.normal(0,20,city.shape),0,255).astype(np.uint8)
grid([noisy,cv2.blur(noisy,(5,5)),cv2.GaussianBlur(noisy,(5,5),0),cv2.medianBlur(noisy,5),
      g,cv2.blur(g,(5,5)),cv2.GaussianBlur(g,(5,5),0),cv2.medianBlur(g,5)],
 ["椒盐噪声","均值滤波 5×5","高斯滤波 5×5","中值滤波 5×5","高斯噪声","均值滤波 5×5","高斯滤波 5×5","中值滤波 5×5"],"filters.jpg",2,4,(14,5))
# 5 threshold
p=cv2.imread(D+"pills.jpg"); pg=cv2.cvtColor(p,cv2.COLOR_BGR2GRAY)
_,t1=cv2.threshold(pg,127,255,cv2.THRESH_BINARY)
_,t2=cv2.threshold(pg,200,255,cv2.THRESH_BINARY)
otsu,t3=cv2.threshold(pg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("otsu",otsu)
grid([p,t1,t2,t3],["药片照片","门槛 127",f"门槛 200（药片变小、有小洞）",f"自动门槛（大津法，算出 {otsu:.0f}）"],"threshold.jpg",1,4,(15,3.4))
# 6 id photo
grid([cv2.imread(L+"lab2_1_blue.jpg"),cv2.imread(L+"lab2_1_mask.png",0),cv2.imread(L+"lab2_1_white.jpg")],["① 裁剪、缩放到 295×413","② HSV 找出的蓝色（白色部分）","③ 换成白底"],"id_photo.jpg",1,3,(9,4.4))
# 7 lane color
grid([cv2.imread(L+"lab2_3_mask.png",0),cv2.imread(L+"lab2_3_lanes.jpg")],["黄或白的像素（只看下半部分）","涂红后放回原图"],"lane_color.jpg",1,2,(13,3.6))
# hist
import shutil; shutil.copy(L+"lab2_2_hist.png",O+"night_hist.png")
