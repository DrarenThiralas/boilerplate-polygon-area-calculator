class Rectangle:

	def __init__(self, width, height):
		self.width, self.height = width, height
	def set_width(self, width):
		self.width = width
	def set_height(self, height):
		self.height = height

	def get_area(self):
		return self.width * self.height
	def get_perimeter(self):
		return 2*(self.width + self.height)
	def get_diagonal(self):
		return (self.width**2 + self.height**2)**0.5
	def get_picture(self):
		if self.width > 50 or self.height > 50:
			return "Too big for picture."
		else:
			line = "".ljust(self.width, "*")
			toReturn = ""
			for i in range(self.height):
				toReturn += line + "\n"
			return toReturn
	def get_amount_inside(self, rect):
		return int(self.width/rect.width)*int(self.height/rect.height)
	def __str__(self):
		return "Rectangle(width={}, height={})".format(self.width, self.height)





class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)
	def set_side(self, side):
		self.width, self.height = side, side
	def set_width(self, width):
		self.set_side(width)
	def set_height(self, height):
		self.set_side(height)
	def __str__(self):
		return "Square(side={})".format(self.width)
