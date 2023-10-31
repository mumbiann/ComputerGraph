import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 500)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.arc(300, 250, 100, 0, 2*math.pi)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png(f"outputs/circle2.png")
