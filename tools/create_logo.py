from pathlib import Path
import math
from PIL import Image, ImageDraw
SIZE=512
out=Path("app/src/main/res/drawable-nodpi/ic_launcher_new.png")
out.parent.mkdir(parents=True, exist_ok=True)
im=Image.new("RGBA",(SIZE,SIZE),(15,24,35,255)); p=im.load()
for y in range(SIZE):
 for x in range(SIZE):
  g=max(0.0,1.0-math.hypot(x-256,y-220)/390)
  p[x,y]=(int(15+10*g),int(24+28*g),int(35+30*g),255)
d=ImageDraw.Draw(im)
d.rounded_rectangle((24,24,488,488),radius=112,fill=(22,38,51,255),outline=(91,139,121,255),width=8)
d.rounded_rectangle((92,94,420,286),radius=35,fill=(39,65,76,255),outline=(111,164,135,255),width=8)
for bx,by in [(135,180),(190,145),(245,180),(300,145),(355,180)]:
 d.rectangle((bx-12,by+22,bx+12,by+58),fill=(113,184,108,255))
 d.polygon([(bx,by-20),(bx-27,by+18),(bx,by+7),(bx+27,by+18)],fill=(162,211,130,255))
d.polygon([(70,350),(145,292),(205,326),(278,258),(352,315),(442,268),(442,420),(70,420)],fill=(62,126,88,255))
d.line([(70,350),(145,292),(205,326),(278,258),(352,315),(442,268)],fill=(133,190,123,255),width=13,joint="curve")
ov=Image.new("RGBA",(SIZE,SIZE),(0,0,0,0)); q=ImageDraw.Draw(ov)
q.line((130,390,360,120),fill=(236,190,91,255),width=24);q.line((130,390,360,120),fill=(255,225,151,255),width=8)
q.rounded_rectangle((105,380,155,430),radius=13,fill=(153,95,54,255),outline=(245,204,128,255),width=5)
q.ellipse((340,94,380,134),fill=(238,190,91,255),outline=(255,230,165,255),width=6)
im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im)
for x,y,r in [(395,94,10),(92,245,7),(410,350,8)]:
 d.line((x-r,y,x+r,y),fill=(255,229,157,255),width=4);d.line((x,y-r,x,y+r),fill=(255,229,157,255),width=4)
im.save(out,optimize=True)
print("Pillow logo generated:",out)
