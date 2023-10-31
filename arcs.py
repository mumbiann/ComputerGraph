import cairo
import math

surface= cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.arc(50, 50, 100, 0, math.pi/2)
ctx.set_source_rgb(1, 0.8, 0)
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png('arc.png')