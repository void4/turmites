from PIL import Image, ImageDraw
from time import time
from random import randint, random, choice, sample
import os
import numpy as np

W = H = 512

space = [[0 for x in range(W)] for y in range(H)]
turmites = []

path = f"{int(time()*1000)}"

os.makedirs(path, exist_ok=True)

class Turmite:
	def __init__(self, p, x, y, o):

		self.rules = []

		for o in range(4):
			self.rules.append([])
			for i in range(256):
				self.rules[-1].append([randint(0,3), randint(0,255)])

		self.x = x
		self.y = y
		self.o = o

	def step(self):

		self.o, out = self.rules[self.o][space[self.y][self.x]]

		space[self.y][self.x] = out

		dx, dy = [(-1,0),(0,1),(1,0),(0,-1)][self.o]

		self.x = (self.x+dx)%W
		self.y = (self.y+dy)%H



for i in range(100):
	turmites.append(Turmite(i/100, randint(0,W-1), randint(0,H-1), randint(0,3)))

for s in range(1000):
	for t in sample(turmites, len(turmites)):
		t.step()

	"""
	img = Image.new("RGB", (W,H))
	for y in range(H):
		for x in range(W):
			v = space[y][x]
			r,g,b = (v,v,v)
			img.putpixel((x,y), (r,g,b))
	"""
	img = Image.fromarray(np.array(space, dtype=np.uint8), "L")

	img.save(f"{path}/{s}.png")
