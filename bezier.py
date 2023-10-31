import cairo
#Set up pycairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context (surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint ()

# Bezier curve
ctx.move_to (100, 100)
ctx.curve_to(200, 0, 400, 200, 500, 100)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.stroke()
surface.write_to_png("bez.png")
