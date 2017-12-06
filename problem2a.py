# Author: Jaclyn Setina

import rosegraphics as rg

window = rg.RoseWindow(700, 400)

center = rg.Point(100, 50)
circle = rg.Circle(center, 40)
circle.fill_color = 'red'
circle.attach_to(window)


corner_1 = rg.Point(100, 150)
corner_2 = rg.Point(300, 250)
rectangle = rg.Rectangle(corner_1, corner_2)
rectangle.outline_color = 'blue'
rectangle.attach_to(window)

window.render()
window.continue_on_mouse_click()




