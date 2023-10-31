import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 700, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.rectangle(100, 150, 100, 240)
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

ctx.rectangle(300, 150, 100, 240)
ctx.set_source_rgb(1, 0, 1)
ctx.set_line_width(5)
ctx.stroke()

ctx.rectangle(500, 150, 100, 240)
ctx.set_source_rgb(1, 1, 0)
ctx.fill_preserve()
ctx.set_source_rgb(0, 1, 0)
ctx.set_line_width(7)
ctx.stroke()


# Save the output to a PNG file
surface.write_to_png(f"outputs/ann.png")


