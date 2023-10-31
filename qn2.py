import cairo

surface = cairo.ImageSurface(cairo. FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.rectangle(150, 100, 100, 240)
ctx.set_source_rgb(1, 0.9, 1)
ctx.fill()

output_dir = "outputs"  
output_filename = "image.png"  
surface.write_to_png(f"{output_dir}/{output_filename}")
surface.finish() 
