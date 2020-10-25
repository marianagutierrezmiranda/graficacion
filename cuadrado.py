import pyglet
from pyglet import shapes

#window = pyglet.window.Window(fullscreen=True)
window = pyglet.window.Window(350, 350)
batch = pyglet.graphics.Batch()
square_size = 100
x = 0
y = window.height - square_size
square = shapes.Rectangle(x, y, square_size, square_size, color=(93, 173, 226 ), batch=batch)

square.rotation = 45
square.width = square.width * 2
square.height = square.height * 2
square.position = ((window.width - square.width)*0.25 , window.height/2)


@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()
