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
window.continue_on_mouse_click()

# TEST 2

center = rg.Point(500, 150)
circle2 = rg.Circle(center, 80)
circle2.attach_to(window)

corner_1 = rg.Point(500, 150)
corner_2 = rg.Point(700, 250)
rectangle2 = rg.Rectangle(corner_1, corner_2)
rectangle2.outline_color = 'green'
rectangle2.attach_to(window)

window.render()
window.continue_on_mouse_click()

start_point = rg.Point(700, 150)
end_point = rg.Point(500, 250)
line = rg.Line(start_point, end_point)
line.arrow = 'last'
line.attach_to(window)

window.render()
window.continue_on_mouse_click()

circle2.fill_color = 'green'
window.render()
window.close_on_mouse_click()


window2 = rg.RoseWindow(400, 700)

center = rg.Point(200, 150)
circle = rg.Circle(center, 100)
circle.fill_color = 'yellow'
circle.attach_to(window2)

point_1 = rg.Point(100, 250)
point_2 = rg.Point(300, 600)
rectangle3 = rg.Rectangle(point_1, point_2)
rectangle3.attach_to(window2)

window2.render()
window2.close_on_mouse_click()


