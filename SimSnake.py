import math
import time
class SimSnake(object):
    
    def __init__(self):
        self.INSTRUCTIONS = []
        self.PX = 0
        self.PY = 0
        self.TGTX = 0
        self.TGTY = 0
        self.XSPEED = 1
        self.YSPEED = 0
        self.SCALE_FACTOR = 1.2
		
    def init_snake(self, instruction_list, posx,posy, tgtx,tgty, scale_factor):
        self.INSTRUCTIONS = instruction_list
        self.PX = posx
        self.PY = posy
        self.TGTX = tgtx
        self.TGTY = tgty
        self.XSPEED = 1
        self.YSPEED = 0

        self.SCALE_FACTOR = scale_factor


    def calcFitness(self):
        a = math.sqrt((math.fabs(self.PX - self.TGTX) ** 2) + (math.fabs(self.PY - self.TGTY) ** 2))
        if(a == 0):
            return 1
        else:
            return 1/a
	
    def update_snake(self, time_del, direction):
        t0 = time.clock()
        while(time.clock() - t0 <= time_del/100):
            if(direction == 'UP'):
                self.XSPEED = 0
                self.YSPEED = 1
                self.PY -= self.YSPEED
                if (self.PY < 0):
                    self.PY = 200 
            elif(direction == 'DOWN'):
                self.XSPEED = 0
                self.YSPEED = 1
                self.PY += self.YSPEED
                if (self.PY > 200):
                    self.PY = 0 
            elif(direction == 'LEFT'):
                self.XSPEED = 1
                self.YSPEED = 0
                self.PX -= self.XSPEED
                if(self.PX < 0):
                    self.PX = 200
            elif(direction == 'RIGHT'):
                self.XPSEED = 1
                self.YSPEED = 0
                self.PX += self.XSPEED
                if(self.PX > 200):
                    self.PX = 0

    def sim_snake(self):
        sclstructions = []
        for instruction in self.INSTRUCTIONS:
            sclstructions.append(instruction*self.SCALE_FACTOR)

        self.update_snake(sclstructions[0], 'UP')
        self.update_snake(sclstructions[1], 'LEFT')
        self.update_snake(sclstructions[2], 'DOWN')
        self.update_snake(sclstructions[3], 'RIGHT')

        return self.calcFitness()

		
