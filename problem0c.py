# Author: Jaclyn Setina

import rosegraphics as rg


window = rg.RoseWindow(700, 400)
x = 100
y = 80
counter = 0
for k in range(6):
    center = rg.Point(x, y)
    circle = rg.Circle(center, 30)
    if k == 0:
        circle.fill_color = 'blue'
        counter = counter +1
    x = x + 60
    circle.attach_to(window)
    window.render(0.5)  # Pauses for 0.05 seconds after rendering.

counter = 0
x = 80
y = 200
for k in range (4):
    center2 = rg.Point(x, y)
    circle2 = rg.Circle(center2, 60)
    if k == 0:
        circle2.fill_color = 'green'
        counter = counter +1
    x = x + 120
    circle2.attach_to(window)
    window.render(0.5)


window.close_on_mouse_click()


window2 = rg.RoseWindow(700, 400)

x = 100
y = 80
for k in range(10):
    center = rg.Point(x, y)
    circle = rg.Circle(center, 30)
    if k == 0:
        circle.fill_color = 'red'
    x = x + 60
    circle.attach_to(window2)
    window2.render(0.5)  # Pauses for 0.05 seconds after rendering.


window2.close_on_mouse_click()



