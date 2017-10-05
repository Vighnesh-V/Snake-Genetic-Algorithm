from NeuralNet import FFNeuralNet
import math
from GASnake import GAInExtensible
from Snake import Snake
import time
#this class is responsible for controlling the evolution of each snake and sending instructions to the matin class - is maintains the population of snakes and passes them to a GA Object
#The GA object accepts this list of snakes and evolves them through the epoch method
#The GA then returns the list of snakes post evolution
#this list can then be used to draw each snake after simulating the snakes movement and drawing its coordinates
class SnakeControllers(object):
    
    def __init__(self):
        self.SNAKE_LIST = []
        self.mq = []
        for i in range(0, 15):
            x = Snake(10,10, 1.2)
            self.SNAKE_LIST.append(x)
            
        input_list_of_lists = []
        for snake in self.SNAKE_LIST:
            a,b = snake.dirvec
            input_list_of_lists.append([snake.PX, snake.PY, a, b])
        
        self.GeneticAlgorithm = GAInExtensible(self.SNAKE_LIST, 0.2, 0.7, input_list_of_lists )
        i = 0
        while ( i < 10):
            print('epoch' + str(i))
            self.GeneticAlgorithm.Epoch()
            
            print ('epoch' + str(i) + ' generation' +  str(self.GeneticAlgorithm.GENERATION) + ' done')
            i+=1
            print 'Max Fitness is' + str(self.GeneticAlgorithm.findMaxSnake())
        
        self.SNAKE_LIST = self.GeneticAlgorithm.SNAKE_LIST
    
    def show_snake1(self):
        tf = open('tst.txt', 'w')
        move_queue = []
        s = self.SNAKE_LIST[0]
        instructions = s.instruction_list
        print instructions
        direction = 'UP'
        for i in range(0,4):
            if (i == 0):
                direction = 'UP'
            elif(i == 1):
                direction = 'LEFT'
            elif(i == 2):
                direction = 'DOWN'
            elif(i == 3):
                direction = 'RIGHT'
            time_del = instructions[i]
            
            t0 = time.clock()
            wer = time.clock()- t0
            while(time.clock() - t0 <= time_del / 100):
                print 'this is the time difference' + str(wer)
                if(direction == 'UP'):
                    s.XSPEED = 0
                    s.YSPEED = 1
                    s.PY -= s.YSPEED
                    if (s.PY < 0):
                        s.PY = 200 
                elif(direction == 'DOWN'):
                    s.XSPEED = 0
                    s.YSPEED = 1
                    s.PY += s.YSPEED
                    if (s.PY > 200):
                        s.PY = 0
                elif(direction == 'LEFT'):
                    s.XSPEED = 1
                    s.YSPEED = 0
                    s.PX -= s.XSPEED
                    if(s.PX < 0):
                        s.PX = 200
                elif(direction == 'RIGHT'):
                    s.XPSEED = 1
                    s.YSPEED = 0
                    s.PX += s.XSPEED
                    if(s.PX > 200):
                        s.PX = 0
                
                a = (s.PX, s.PY)
                z = '(' + str(s.PX) + ',' + str(s.PY) + ',' + direction + ' )' + '\n'
                tf.write(z)
                move_queue.append(a)
        self.mq = move_queue
        tf.close()
        
                
                
                
    def show(self):
        
        if(len(self.mq) > 0):
            a,b = self.mq.pop(0)
            fill(0, 40, 255)
            rect(a, b, 20,20)
            
        
            
            
        
                
        
        
        
    
                
                        

x = SnakeControllers()
x.show_snake1()
print('here')
def setup():
    size(200,200)
    noStroke()
    
def draw():
    background(0)
    fill(255,0,0)
    rect(10,10,10,10)
#tgt already printed
    x.show()
    
    