from PIL import Image
import os
p = r"G:/My Drive/Programming/Portfolio-Kian-Maleki-main/Portfolio_photo.jpg"
if not os.path.exists(p):
    print('MISSING')
    raise SystemExit(1)
img = Image.open(p)
img = img.convert('RGBA')
img.thumbnail((200,200))
pal = img.convert('P', palette=Image.ADAPTIVE, colors=6)
palette = pal.getpalette()
color_counts = sorted(pal.getcolors(), reverse=True)
colors = []
for count, idx in color_counts[:6]:
    r = palette[idx*3]
    g = palette[idx*3+1]
    b = palette[idx*3+2]
    colors.append((r,g,b))
def tohex(c):
    return '#%02x%02x%02x' % c
out = [tohex(c) for c in colors]
print(','.join(out))
