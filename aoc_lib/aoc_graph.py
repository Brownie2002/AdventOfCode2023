import math
import random
import re
import string
import sys

import pandas as pd
from PIL import Image, ImageDraw, ImageFont


def graph(df, filename="output.png", font_size=18):
    """Create a PNG file from ASCII DataFrame

    Args:
        df (DataFrame): DataFrame to save as a PNG
        filename (String): Name of the output
        font_size (int): Size of the font to use

    Returns:
        int: Success
    """

    # TODO : Need to handle the space correctly here ...
    txt = df.to_string(index=False, header=False)
    txt = re.sub("[]()[{} ']","",txt)
    txt = re.sub("Z"," ",txt)

    font_path='/opt/venv/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono.ttf'
    font = ImageFont.truetype(font_path,font_size)

    # Retrieve the max value of the font
    font_lenght = 0
    font_size = 0
    for i in set(txt):
        left, top, right, bottom = font.getbbox("@")
        if right + left > font_lenght: font_lenght = right + left
        if top + bottom > font_size: font_size = top + bottom

    im_width  = math.ceil(font_lenght * len(df.columns))
    im_height = math.ceil(font_size   * len(df.index))
    im = Image.new("RGBA",(im_width,im_height),(0,0,0))

    draw = ImageDraw.Draw(im)

    draw.text( (0,0), txt, font=font)

    del draw

    im.save(filename)
    
    return 0

def main() -> int:
    # Print a Pandas Dataframe

    char1 = random.choice(string.ascii_uppercase)
    d = ["☺️", "\u0394",8], [char1, random.randrange(0, 9),4]
    df = pd.DataFrame(data=d)

    graph(df)

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit