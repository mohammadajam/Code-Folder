import pygame as pg
import time as t

def main():
	w,h = 1080,760
	dis = pg.display.set_mode((w,h))
	pg.display.set_caption("test")
	font = pg.font.Font(None, 32)
	colour = pg.Color('dodgerblue2')
	active = (255,255,255)
	clock = pg.time.Clock()

	_input = ''
	done = False
	opration = ''
	opration_holder = ''
	on_hold = ''
	eq = False
	clean = True

	num_1 = pg.Rect(200,200,200,120)
	num_2 = pg.Rect(num_1.x+num_1.w,num_1.y,num_1.w,num_1.h)
	num_3 = pg.Rect(num_2.x+num_2.w,num_1.y,num_1.w,num_1.h)
	num_4 = pg.Rect(num_1.x,num_1.y+num_1.h,num_1.w,num_1.h)
	num_5 = pg.Rect(num_2.x,num_2.y+num_2.h,num_1.w,num_1.h)
	num_6 = pg.Rect(num_3.x,num_3.y+num_3.h,num_1.w,num_1.h)
	num_7 = pg.Rect(num_4.x,num_4.y+num_4.h,num_1.w,num_1.h)
	num_8 = pg.Rect(num_5.x,num_5.y+num_5.h,num_1.w,num_1.h)
	num_9 = pg.Rect(num_6.x,num_6.y+num_6.h,num_1.w,num_1.h)
	num_0 = pg.Rect(num_1.x,num_7.y+num_7.h,num_1.w*2,num_1.h)

	num_1_colour = colour
	num_2_colour = colour
	num_3_colour = colour
	num_4_colour = colour
	num_5_colour = colour
	num_6_colour = colour
	num_7_colour = colour
	num_8_colour = colour
	num_9_colour = colour
	num_0_colour = colour
	plus_colour = colour
	minus_colour = colour
	x_colour = colour
	divide_colour = colour
	clear_colour = colour
	backspace_colour = colour
	eq_colour = colour

	main_t = t.time()

	num_1_t = t.time()
	num_2_t = t.time()
	num_3_t = t.time()
	num_4_t = t.time()
	num_5_t = t.time()
	num_6_t = t.time()
	num_7_t = t.time()
	num_8_t = t.time()
	num_9_t = t.time()
	num_0_t = t.time()
	plus_t = t.time()
	minus_t = t.time()
	x_t = t.time()
	divide_t = t.time()
	clear_t = t.time()
	backspace_t = t.time()
	eq_t = t.time()

	_input_rect = pg.Rect(num_1.x,num_1.y-120,num_1.w*3,num_1.h)

	plus_rect = pg.Rect(num_1.x*4,num_1.y,num_1.w,num_1.h)
	minus_rect = pg.Rect(num_1.x*4,num_1.y+num_1.h,num_1.w,num_1.h)
	x_rect = pg.Rect(num_1.x*4,num_1.y+(num_1.h*2),num_1.w,num_1.h)
	divide_rect = pg.Rect(num_1.x*4,num_1.y+(num_1.h*3),num_1.w,num_1.h)
	backspace_rect = pg.Rect(_input_rect.x+_input_rect.w,_input_rect.y,num_1.w,num_1.h)
	clear_rect = pg.Rect(num_0.x+num_0.w,num_0.y,num_1.w,num_1.h)
	eq_rect = pg.Rect(_input_rect.x-num_1.w,_input_rect.y,num_1.w,num_1.h)


	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				done = True
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					done = True
				elif event.key == pg.K_KP1 and clean or event.key == pg.K_1 and clean:
					_input += '1'
					num_1_colour = active
					num_1_t = t.time()
				elif event.key == pg.K_KP2 and clean or event.key == pg.K_2 and clean:
					_input += '2'
					num_2_colour = active
					num_2_t = t.time()
				elif event.key == pg.K_KP3 and clean or event.key == pg.K_3 and clean:
					_input += '3'
					num_3_colour = active
					num_3_t = t.time()
				elif event.key == pg.K_KP4 and clean or event.key == pg.K_4 and clean:
					_input += '4'
					num_4_colour = active
					num_4_t = t.time()
				elif event.key == pg.K_KP5 and clean or event.key == pg.K_5 and clean:
					_input += '5'
					num_5_colour = active
					num_5_t = t.time()
				elif event.key == pg.K_KP6 and clean or event.key == pg.K_6 and clean:
					_input += '6'
					num_6_colour = active
					num_6_t = t.time()
				elif event.key == pg.K_KP7 and clean or event.key == pg.K_7 and clean:
					_input += '7'
					num_7_colour = active
					num_7_t = t.time()
				elif event.key == pg.K_KP8 and clean or event.key == pg.K_8 and clean:
					_input += '8'
					num_8_colour = active
					num_8_t = t.time()
				elif event.key == pg.K_KP9 and clean or event.key == pg.K_9 and clean:
					_input += '9'
					num_9_colour = active
					num_9_t = t.time()
				elif event.key == pg.K_KP0 and clean or event.key == pg.K_0 and clean:
					if not _input == '':
						_input += '0'
					num_0_colour = active
					num_0_t = t.time()
				elif event.key == pg.K_EQUALS and clean:
					eq = True
					eq_colour = active
					eq_t = t.time()
				elif event.key == pg.K_KP_ENTER and clean or event.key == pg.K_RETURN and clean:
					eq = True
					eq_colour = active
					eq_t = t.time()
				elif event.key == pg.K_KP_PLUS and clean:
					opration = '+'
					plus_colour = active
					plus_t = t.time()
				elif event.key == pg.K_KP_MINUS and clean:
					opration = '-'
					minus_colour = active
					minus_t = t.time()
				elif event.key == pg.K_KP_MULTIPLY and clean:
					opration = 'x'
					x_colour = active
					x_t = t.time()
				elif event.key == pg.K_KP_DIVIDE and clean:
					opration = '/'
					divide_colour = active
					divide_t = t.time()
				elif event.key == pg.K_BACKSPACE and clean:
					_input = _input[:-1]
					backspace_colour = active
					backspace_t = t.time()
				elif event.key == pg.K_c or event.key == pg.K_SPACE:
					_input = ''
					on_hold = ''
					opration = ''
					opration_holder = ''
					clean = True
					clear_colour = active
					clear_t = t.time()
			if event.type == pg.MOUSEBUTTONDOWN:
				if num_1.collidepoint(event.pos) and clean:
					_input += '1'
					num_1_colour = active
					num_1_t = t.time()
				if num_2.collidepoint(event.pos) and clean:
					_input += '2'
					num_2_colour = active
					num_2_t = t.time()
				if num_3.collidepoint(event.pos) and clean:
					_input += '3'
					num_3_colour = active
					num_3_t = t.time()
				if num_4.collidepoint(event.pos) and clean:
					_input += '4'
					num_4_colour = active
					num_4_t = t.time()
				if num_5.collidepoint(event.pos) and clean:
					_input += '5'
					num_5_colour = active
					num_5_t = t.time()
				if num_6.collidepoint(event.pos) and clean:
					_input += '6'
					num_6_colour = active
					num_6_t = t.time()
				if num_7.collidepoint(event.pos) and clean:
					_input += '7'
					num_7_colour = active
					num_7_t = t.time()
				if num_8.collidepoint(event.pos) and clean:
					_input += '8'
					num_8_colour = active
					num_8_t = t.time()
				if num_9.collidepoint(event.pos) and clean:
					_input += '9'
					num_9_colour = active
					num_9_t = t.time()
				if num_0.collidepoint(event.pos) and clean:
					if not _input == '':
						_input += '0'
					num_0_colour = active
					num_0_t = t.time()
				if plus_rect.collidepoint(event.pos) and clean:
					opration = '+'
					plus_colour = active
					plus_t = t.time()
				if minus_rect.collidepoint(event.pos) and clean:
					opration = '-'
					minus_colour = active
					minus_t = t.time()
				if x_rect.collidepoint(event.pos) and clean:
					opration = 'x'
					x_colour = active
					x_t = t.time()
				if divide_rect.collidepoint(event.pos) and clean:
					opration = '/'
					divide_colour = active
					divide_t = t.time()
				if eq_rect.collidepoint(event.pos) and clean:
					eq = True
					eq_colour = active
					eq_t = t.time()
				if clear_rect.collidepoint(event.pos):
					_input = ''
					on_hold = ''
					opration = ''
					opration_holder = ''
					clean = True
					clear_colour = active
					clear_t = t.time()
				if backspace_rect.collidepoint(event.pos) and clean:
					_input = _input[:-1]
					backspace_colour = active
					backspace_t = t.time()

		main_t = t.time()
		if main_t - num_1_t > 0.1:
			num_1_colour = colour
		if main_t - num_2_t > 0.1:
			num_2_colour = colour
		if main_t - num_3_t > 0.1:
			num_3_colour = colour
		if main_t - num_4_t > 0.1:
			num_4_colour = colour
		if main_t - num_5_t > 0.1:
			num_5_colour = colour
		if main_t - num_6_t > 0.1:
			num_6_colour = colour
		if main_t - num_7_t > 0.1:
			num_7_colour = colour
		if main_t - num_8_t > 0.1:
			num_8_colour = colour
		if main_t - num_9_t > 0.1:
			num_9_colour = colour
		if main_t - num_0_t > 0.1:
			num_0_colour = colour
		if main_t - plus_t > 0.1:
			plus_colour = colour
		if main_t - minus_t > 0.1:
			minus_colour = colour
		if main_t - x_t > 0.1:
			x_colour = colour
		if main_t - divide_t > 0.1:
			divide_colour = colour
		if main_t - eq_t > 0.1:
			eq_colour = colour
		if main_t - clear_t > 0.1:
			clear_colour = colour
		if main_t - backspace_t > 0.1:
			backspace_colour = colour

		num_1_text = font.render('1', False, colour)
		num_2_text = font.render('2', True, colour)
		num_3_text = font.render('3', True, colour)
		num_4_text = font.render('4', True, colour)
		num_5_text = font.render('5', True, colour)
		num_6_text = font.render('6', True, colour)
		num_7_text = font.render('7', True, colour)
		num_8_text = font.render('8', True, colour)
		num_9_text = font.render('9', True, colour)
		num_0_text = font.render('0', True, colour)

		plus_text = font.render('+', True, colour)
		minus_text = font.render('-', True, colour)
		x_text = font.render('x', True, colour)
		divide_text = font.render('/', True, colour)
		eq_text = font.render('=', True, colour)

		clear_text = font.render('clear', True, colour)
		backspace_text = font.render('backspace', True, colour)

		_input_text = font.render(_input, True, colour)
		
		if opration == '+' or opration == '-' or opration == 'x' or opration == '/':
			if not _input == '':
				if opration_holder == '':				
					on_hold = _input
				elif opration_holder == '+':
					on_hold = str(int(on_hold)+int(_input))
				elif opration_holder == '-':
					on_hold = str(int(on_hold)-int(_input))
				elif opration_holder == 'x':
					on_hold = str(int(on_hold)*int(_input))
				elif opration_holder == '/':
					on_hold = str(int(on_hold)/int(_input))
				opration_holder = opration
				opration = ''
				_input = ''
			else:
				opration = ''

		if eq:
			if on_hold == '':
				_input = _input
				clean, eq = False, False
			else:
				if _input == '':
					eq = False
				else:
					if opration_holder == '+':
						_input = str(int(on_hold)+int(_input))
					elif opration_holder == '-':
						_input = str(int(on_hold)-int(_input))
					elif opration_holder == 'x':
						_input = str(int(on_hold)*int(_input))
					elif opration_holder == '/':
						_input = str(int(on_hold)/int(_input))
					clean, eq = False, False

		length_list = [*_input]
		if len(length_list) > 44:
			_input = _input[:-1]

		dis.fill((30,30,30))
		pg.draw.rect(dis, num_1_colour, num_1,2)
		pg.draw.rect(dis, num_2_colour, num_2,2)
		pg.draw.rect(dis, num_3_colour, num_3,2)
		pg.draw.rect(dis, num_4_colour, num_4,2)
		pg.draw.rect(dis, num_5_colour, num_5,2)
		pg.draw.rect(dis, num_6_colour, num_6,2)
		pg.draw.rect(dis, num_7_colour, num_7,2)
		pg.draw.rect(dis, num_8_colour, num_8,2)
		pg.draw.rect(dis, num_9_colour, num_9,2)
		pg.draw.rect(dis, num_0_colour, num_0,2)
		pg.draw.rect(dis, plus_colour, plus_rect,2)
		pg.draw.rect(dis, minus_colour, minus_rect,2)
		pg.draw.rect(dis, x_colour, x_rect,2)
		pg.draw.rect(dis, divide_colour, divide_rect,2)
		pg.draw.rect(dis, colour, _input_rect,2)
		pg.draw.rect(dis, backspace_colour, backspace_rect,2)
		pg.draw.rect(dis, clear_colour, clear_rect,2)
		pg.draw.rect(dis, eq_colour, eq_rect,2)
		dis.blit(num_1_text, (num_1.x+90,num_1.y+50))
		dis.blit(num_2_text, (num_2.x+90,num_2.y+50))
		dis.blit(num_3_text, (num_3.x+90,num_3.y+50))
		dis.blit(num_4_text, (num_4.x+90,num_4.y+50))
		dis.blit(num_5_text, (num_5.x+90,num_5.y+50))
		dis.blit(num_6_text, (num_6.x+90,num_6.y+50))
		dis.blit(num_7_text, (num_7.x+90,num_7.y+50))
		dis.blit(num_8_text, (num_8.x+90,num_8.y+50))
		dis.blit(num_9_text, (num_9.x+90,num_9.y+50))
		dis.blit(num_0_text, (num_0.x+193,num_0.y+50))
		dis.blit(plus_text, (plus_rect.x+90,plus_rect.y+50))
		dis.blit(minus_text, (minus_rect.x+90,minus_rect.y+50))
		dis.blit(x_text, (x_rect.x+90,x_rect.y+50))
		dis.blit(eq_text, (eq_rect.x+90,eq_rect.y+50))
		dis.blit(divide_text, (divide_rect.x+90,divide_rect.y+50))
		dis.blit(clear_text, (clear_rect.x+65,clear_rect.y+45))
		dis.blit(backspace_text, (backspace_rect.x+45,backspace_rect.y+45))

		dis.blit(_input_text, (_input_rect.x+5,_input_rect.y+5))

		pg.display.update()
		clock.tick(30)

if __name__ == '__main__':
	pg.init()
	main()
	pg.quit()