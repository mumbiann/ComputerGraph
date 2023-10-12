import cairo

# Define a dictionary to store shapes and their respective vertices
shapes = {
    'rectangle': [(150, 100, 100, 240)],
    'triangle': [(300, 100, 400, 100, 350, 50)],
    'pentagon': [(500, 100, 550, 150, 525, 200, 475, 200, 450, 150)],
}

# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Draw shapes
for shape, vertices in shapes.items():
    ctx.set_source_rgb(1, 0, 0)
    for vertex in vertices:
        if shape == 'rectangle':
            ctx.rectangle(*vertex)
        elif shape == 'triangle':
            ctx.move_to(*vertex[0:2])
            for i in range(2, len(vertex), 2):
                ctx.line_to(*vertex[i:i+2])
            ctx.close_path()
        elif shape == 'pentagon':
            ctx.move_to(*vertex[0:2])
            for i in range(2, len(vertex), 2):
                ctx.line_to(*vertex[i:i+2])
            ctx.close_path()
    ctx.fill()

# Save the output to a PNG file
surface.write_to_png("ann.png")
