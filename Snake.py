import random
import math
import time
from NeuralNet import FFNeuralNet
class Snake(object):
    def __init__(self, xtgt, ytgt, scale_factor):
        self.PX = random.uniform(0,200)
        self.PY = random.uniform(0,200)
        self.direction = 'RIGHT'
        self.xspeed = 1;
        self.yspeed = 0;
        self.brain = FFNeuralNet(4,4,2,4)
        self.XG = xtgt
        self.YG = ytgt
        self.dirvec = self.calc_nvector_to_tgt()
        a,b = self.dirvec
        self.instruction_list = self.brain.feed_forward([self.PX, self.PY, a, b])
        self.SCALE_FACTOR = scale_factor
        self.fitness = -1
        
    def calc_nvector_to_tgt(self):
        magnitude = math.sqrt((self.PX - self.XG) ** 2 + (self.PY - self.YG) ** 2)
        xcomp = (self.XG - self.PX) / magnitude
        ycomp = (self.YG - self.PY) / magnitude
        return (xcomp, ycomp)
    
    
        
        