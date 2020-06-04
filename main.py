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

count = 0
try:
	for s in range(1000):
		for t in sample(turmites, len(turmites)):
			t.step()

		if s % 4 != 0:
			continue

		img = Image.fromarray(np.array(space, dtype=np.uint8), "L")

		img.save(f"{path}/{count}.png")
		count += 1
except KeyboardInterrupt:
	pass

os.system(f"convert -delay 10 -loop 0 $(ls -1 {path}/*.png | sort -V) {path}.gif")
