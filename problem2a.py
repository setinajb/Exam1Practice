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


start_point = rg.Point(300, 150)
end_point = rg.Point(100, 250)
line = rg.Line(start_point, end_point)
line.arrow = 'last'
line.attach_to(window)

window.render()
window.continue_on_mouse_click()


circle.fill_color = 'blue'
circle.attach_to(window)

window.render()
window.close_on_mouse_click()





