import os
import cv2
pasta="Imagens"
imagens=[]
for file in os.listdir(pasta):
    nome,ext=os.path.splitext(file)
    if ext in[".jpg"]:
        file_name=pasta+"/"+file
        imagens.append(file_name)
count=len(imagens)
frame=cv2.imread(imagens[0])
height,width,layers=frame.shape
size=(width,height)
video=cv2.VideoWriter("video.avi",cv2.VideoWriter_fourcc(*"DIVX"),1,size)
for i in range(0,count):
    frame=cv2.imread(imagens[i])
    video.write(frame)
video.release()
print("Concluido!")