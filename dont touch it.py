import pygame as pg
from random import randint
import time

def main():
	global done
	w,h = 720,480
	dis = pg.display.set_mode((w,h))
	pg.display.set_caption("test")
	clock = pg.time.Clock()

	done = False

	main_t = time.time()
	speed_t = time.time()
	thickness_t = time.time()
	start = time.time()

	class Ball:
		def __init__(self):
			self.thickness = 10
			self.ball_x = randint(40,680)
			self.ball_y = randint(40,440)
			self.x_direction = randint(0,9)
			self.y_direction = randint(0,9)
			self.speed = [-15,-12,-9,-5,-3,3,5,9,12,15]
			self.ball_x_speed = self.speed[self.x_direction]
			self.ball_y_speed = self.speed[self.y_direction]
		def draw(self):
			pg.draw.circle(dis, (255,0,0), (self.ball_x,self.ball_y), self.thickness)
			
			self.ball_x += self.ball_x_speed
			self.ball_y += self.ball_y_speed
		
		def change_direction(self):
			if self.ball_x - self.thickness < 0 or self.ball_x + self.thickness > w:
				self.ball_x_speed *= -1
			if self.ball_y - self.thickness < 0 or self.ball_y + self.thickness > h:
				self.ball_y_speed *= -1

		def touch(self):
			self.pos = pg.mouse.get_pos()
			if self.pos[0] > self.ball_x-self.thickness and self.pos[0] < self.ball_x+self.thickness:
				if self.pos[1] > self.ball_y-self.thickness and self.pos[1] < self.ball_y+self.thickness:
					
					return True

		def harder(self):
			self.x_direction = randint(0,9)
			self.y_direction = randint(0,9)
			self.ball_x_speed = self.speed[self.x_direction]
			self.ball_y_speed = self.speed[self.y_direction]
			self.ball_x_speed *= 2
			self.ball_y_speed *= 1.2

		def thick(self):
			self.thickness += 1

	ball = Ball()
	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				done = True
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					done = True

		main_t = time.time()

		if main_t - speed_t > 1:
			ball.harder()
			speed_t = time.time()
		if main_t - thickness_t > 15:
			ball.thick()
			thickness_t = time.time()

		dis.fill((255,255,255))

		ball.draw()
		ball.change_direction()  
		ball.touch()
		if ball.touch():
			print('you died')
			print(f'you survived for {round(main_t-start,2)} seconds')
			done = True

				

		pg.display.update()
		time.sleep(1/120)
		clock.tick(120)

if __name__ == '__main__':
	pg.init()
	main()
	pg.quit()