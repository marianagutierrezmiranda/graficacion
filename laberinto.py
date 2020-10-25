import pyglet
from pyglet import shapes

window = pyglet.window.Window(fullscreen=True)
square_size = window.height - 20
x = (window.width - square_size)/2
y = (window.height - square_size)/2
line_width = 10
line_color = (0, 0, 125) # RGB Black
batch = pyglet.graphics.Batch()

# Rectangle(x, y, width, height, color=(255, 255, 255), batch=None, group=None)
background = shapes.Rectangle(x-20, y-20, square_size+40, square_size+40, batch=batch)
square = shapes.Rectangle(x, y, square_size, square_size, batch=batch)

# Horizontal lines
# Bottom Row
line01 = shapes.Line(x, y, x+(square_size*.70), y, 
    color=line_color, width=line_width, batch=batch)
line02 = shapes.Line(x+(square_size*.84), y, x+square_size, y, 
    color=line_color, width=line_width, batch=batch)

# 2nd row
line03 = shapes.Line(x, y+(square_size*.14), x+(square_size*.14), y+(square_size*.14), 
    color=line_color, width=line_width, batch=batch)
line04 = shapes.Line(x+(square_size*.28), y+(square_size*.14), x+(square_size*.42), y+(square_size*.14), 
    color=line_color, width=line_width, batch=batch)
line05 = shapes.Line(x+(square_size*.56), y+(square_size*.14), x+(square_size*.70), y+(square_size*.14), 
    color=line_color, width=line_width, batch=batch)

# 3rd row
line06 = shapes.Line(x+(square_size*.42), y+(square_size*.28), x+(square_size*.56), y+(square_size*.28), 
    color=line_color, width=line_width, batch=batch)
line07 = shapes.Line(x+(square_size*.70), y+(square_size*.28), x+(square_size*.84), y+(square_size*.28), 
    color=line_color, width=line_width, batch=batch)

# 4th row 
line11 = shapes.Line(x+(square_size*.56), y+(square_size*.42), x+(square_size*.70), y+(square_size*.42), 
    color=line_color, width=line_width, batch=batch)

# 5th row
line13 = shapes.Line(x+(square_size*.42), y+(square_size*.56), x+(square_size), y+(square_size*.56), 
    color=line_color, width=line_width, batch=batch)

# 6th row 
line16 = shapes.Line(x+(square_size*.14), y+(square_size*.70), x+(square_size*.42), y+(square_size*.70), 
    color=line_color, width=line_width, batch=batch)
line17 = shapes.Line(x+(square_size*.56), y+(square_size*.70), x+(square_size*.84), y+(square_size*.70), 
    color=line_color, width=line_width, batch=batch)

# 7th row
line18 = shapes.Line(x, y+(square_size*.85), x+(square_size*.28), y+(square_size*.85), 
    color=line_color, width=line_width, batch=batch)
line20 = shapes.Line(x+(square_size*.42), y+(square_size*.85), x+(square_size*.70), y+(square_size*.85), 
    color=line_color, width=line_width, batch=batch)

# Top row
line21 = shapes.Line(x, y+(square_size), x+(square_size), y+(square_size), 
    color=line_color, width=line_width, batch=batch)


# Vertical lines
# Left Row
line101 = shapes.Line(x, y, x, y+(square_size*.14), 
    color=line_color, width=line_width, batch=batch)
line102 = shapes.Line(x, y+(square_size*.28), x, y+(square_size), 
    color=line_color, width=line_width, batch=batch)

# 2nd Row
line103 = shapes.Line(x+(square_size*.14), y+(square_size*.14), x+(square_size*.14), y+(square_size*.70), 
    color=line_color, width=line_width, batch=batch)

# 3rd Row
line104 = shapes.Line(x+(square_size*.28), y+(square_size*.28), x+(square_size*.28), y+(square_size*.70), 
    color=line_color, width=line_width, batch=batch)

# 4th Row
line105 = shapes.Line(x+(square_size*.42), y+(square_size*.14), x+(square_size*.42), y+(square_size*.56), 
    color=line_color, width=line_width, batch=batch)
line106 = shapes.Line(x+(square_size*.42), y+(square_size*.70), x+(square_size*.42), y+(square_size*.85), 
    color=line_color, width=line_width, batch=batch)

# 5th Row
line107 = shapes.Line(x+(square_size*.56), y, x+(square_size*.56), y+(square_size*.14), 
    color=line_color, width=line_width, batch=batch)

# 6th Row
line108 = shapes.Line(x+(square_size*.70), y+(square_size*.14), x+(square_size*.70), y+(square_size*.42), 
    color=line_color, width=line_width, batch=batch)
line109 = shapes.Line(x+(square_size*.70), y+(square_size*.70), x+(square_size*.70), y+(square_size*.85), 
    color=line_color, width=line_width, batch=batch)

# 7th Row
line110 = shapes.Line(x+(square_size*.84), y+(square_size*.14), x+(square_size*.84), y+(square_size*.28), 
    color=line_color, width=line_width, batch=batch)
line111 = shapes.Line(x+(square_size*.84), y+(square_size*.42), x+(square_size*.84), y+(square_size*.56), 
    color=line_color, width=line_width, batch=batch)
line112 = shapes.Line(x+(square_size*.84), y+(square_size*.84), x+(square_size*.84), y+(square_size), 
    color=line_color, width=line_width, batch=batch)

# Right Row
line121 = shapes.Line(x+(square_size), y, x+(square_size), y+(square_size), 
    color=line_color, width=line_width, batch=batch)



@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()
