#imports used throughout the script, don't forget these
import pygame
import random
import math

#initiates pygame, very importante
pygame.init()

#sets up colors in RGB format
Black = (0, 0, 0)
White = (255, 255, 255,)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
Purple = (255, 0, 255)

#sets a list of colors
palette = [Yellow, Red, Green, Blue, White, Black]

rep = 0

#sets up a font, cailibri is typeface, 25 is point size, True is bold, False is italics
font = pygame.font.SysFont('Calibri', 25, True, False)
#establishes window
Width = 800
Height = 600
size = (Width, Height)
game_display = pygame.display.set_mode(size)
pygame.display.set_caption('test')

#says the game isn't closed, main loop only goes while this is false
closed=False
#sets a clock to be used to set a framerate
clock=pygame.time.Clock()

pygame.mouse.set_visible(False)

x_vel=0
y_vel=0
x = -50
y = -50
curent_canvas = []
rep = 0
while not closed:
	#main event loop
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			closed=True

		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_a:
				x_vel=-3
			elif event.key==pygame.K_d:
				x_vel=3
			elif event.key==pygame.K_w:
				y_vel=-3
			elif event.key==pygame.K_s:
				y_vel=3
		elif event.type==pygame.KEYUP:
			if event.key==pygame.K_a or event.key==pygame.K_d:
				x_vel=0
			elif event.key==pygame.K_w or event.key==pygame.K_s:
				y_vel=0

	#game logic here
	def text_box(x, y, l, w):
		b = pygame.Surface((l, w))
		b.set_alpha(128)
		b.fill(White)
		game_display.blit(b, (x, y))
	def text(stri, x, y, color):
		text = font.render(stri, False, color)
		#text_rect = text.get_rect(center = (x, y))
		game_display.blit(text, (x, y))
	#drawing code here

	game_display.fill(White)
	#clears the game_display

	x-=x_vel
	y-=y_vel
	if x >= 390:
		x = 390
	elif x <=-490:
		x = -490
	if y >= 290:
		y = 290
	elif y <= -390:
		y = -390
	if rep==0:
		for i in range(x, x+900, 50):
			for j in range (y, y+700, 50):
				color_used = random.choice(palette)
				#game_display is what it's being drawn to, color_used is the color, i and j are where it starts being drawn, and 50 and 50 are side length
				pygame.draw.rect(game_display, color_used, [i, j, 50, 50])
				curent_canvas.append(color_used)
		rep = 1
	else:
		counter=0
		for i in range(x, x+900, 50):
			for j in range(y, y+700, 50):
				pygame.draw.rect(game_display, curent_canvas[counter], [i, j, 50, 50])
				counter+=1

	pygame.draw.rect(game_display, Purple, [390, 290, 20, 20])
	text = font.render('nam jef', False, [0, 0, 0])
	text_rect = text.get_rect(center = (Width/2, (Height/2)-30))
	#this actually updates the game_display, is kinda important
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
quit()