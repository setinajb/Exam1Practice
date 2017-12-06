# Author: Jaclyn Setina

import rosegraphics as rg

window = rg.RoseWindow(550, 500)

x = 100
y = 100
x2 = 140
y2 = 120
point1 = rg.Point(x, y)
point2 = rg.Point(x2, y2)
for k in range(6):
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)
    x = x - 15
    y = y - 15
    point1 = rg.Point(x, y)
    x2 = x2 +15
    y2 = y2 + 15
    point2 = rg.Point(x2, y2)
    if k == 0:
        rectangle.fill_color = 'blue'


# Doing the green rectangle part
x = 350
y = 200
x2 = 400
y2 = 300
point1 = rg.Point(x, y)
point2 = rg.Point(x2, y2)
for k in range(3):
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)
    x = x - 50
    y = y - 50
    point1 = rg.Point(x, y)
    x2 = x2 + 50
    y2 = y2 + 50
    point2 = rg.Point(x2, y2)
    if k == 0:
        rectangle.fill_color = 'green'

window.render()
window.close_on_mouse_click()


window2 = rg.RoseWindow(550, 500)
x = 200
y = 200
x2 = 250
y2 = 250
point1 = rg.Point(x, y)
point2 = rg.Point(x2, y2)
for k in range(10):
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window2)
    x = x - 12
    y = y - 12
    point1 = rg.Point(x, y)
    x2 = x2 + 12
    y2 = y2 + 12
    point2 = rg.Point(x2, y2)
    if k == 0:
        rectangle.fill_color = 'red'

window2.render()
window2.close_on_mouse_click()




