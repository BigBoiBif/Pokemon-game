#imports used throughout the script, don't forget these
import pygame
from random import *
import math

#initiates pygame, very importante
pygame.init()

#sets up colors in RGB format
Black=(0, 0, 0)
White=(255, 255, 255,)
Green=(0, 255, 0)
Blue=(0, 0, 255)
Red=(255, 0, 0)
Yellow=(255, 255, 0)

#sets a list of colors
palette=[Yellow, Red, Green, Blue, White, Black]

#sets up a font, cailibri is typeface, 25 is point size, True is bold, False is italics
font=pygame.font.SysFont('Calibri', 25, True, False)

#establishes window
size=(800, 600)
game_display=pygame.display.set_mode(size)
pygame.display.set_caption('test')

#says the game isn't closed, main loop only goes while this is false
closed=False
#sets a clock to be used to set a framerate
clock=pygame.time.Clock()

pygame.mouse.set_visible(False)

rect_x=1
rect_y=1
rect_ix=3
rect_iy=3
snow=[]
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

	#drawing code here

	game_display.fill(White)
	#clears the game_display
	def draw_stick_figure(game_display, x, y):
		# Head
		pygame.draw.ellipse(game_display, Black, [1+x,y,10,10], 0)
	    # Legs
		pygame.draw.line(game_display, Black ,[5+x,17+y], [10+x,27+y], 2)
		pygame.draw.line(game_display, Black, [5+x,17+y], [x,27+y], 2)
		# Body
		pygame.draw.line(game_display, Red, [5+x,17+y], [5+x,7+y], 2)
		# Arms
		pygame.draw.line(game_display, Red, [5+x,7+y], [9+x,17+y], 2)
		pygame.draw.line(game_display, Red, [5+x,7+y], [1+x,17+y], 2)
	def mouse_cursor():
		pos=pygame.mouse.get_pos()
		x=pos[0]
		y=pos[1]
		draw_stick_figure(game_display, x, y)

	def keyboard_velocity_test(x_coord, y_coord):
		#this doesn't work as an individual function because of the way the loop is executed
		x_vel=0
		y_vel=0

		x_coord=10
		y_coord=10		

		x_coord+=x_vel
		y_coord+=y_vel
		draw_stick_figure(game_display, x_coord, y_coord)

	def snowflakes():
		x=randint(0,800)
		y=randint(0,600)
		snow.append([x, y])
		#i is item in list, going through every list item
		for i in range(len(snow)):
			#game_display is the display being drawn to. White is color, x and y are coordinates, 2 is size
			pygame.draw.circle(game_display, White, snow[i], 2)
			#snow[i] is the item in the list at position [i]
			snow[i][1]+=1
			if snow[i][1]>598:
				#redraws snow elsewhere if it goes offgame_display
				x=randint(0,800)
				y=randint(-50, -10)
				snow[i][0]=x
				snow[i][1]=y
	def bouncing_box():
		pygame.draw.rect(game_display, Green, [x, y, 50, 50])
		#game_display is what display it is set to. Green is color, and x and y are where it starts being drawn. 50 and 50 are parameters for side length
		if x>=750 or x<=0:
			ix*=-1
		if y>=550 or y<=0:
			iy*=-1
		x+=ix
		y+=iy
	keyboard_velocity_test()
	#this actually updates the game_display, is kinda important
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
quit()