import cairo

# Create a PNG surface
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 600)
ctx = cairo.Context(surface)

# Set the line width and color
ctx.set_line_width(5)
ctx.set_source_rgb(255, 0, 0)  # Black color

# Define the triangle's vertices
x1, y1 = 10, 50
x12, y12 = 10, 40
x2, y2 = 10, 300
x22, y22 = 500,40
x3, y3 = 500, 300
x32, y32 = 500, 290

# Move to the first vertex
ctx.move_to(x1, y1)


# Draw lines to the other vertices
ctx.line_to(x2, y2)
ctx.line_to(x3, y3)

# Close the path to complete the triangle
ctx.close_path()

# Stroke (outline) the triangle
ctx.stroke()

#second triangle

# fill the triangle with red 
ctx.move_to(x12, y12)
ctx.line_to(x22, y22)
ctx.line_to(x32, y32)
ctx.close_path()
ctx.set_source_rgb(1, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(5)
ctx.stroke()
surface.write_to_png("triangle2.png")

# Cleanup
ctx.show_page()