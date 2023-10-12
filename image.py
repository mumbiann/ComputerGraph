import cairo

#set up surface
surface= cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 400)
'''When we create the surface, we are also specifying the type of output.
An ImageSurface will create a PNG image as output. There are other types of surfaces that create different output formats, for example SVG and PDF.
We set the format to FORMAT_RGB24, which is a normal RGB image. We set the output image’s size to 600 by 400 pixels
'''
ctx = cairo.Context(surface)
'''
This is used to create a context. A context is a tool we use to draw on the surface.
We can think of it as being analogous to a pen that is used to draw. However, this is a somewhat weak analogy.
'''
ctx.set_source_rgb(0.8, 0.8, 0.8)
'''We will fill the entire surface with a light gray color, using the paint function.'''
ctx.paint()

#Draw the image
# red rectangle
ctx.rectangle(100, 100, 100, 240)
'''
The rectangle(x,y,width,height) function adds a rectangle shape to the path.
It doesn’t draw a rectangle. Instead, it adds it to the plan of what we are intending to draw.
It specifies a rectangle placed at a position (x, y), with a certain width and height. Our code will place a rectangle at the (150, 100) position, with a width of 100 pixels and a height of 240 pixels
'''
ctx.set_source_rgb(1, 0, 0)
'''
Using set_source_rgb, set the color to (1, 0, 0), which is a bright red.
Call the fill function. This function looks at the path we have defined and fills it with the color we previously selected. 
The fill function is what actually draws the shape which, in this case, is a rectangle.
'''
ctx.fill()

#Green rectangle
ctx.rectangle(250, 100, 100, 240) 
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

#blue square
ctx.rectangle(400, 100, 100, 240) 
ctx.set_source_rgb(0, 1, 0)
ctx.set_line_width(5)
ctx.stroke()

#blue square fill and stroke
ctx.rectangle(550, 100, 100, 240) 
ctx.set_source_rgb(0, 0, 1)
ctx.fill_preserve()
ctx.set_source_rgb(0,0,0)
ctx.set_line_width(10)
ctx.stroke()

surface.write_to_png("output.png")