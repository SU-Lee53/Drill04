from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet2.png')

def left():
	global frame, base
	clear_canvas()
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	character.clip_draw(base+frame*30, 675, 28, 25, x, y, 130, 130)
	update_canvas()
	handle_events()
	frame = (frame+1) % 8

def right():
	global frame
	clear_canvas()
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	character.clip_composite_draw(base + frame * 30, 675, 28, 28, 0, 'h', x, y, 130, 130)
	update_canvas()
	handle_events()
	frame = (frame + 1) % 8

def handle_events():
	global running, xdir, ydir
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_UP:
				pass
			elif event.key == SDLK_DOWN:
				pass
			elif event.key == SDLK_RIGHT:
				pass
			elif event.key == SDLK_LEFT:
				pass
		elif event.key == SDL_KEYUP:
			if event.key == SDLK_UP:
				pass
			elif event.key == SDLK_DOWN:
				pass
			elif event.key == SDLK_RIGHT:
				pass
			elif event.key == SDLK_LEFT:
				pass

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0
base = 4
xdir = ydir = 0

while running:
	# left()
	right()
	x += xdir * 5
	y += ydir * 5
	delay(0.1)









