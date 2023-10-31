#using pycairo, draw  a circle with two lines subdividing it into 4 hemispheres
import cairo
from math import pi
def draw_circle(cr):
    x = y = r=10.0; 
    cr.arc (x ,y ,r ,pi/2,3*pi/2)
    cr.stroke()
    #draw the top and bottom halves of the circle as lines
    cr.move_to(x+r,y); cr.line_to(x-r,y); cr.stroke();
    cr.move_to(x,y+r); cr.line_to(x,y-r); cr.stroke();
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 500, 500)
context = cairo.Context(surface)
draw_circle(context)
surface.write_to_png("hemi_sphere.png")
