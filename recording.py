import cairo

# Create a recording surface
recording_surface = cairo.RecordingSurface(cairo.CONTENT_COLOR_ALPHA, None)

# Create a context for the recording surface
context = cairo.Context(recording_surface)

# Draw on the recording surface
context.set_source_rgb(1.0, 0.0, 0.0)  # Red color
context.rectangle(50, 50, 100, 100)
context.fill()

context.set_source_rgb(0.0, 0.0, 1.0)  # Blue color
context.arc(200, 200, 50, 0, 2 * 3.14)  # Draw a blue circle
context.fill()

# Now let's reproduce the recorded drawing on another surface

# Create a PNG surface to display the recorded content
output_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 300, 300)
output_context = cairo.Context(output_surface)

# Reproduce the recorded drawing on the output surface
output_context.set_source_surface(recording_surface)
output_context.paint()

# Save the output surface to a PNG file
output_surface.write_to_png("recorded_drawing.png")

# Clean up the surfaces
recording_surface.finish()
output_surface.finish()
