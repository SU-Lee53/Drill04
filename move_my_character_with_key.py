from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def idle():
	global frame, base, size, x, y
	clear_canvas()
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	if frame < 4:
		character.clip_draw(1 + frame * 26, 500, 26, 25, x, y, size, size)
	elif frame >= 4 and frame < 8:
		character.clip_draw(frame * 28 - 1, 500, 26, 25, x, y, size, size)
	elif frame == 8:
		character.clip_draw(frame * 28 - 5, 500, 28, 25, x, y, size, size)
	elif frame > 8 and frame < 12:
		character.clip_draw(frame * 28 - 10, 500, 28, 25, x, y, size, size)
	else:
		character.clip_draw(frame * 28 - 8, 500, 28, 25, x, y, size, size)
	update_canvas()
	handle_events()
	frame = (frame + 1) % 16
	delay(0.08)

def left():
	global frame, base, size, x, y
	clear_canvas()
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	character.clip_composite_draw(base + frame * 30, 675, 28, 28, 0, 'h', x, y, size, size)
	update_canvas()
	handle_events()
	frame = (frame + 1) % 8
	if x > 70:
		x += xdir * 20
	delay(0.03)

def right():
	global frame, base, size, x, y
	clear_canvas()
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	character.clip_draw(base + frame * 30, 675, 28, 25, x, y, size, size)
	update_canvas()
	handle_events()
	frame = (frame + 1) % 8
	if x < 1210:
		x += xdir * 20
	delay(0.03)

def up():
	global frame, base, size, x, y
	clear_canvas()
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	if frame < 6:
		character.clip_composite_draw(frame * 24, 465, 28, 28, 0, 'h', x, y, size, size)
	else:
		character.clip_composite_draw(frame * 24 + 1, 465, 28, 28, 0, 'h', x, y, size, size)
	update_canvas()
	handle_events()
	frame = (frame + 1) % 10
	if y < 960:
		y += ydir * 20
	delay(0.03)

def down():
	global frame, base, size, x, y
	clear_canvas()
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	character.clip_composite_draw(frame * 29 + 250, 465, 28, 28, 0, 'h', x, y, size, size)
	update_canvas()
	handle_events()
	frame = (frame + 1) % 4
	if y > 70:
		y += ydir * 20
	delay(0.03)

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
size = 120
xdir, ydir = 0, 0

while running:
	if xdir < 0:
		left()
	elif xdir > 0:
		right()
	elif ydir > 0:
		up()
	elif ydir < 0:
		down()
	else:
		idle()









