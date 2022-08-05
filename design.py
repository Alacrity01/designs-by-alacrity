# import tkinter as tk
from signal import sigpending
import turtle as trt

import rgb_colors_by_alacrity as CustomColors


# def single_quadrant(y_max, d, t1):
# 	t1.pendown()
# 	delta_x = d
# 	delta_y = -d
# 	y = y_max
# 	x = 0
# 	finish = y_max
# 	while abs(x) <= abs(finish): # draws quadrant
# 		t1.penup()  
# 		t1.setpos(0,y)
# 		t1.pendown()
# 		t1.goto(x,0)
# 		x += delta_x
# 		y += delta_y




# def run_design(theme_name, y_max=None, d=None):
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

	s.bgcolor(my_background)  # background color
	t1.pencolor(my_line)   # line color
	p1.pencolor(my_pen)   # line color

	t1.ht() # hide both turtle objects
	p1.ht() # hide both turtle objects
	s.tracer(50) # no drawing animation



	# s = trt.Screen() # instantiate Screen with Turtle.Screen()
	# s.colormode(255) # change screen instance to RGB colormode
	# trt.TurtleScreen(s)
	# trt.bgcolor(my_canvas_color)  # background color


	# t1.speed(10.5)
	# pen_1.pencolor((150,150,150))






	# y_max = 500 # y_max will determine size of drawing
	# d = 10 # d is for delta -- an integer of pixels to change with each new line


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
		# finish = y_max
		y = y_max
		x = 0
		# while abs(x) <= abs(finish): # draws quadrant
		while abs(x) <= abs(y_max): # draws quadrant
			t1.penup()  
			t1.setpos(0,y)
			t1.pendown()
			t1.goto(x,0)
			x += delta_x
			y += delta_y



	# def single_quadrant(y_max, d, t1):
	# t1.pendown()
	# delta_x = d
	# delta_y = -d
	# y = y_max
	# x = 0
	# finish = y_max
	# while abs(x) <= abs(finish): # draws quadrant
	# 	t1.penup()  
	# 	t1.setpos(0,y)
	# 	t1.pendown()
	# 	t1.goto(x,0)
	# 	x += delta_x
	# 	y += delta_y

# single_quadrant(0,  y_max,  d, -d) 

run_design('stone_age')


# def draw_4_quadrants():

# y_max = 500
# delta = 10

# for v in delta_vectors:
# 	y_max = abs(y_max) * v[0]
# 	delta_x = abs(delta) * v[1]
# 	delta_y = abs(delta) * v[2]
# 	x = 0
# 	while abs(x) <= abs(finish): # draws quadrant
# 		t1.penup()  
# 		t1.setpos(0,y)
# 		t1.pendown()
# 		t1.goto(x,0)
# 		x += delta_x
# 		y += delta_y

# single_quadrant(0,  y_max, -d, -d) # delta_x *= -1; delta_y *= 1
# single_quadrant(0, -y_max, -d,  d) # delta_x *= 1; delta_y *= -1
# single_quadrant(0, -y_max,  d,  d) # delta_x *= -1; delta_x *= 1


	# if my_design == 'single_quadrant':
	# 	single_quadrant(y_max, d, t1)



# colors_dict = CustomColors.get_colors_dict()
# themes = CustomColors.get_themes()


# y_max = 500 # y_max will determine size of drawing
# d = 10 # d is for delta -- an integer of pixels to change with each new line


# theme_name = 'stone_age'
# themes_dict = CustomColors.get_themes()
# theme = themes_dict[theme_name]

# print(theme[0])
# print(theme[1])
# print(theme[2])


# print("-" * 100)
# print("-" * 100)
# print(colors_dict)
# # print("." * 100)
# print(themes)

# print("-" * 100)
# print("-" * 100)

# my_theme = themes['stone_age']


# y_max = 500 # y_max will determine size of drawing
# d = 10 # d is for delta -- an integer of pixels to change with each new line


# prepare(my_theme)




# single_quadrant(0,  y_max,  d, -d) # quadrant I
# t1.penup()
# single_quadrant(0,  y_max, -d, -d) 
# t1.penup()
# single_quadrant(0, -y_max, -d,  d)
# t1.penup()
# single_quadrant(0, -y_max,  d,  d)
trt.exitonclick()
trt.mainloop()