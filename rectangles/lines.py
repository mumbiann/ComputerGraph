import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 500)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

#closed shape
ctx.move_to(50, 50)
ctx.line_to(50, 150)
ctx.line_to(100, 75)
ctx.close_path()
ctx.set_source_rgb(1, 0, 1)
ctx.set_line_width(5)
ctx.stroke()

#open polygon
ctx.move_to(200, 75)
ctx.line_to(200, 150)
ctx.line_to(300, 150)
ctx.line_to(400, 100)
ctx.line_to(400, 75)
ctx.set_source_rgb(1, 0.8, 0.8)
ctx.set_line_width(5)
ctx.stroke()


surface.write_to_png(f"outputs/lines.png")