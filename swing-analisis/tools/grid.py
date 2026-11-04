import sys, cv2, numpy as np
video, out = sys.argv[1], sys.argv[2]; frames=[int(x) for x in sys.argv[3].split(',')]
cap=cv2.VideoCapture(video); fr=[]
while True:
    ok,f=cap.read()
    if not ok: break
    fr.append(f)
tiles=[]
for i in frames:
    im=cv2.resize(fr[i],None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
    for x in range(0,im.shape[1],40): cv2.line(im,(x,0),(x,im.shape[0]),(255,255,255) if x%200==0 else (180,180,180),1)
    for y in range(0,im.shape[0],40): cv2.line(im,(0,y),(im.shape[1],y),(255,255,255) if y%200==0 else (180,180,180),1)
    for x in range(0,im.shape[1],200): cv2.putText(im,str(x//2),(x+2,14),cv2.FONT_HERSHEY_SIMPLEX,.45,(0,0,255),1)
    for y in range(0,im.shape[0],200): cv2.putText(im,str(y//2),(2,y+14),cv2.FONT_HERSHEY_SIMPLEX,.45,(0,0,255),1)
    cv2.putText(im,f"f{i}",(560,30),cv2.FONT_HERSHEY_SIMPLEX,.9,(0,255,255),2)
    tiles.append(im)
cv2.imwrite(out,np.hstack(tiles))
