# import tkinter as tk
from signal import sigpending
import turtle as trt

import rgb_colors_by_alacrity as CustomColors

def run_design(theme_name):

	themes_dict = CustomColors.get_themes()
	theme = themes_dict[theme_name]

	# set colors
	my_background = theme[0]
	my_line = theme[1]
	my_pen = theme[2]

	cv = trt.getcanvas() # instantiate canvas with Turtle.getcanvas()
	root = cv.winfo_toplevel()
	root.overrideredirect(1)

	trt.setup(width=1.0, height=1.0) 
	trt.colormode(255)

	s = trt.Screen() # instantiate Screen with Turtle.Screen()
	t1 = trt.RawPen(s) # turtle object to draw on screen instance (s)
	p1 = trt.RawPen(s) # turtle object to draw on screen instance (s)
	p2 = trt.RawPen(s) # turtle object to draw on screen instance (s)

	s.bgcolor(my_background)  # background color
	t1.pencolor(my_line)   # line color
	p1.pencolor(my_pen)   # text color
	p2.pencolor(my_line)   # line color <- used with 2nd pen

	t1.ht() # hide both turtle objects
	p1.ht() # hide both turtle objects
	s.tracer(50) # no drawing animation

	y_max = 500 # height of a quadrant (a coordinate in pixels)
	delta = 10 # pixels to change with each new line (integer)

	delta_vectors = [
		[1, 1, -1],
		[1, -1, -1],
		[-1, -1, 1],
		[-1, 1, 1]
	]

	for v in delta_vectors:
		y_max = abs(y_max) * v[0]
		delta_x = abs(delta) * v[1]
		delta_y = abs(delta) * v[2]
		y = y_max
		x = 0
		while abs(x) <= abs(y_max): # draws quadrant
			t1.penup()  
			t1.setpos(0,y)
			t1.pendown()
			t1.goto(x,0)
			x += delta_x
			y += delta_y
	
	p1.penup() # no drawing when moving
	p1.forward((p1.getscreen().window_width() / 2) - 25)
	p1.left(90)
	p1.forward((p1.getscreen().window_height() / 2) - 25)
	message = theme_name
	p1.write(message, move=True, font=('arial',20,'bold'), align='right')

	
	p2.penup() # no drawing when moving
	p2.forward((p2.getscreen().window_width() / 2) - 25)
	p2.left(90)
	p2.forward((p2.getscreen().window_height() / 2) - 50)
	sign_text = "Design by Alacrity"
	p2.write(sign_text, move=True, font=('arial',20,'bold'), align='right')

run_design('cyberslate')

trt.exitonclick()
trt.mainloop()