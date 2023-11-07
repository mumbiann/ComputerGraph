import math
import cairo
import logging
from datetime import datetime
_OUTPUTFILE = "outputs/"


surface= cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 800)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.rectangle(200, 200, 400,400)
ctx.set_source_rgb(0,8, 0.8, 0.8)
ctx.set_line_width(5)
ctx.stroke()