from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *

class Clock:
	def __init__(self, root):
		self.root = root
		self.root.title("Analog Clock")
		self.root.geometry("1370x800+0+0")
		self.root.config(bg = "#082d68")
		title = Label(self.root, text = "Indian Standard Time", bd = 5, relief = GROOVE, bg = "#164bcd", fg = "white", font = ("", 45, "bold"))
		title.place(x = 0, y = 50, relwidth = 1)
		self.lbl = Label(self.root, bg = "white", bd = 20, relief = RAISED)
		self.lbl.place(x = 450, y = 150, height = 500, width = 500)
		self.working_clock()

	def clock_image(self, hr, _min, sec):
		clock = Image.new("RGB", (400,400), (255, 255, 255))
		draw = ImageDraw.Draw(clock)

		#for clock image

		bg = Image.open("analog_clock.jpg")
		bg = bg.resize((300, 300), Image.ANTIALIAS)
		clock.paste(bg, (50, 50))

		#formula to rotate clock
		'''
		angle_in_radians = angle_in_degrees * math.pi/180
		line_length = 100
		center_x = 250
		center_y = 250
		end_x = center_x + line_length * math.cos(angle_in_radians)
		end_y = center_y - line_length * math.sin(angle_in_radians)
		'''

		origin = 200, 200

		#for hour hand image

		draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill = "black", width = 4)

		#for minute hand image

		draw.line((origin, 200 + 80 * sin(radians(_min)), 200 - 80 * cos(radians(_min))), fill = "blue", width = 3)

		#for second hand image

		draw.line((origin, 200 + 100 * sin(radians(sec)), 200 - 100 * cos(radians(sec))), fill = "red", width = 4)

		draw.ellipse((195, 195, 210, 210), fill = "black")

		clock.save("clock_new.png")

	def working_clock(self):
		h = datetime.now().time().hour
		m = datetime.now().time().minute
		s = datetime.now().time().second
		
		hr = (h/12)*360
		_min = (m/60)*360
		sec = (s/60)*360

		self.clock_image(hr, _min, sec)
		self.img = ImageTk.PhotoImage(file = "clock_new.png")
		self.lbl.config(image = self.img)
		self.lbl.after(200, self.working_clock)

root = Tk()
obj = Clock(root)
root.mainloop()