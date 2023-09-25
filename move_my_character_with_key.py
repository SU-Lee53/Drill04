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
				ydir += 1
			elif event.key == SDLK_DOWN:
				ydir -= 1
			elif event.key == SDLK_RIGHT:
				xdir += 1
			elif event.key == SDLK_LEFT:
				xdir -= 1
			elif event.key == SDLK_ESCAPE:
				running = False
		elif event.type == SDL_KEYUP:
			if event.key == SDLK_UP:
				ydir -= 1
			elif event.key == SDLK_DOWN:
				ydir += 1
			elif event.key == SDLK_RIGHT:
				xdir -= 1
			elif event.key == SDLK_LEFT:
				xdir += 1

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0
base = 4
xdir = ydir = 0

while running:
	clear_canvas()
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	if frame < 4:
		character.clip_draw(1 + frame * 26, 500, 26, 25, x, y, 130, 130)
	elif frame >= 4 and frame < 8:
		character.clip_draw(frame * 28 - 1, 500, 26, 25, x, y, 130, 130)
	elif frame == 8:
		character.clip_draw(frame * 28 - 5, 500, 28, 25, x, y, 130, 130)
	elif frame > 8 and frame < 12:
		character.clip_draw(frame * 28 - 10, 500, 28, 25, x, y, 130, 130)
	else:
		character.clip_draw(frame * 28 - 8, 500, 28, 25, x, y, 130, 130)
	update_canvas()
	handle_events()
	frame = (frame + 1) % 16
	x += xdir * 20
	y += ydir * 20
	delay(0.1)









