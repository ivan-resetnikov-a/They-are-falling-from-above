import pygame as pg
from .constants import LOCATION, TILE_SIZE


class Tile :
	def __init__ (self, pos) :
		self.img = pg.image.load('assets/block.png').convert()
		self.bg = self.img.copy()
		self.bg.set_alpha(128)
		self.pos = pos
		self.size = (32, 32)

	def render (self, frame, cam) :
		frame.blit(self.bg, (self.pos[0] - cam.pos[0] + 3, self.pos[1] - cam.pos[1] + 3))
		frame.blit(self.img, ( self.pos[0] - cam.pos[0], self.pos[1] - cam.pos[1]))


def loadLevel () :
	tiles = []
	targetPos = []

	for y, line in enumerate(LOCATION) :
		for x, char in enumerate(line) :
			if char != ' ' and char != '.' :
				tiles.append(Tile((x * TILE_SIZE, y * TILE_SIZE),))
			elif char == '.' :
				targetPos.append([x * TILE_SIZE, y * TILE_SIZE],)

	return tiles, targetPos