import cairo

_OUTPUTFILE = "outputs/"

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 200)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.move_to(100, 30)
ctx.line_to(100, 100)

ctx.curve_to(100 + 250, 50, 100 + 50, 50, 100 + 200, 100)
ctx.line_to(100, 30)
ctx.close_path()
ctx.set_source_rgb(1, 1, 1)
ctx.fill_preserve()
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(5)
ctx.stroke()



surface.write_to_png(f"{_OUTPUTFILE}shapes2.png")
