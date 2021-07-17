#!/usr/bin/python3
from PIL import Image
from shutil import get_terminal_size

def checker(size):
    img = Image.new("RGB", size)
    s = True
    for x in range(img.width):
        for y in range(img.height):
            col = (165, 165, 165) if s else (85, 85, 85)
            img.putpixel((x, y), col)
            s = not s
        s = not s
    return img

def display(img, alphacheck=True):
    img = img.convert("RGBA")
    termsize = get_terminal_size((80, 24))
    img.thumbnail((termsize.columns, termsize.lines * 2))
    if alphacheck:
        bg = checker(img.size)
        bg.paste(img, (0, 0), img)
        img = bg
    for y in range(0, img.height, 2):
        thisline = ""
        for x in range(img.width):
            px = img.getpixel((x, y))
            thisline += f"\x1B[48;2;{px[0]};{px[1]};{px[2]}m"
            px = img.getpixel((x, y + 1))
            thisline += f"\x1B[38;2;{px[0]};{px[1]};{px[2]}m"
            thisline += "▄"
        thisline += "\x1B[0m"
        print(thisline)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("please specify filename(s)")
        sys.exit(1)
    for fname in sys.argv[1:]:
        if len(sys.argv) > 2: print(fname)
        display(Image.open(fname))
