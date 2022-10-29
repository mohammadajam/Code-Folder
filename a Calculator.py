import pygame as pg


def main():
	w,h = 1080,760
	dis = pg.display.set_mode((w,h))
	pg.display.set_caption("test")
	font = pg.font.Font(None, 32)
	colour = pg.Color('lightskyblue3')
	clock = pg.time.Clock()

	_input = ''
	loop = False
	opration = ''
	opration_hold = ''
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

	_input_rect = pg.Rect(num_1.x,num_1.y-120,num_1.w*3,num_1.h)

	plus_rect = pg.Rect(num_1.x*4,num_1.y,num_1.w,num_1.h)
	minus_rect = pg.Rect(num_1.x*4,num_1.y+num_1.h,num_1.w,num_1.h)
	x_rect = pg.Rect(num_1.x*4,num_1.y+(num_1.h*2),num_1.w,num_1.h)
	divide_rect = pg.Rect(num_1.x*4,num_1.y+(num_1.h*3),num_1.w,num_1.h)
	backspace_rect = pg.Rect(_input_rect.x+_input_rect.w,_input_rect.y,num_1.w,num_1.h)
	clear_rect = pg.Rect(num_0.x+num_0.w,num_0.y,num_1.w,num_1.h)
	eq_rect = pg.Rect(_input_rect.x-num_1.w,_input_rect.y,num_1.w,num_1.h)


	while not loop:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				loop = True
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					loop = True
			if event.type == pg.MOUSEBUTTONDOWN:
				if num_1.collidepoint(event.pos) and clean:
					_input += '1'
				if num_2.collidepoint(event.pos) and clean:
					_input += '2'
				if num_3.collidepoint(event.pos) and clean:
					_input += '3'
				if num_4.collidepoint(event.pos) and clean:
					_input += '4'
				if num_5.collidepoint(event.pos) and clean:
					_input += '5'
				if num_6.collidepoint(event.pos) and clean:
					_input += '6'
				if num_7.collidepoint(event.pos) and clean:
					_input += '7'
				if num_8.collidepoint(event.pos) and clean:
					_input += '8'
				if num_9.collidepoint(event.pos) and clean:
					_input += '9'
				if num_0.collidepoint(event.pos) and clean:
					_input += '0'
				if plus_rect.collidepoint(event.pos) and clean:
					opration = '+'
				if minus_rect.collidepoint(event.pos) and clean:
					opration = '-'
				if x_rect.collidepoint(event.pos) and clean:
					opration = 'x'
				if divide_rect.collidepoint(event.pos) and clean:
					opration = '/'
				if eq_rect.collidepoint(event.pos) and clean:
					eq = True
				if clear_rect.collidepoint(event.pos):
					_input = ''
					on_hold = ''
					opration = ''
					opration_hold = ''
					clean = True
				if backspace_rect.collidepoint(event.pos) and clean:
					_input = _input[:-1]

		num_1_text = font.render('1', True, colour)
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
				if opration_hold == '':				
					on_hold = _input
				elif opration_hold == '+':
					on_hold = str(int(on_hold)+int(_input))
				elif opration_hold == '-':
					on_hold = str(int(on_hold)-int(_input))
				elif opration_hold == 'x':
					on_hold = str(int(on_hold)*int(_input))
				elif opration_hold == '/':
					on_hold = str(int(on_hold)/int(_input))
				opration_hold = opration
				opration = ''
				_input = ''
			else:
				opration = ''

		if eq:
			if on_hold == '':
				_input = _input
				clean = False
			else:
				if opration_hold == '+':
					_input = str(int(on_hold)+int(_input))
				elif opration_hold == '-':
					_input = str(int(on_hold)-int(_input))
				elif opration_hold == 'x':
					_input = str(int(on_hold)*int(_input))
				elif opration_hold == '/':
					_input = str(int(on_hold)/int(_input))
				clean, eq = False, False

		length_list = [*_input]
		if len(length_list) > 44:
			_input = _input[:-1]

		dis.fill((30,30,30))
		pg.draw.rect(dis, colour, num_1,2)
		pg.draw.rect(dis, colour, num_2,2)
		pg.draw.rect(dis, colour, num_3,2)
		pg.draw.rect(dis, colour, num_4,2)
		pg.draw.rect(dis, colour, num_5,2)
		pg.draw.rect(dis, colour, num_6,2)
		pg.draw.rect(dis, colour, num_7,2)
		pg.draw.rect(dis, colour, num_8,2)
		pg.draw.rect(dis, colour, num_9,2)
		pg.draw.rect(dis, colour, num_0,2)
		pg.draw.rect(dis, colour, plus_rect,2)
		pg.draw.rect(dis, colour, minus_rect,2)
		pg.draw.rect(dis, colour, x_rect,2)
		pg.draw.rect(dis, colour, divide_rect,2)
		pg.draw.rect(dis, colour, _input_rect,2)
		pg.draw.rect(dis, colour, backspace_rect,2)
		pg.draw.rect(dis, colour, clear_rect,2)
		pg.draw.rect(dis, colour, eq_rect,2)
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