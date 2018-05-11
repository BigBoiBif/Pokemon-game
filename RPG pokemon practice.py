'''import pygame

pygame.init()

display_width=800
display_height=600

gameDisplay=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('doggy dog world')

black=(0, 0, 0)
white=(255, 255, 255,)

clock=pygame.time.Clock()
crashed=False
player=pygame.image.load('ProfilePic.jpg')

def playerLocation(x, y):
	gameDisplay.blit(player, (x, y))

x=(display_height*.5)
y=(display_width*.5)

while not crashed:
	for event in pygame.event.get():
		move_ticker=0
		keys=pygame.key.get_pressed()
		if keys[K_LEFT]:
			if move_ticker==0:
				move_ticker=10
				location-=1
				if location == -1:
					location=0
		if keys[K_RIGHT]:
			if move_ticker==0:
				move_ticker=10
				location+=1
				if location>display_width:
					location=display_width
		if event==pygame.QUIT:
			crashed=True
	gameDisplay.fill(white)
	playerLocation(x, y)

	pygame.display.update()
	clock.tick(60)
	if move_ticker>0:
		move_ticker-=1

pygame.quit()
quit()'''
