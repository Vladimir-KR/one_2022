import pygame
from pygame import *
from pygame.draw import *
import random 

size_x = 1000
size_y = 600
screen = display.set_mode((size_x, size_y))
display.set_caption('AERO-Football')
init()


GREEN = (0, 155, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)


Surface.fill(screen, GREEN)
def lines():
	global width, length, thickness, x, y
	width = 400
	length = 800
	thickness = 2
	x = width/4
	y = length/8
 #basic markup
	rect(screen, WHITE, (x, y, length, width), thickness)
	line(screen, WHITE, [(x*2+length)/2, y], [(x*2+length)/2, y+width], thickness)
	circle(screen, WHITE, (x+(length/2), y+(width/2)), length/12, thickness)
	circle(screen, WHITE, (x+(length/2)+(thickness/2), y+(width/2)), thickness)
 #left gates
	rect(screen, WHITE, (x, y+(width/5), length/7.5, width/1.6), thickness)
	rect(screen, WHITE, (x, y+(width/3), length/24, width/3), thickness)
	circle(screen, WHITE, (x+(length/11), y+(width/2)), thickness, thickness)
	rect(screen, WHITE, ((x-width/40) , y+((width/2.4)), width/40, width/6), thickness)
 #right gates
	rect(screen, WHITE, (x+length-(length/7.5), y+(width/5), length/7.5, width/1.6), thickness)
	rect(screen, WHITE, (x+length-(length/24), y+(width/3), length/24, width/3), thickness)
	circle(screen, WHITE, (x+length-(length/11), y+(width/2)), thickness, thickness)
	rect(screen, WHITE, (x+length, y+((width/2.4)), width/40, width/6), thickness)


lines()

a = x+(length/2)
b = y+(width/2)

def ball(a, b):
	circle(screen, ORANGE, (a, b), width/60)





gk_left_x = x+(length/48)
gk_left_y = y+(width/2)

gk_right_x = x+length-(length/48)
gk_right_y = y+(width/2)


position_left_gk = gk_left_y+gk_left_x
position_right_gk = gk_right_y+gk_right_x



#print('position_left_gk', position_left_gk)
#print('position_right_gk', position_right_gk)
#print('position_ball', position_ball)


#print('gk_right', gk_right_y, gk_right_x)
#print('gk_left', gk_left_y, gk_left_x)

def touch_gk_and_ball_left():
	global position_left_gk, position_ball, va, vb
	
	if abs(position_left_gk-position_ball) <= width/60:
		va *= 1
		for i in range(1):
			print('touch_left')


def touch_gk_and_ball_right():
	global position_right_gk, position_ball, va, vb
	
	if abs(position_right_gk-position_ball) <= width/60:
		vb *= 1
		for i in range(1):
			print('touch_right')


def goalkeepers():
	circle(screen, BLACK, (gk_left_x, gk_left_y), width/30)
	circle(screen, BLACK, (gk_right_x, gk_right_y), width/30)

# problem of touch goalkeepers and ball

goalkeepers()

gk_speed = 10

def gk_left_stop():
	global size_x, gk_left_x, gk_left_y
	# right, left
	if gk_left_x >= size_x:
		gk_left_x = size_x-(width/60)
	elif gk_left_x <= 0:
		gk_left_x = 0+(width/60)
		
	#up, down
	if gk_left_y >= size_y:
		gk_left_y = size_y-(width/60)
	elif gk_left_y <= 0:
		gk_left_y = 0+(width/60)
def gk_right_stop():
	global size_x, gk_right_x, gk_right_y
	# right, left
	if gk_right_x >= size_x:
		gk_right_x = size_x-(width/60)	
	elif gk_right_x <= 0:
		gk_right_x = 0+(width/60)
		
	#up, down
	if gk_right_y >= size_y:
		gk_right_y = size_y-(width/60)
	elif gk_right_y <= 0:
		gk_right_y = 0+(width/60)

display.flip()

def motion_goalkeeper_left():
	global gk_left_x, gk_left_y, gk_speed
	if pygame.key.get_pressed()[K_w]:
		gk_left_y -= gk_speed
		gk_left_stop()
		if pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_d]:
			gk_left_y -= gk_speed/2
			gk_left_x += gk_speed/2
		if pygame.key.get_pressed()[K_w] and pygame.key.get_pressed()[K_a]:
			gk_left_y -= gk_speed/2
			gk_left_x -= gk_speed/2
		
	if pygame.key.get_pressed()[K_s]:
		gk_left_y += gk_speed
		gk_left_stop()
		if pygame.key.get_pressed()[K_s] and pygame.key.get_pressed()[K_a]:
			gk_left_x -= gk_speed/2
			gk_left_y += gk_speed/2
		if pygame.key.get_pressed()[K_s] and pygame.key.get_pressed()[K_d]:
			gk_left_y += gk_speed/2
			gk_left_x += gk_speed/2
		
	if pygame.key.get_pressed()[K_d]:
		gk_left_x += gk_speed
		gk_left_stop()
		if pygame.key.get_pressed()[K_d] and pygame.key.get_pressed()[K_s]:
			gk_left_y += gk_speed/2
			gk_left_x += gk_speed/2
		if pygame.key.get_pressed()[K_d] and pygame.key.get_pressed()[K_w]:
			gk_left_y -= gk_speed/2
			gk_left_x += gk_speed/2

	if pygame.key.get_pressed()[K_a]:
		gk_left_x -= gk_speed
		gk_left_stop()
		if pygame.key.get_pressed()[K_a] and pygame.key.get_pressed()[K_w]:
			gk_left_y -= gk_speed/2
			gk_left_x -= gk_speed/2
		if pygame.key.get_pressed()[K_a] and pygame.key.get_pressed()[K_s]:
			gk_left_x -= gk_speed/2
			gk_left_y += gk_speed/2

def motion_goalkeeper_right():
	global gk_right_x, gk_right_y, gk_speed
	if pygame.key.get_pressed()[K_KP8]:
		gk_right_y -= gk_speed
		gk_right_stop()
		if pygame.key.get_pressed()[K_KP8] and pygame.key.get_pressed()[K_KP6]:
			gk_right_y -= gk_speed/2
			gk_right_x += gk_speed/2
		if pygame.key.get_pressed()[K_KP8] and pygame.key.get_pressed()[K_KP4]:
			gk_right_y -= gk_speed/2
			gk_right_x -= gk_speed/2
		
	if pygame.key.get_pressed()[K_KP5]:
		gk_right_y += gk_speed
		gk_right_stop()
		if pygame.key.get_pressed()[K_KP5] and pygame.key.get_pressed()[K_KP4]:
			gk_right_x -= gk_speed/2
			gk_right_y += gk_speed/2
		if pygame.key.get_pressed()[K_KP5] and pygame.key.get_pressed()[K_KP6]:
			gk_right_y += gk_speed/2
			gk_right_x += gk_speed/2
		
	if pygame.key.get_pressed()[K_KP6]:
		gk_right_x += gk_speed
		gk_right_stop()
		if pygame.key.get_pressed()[K_KP6] and pygame.key.get_pressed()[K_KP5]:
			gk_right_y += gk_speed/2
			gk_right_x += gk_speed/2
		if pygame.key.get_pressed()[K_KP6] and pygame.key.get_pressed()[K_KP8]:
			gk_right_y -= gk_speed/2
			gk_right_x += gk_speed/2

	if pygame.key.get_pressed()[K_KP4]:
		gk_right_x -= gk_speed
		gk_right_stop()
		if pygame.key.get_pressed()[K_KP4] and pygame.key.get_pressed()[K_KP8]:
			gk_right_y -= gk_speed/2
			gk_right_x -= gk_speed/2
		if pygame.key.get_pressed()[K_KP4] and pygame.key.get_pressed()[K_KP5]:
			gk_right_x -= gk_speed/2
			gk_right_y += gk_speed/2


clock = time.Clock()
FPS = 30
finished = False

va = 1
vb = 1


while not finished:
	clock.tick(FPS)
	Surface.fill(screen, GREEN)
	
	lines()
	goalkeepers()	
	ball(a, b)


	display.flip()
	
	a += va
	b += vb
	position_ball = a+b
	#print(position_ball)
	#print(position_left_gk)
	#print(position_right_gk)

	if a >= x+length-width/60 or a <= x+width/60:
		for i in range(1):
			print('v_left', va, vb)
			va *= -1
			print('pisition_left')
		
	touch_gk_and_ball_left()
	
	
	if b >= y+width-width/60 or b <= y+width/60:
		for i in range(1):
			print('v_right', va, vb)
			vb *= -1
			print('pisition_right')

	touch_gk_and_ball_right()



	#touch_gk_and_ball()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		elif event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				finished = True

		motion_goalkeeper_left()
		motion_goalkeeper_right()			
	

quit()
