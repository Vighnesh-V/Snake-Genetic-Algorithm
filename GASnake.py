from SimSnake import SimSnake
import random
import math
from Snake import Snake
class GAInExtensible(object):
    
    def __init__(self, population, mutation_rate, crossover_rate, input_list_list):
    	self.POP_SIZE = len(population)
    	self.MUTATION_RATE = mutation_rate
    	self.CROSSOVER_RATE = crossover_rate
    	self.SNAKE_LIST = population
    	self.SIM_SNAKE = SimSnake()
    	self.LIST_OF_INPUT_LISTS = input_list_list
    	self.FITNESS_LIST = []
    	self.TOTAL_FITNESS = 0
    	self.GENERATION = 0
    
    def findMaxSnake(self):
        max = -2
        for snake in self.SNAKE_LIST:
            if(snake.fitness > max):
                max = snake.fitness
        
        return max
    
    #wt_list is a wt of doubles
    #this is a void return so it modifies directly
    def mutate(self, wt_list):
        
        for weight in wt_list:
            
            if (random.random() < self.MUTATION_RATE):
                ind = wt_list.index(weight)
                updt_wt = weight
                type(updt_wt)
                updt_wt += random.uniform(-1,1)
                wt_list[ind] = updt_wt
    
    def calcTotalFitness(self):
        o_list = []
        fitnessList = []
        for snake in self.SNAKE_LIST:
            out = snake.instruction_list
            o_list.append(out)
        total_fitness = 0
        for snake in self.SNAKE_LIST:
            self.SIM_SNAKE.init_snake(o_list[self.SNAKE_LIST.index(snake)], snake.PX, snake.PY, snake.XG, snake.YG, 1.2)
            fitness = self.SIM_SNAKE.sim_snake()
            total_fitness += fitness
            snake.fitness = fitness
            fitnessList.append(fitness)
        
        
        self.FITNESS_LIST = fitnessList
        return total_fitness
            
            
            
    
    def RouletteWheelSelection(self):
        fSlice = random.random() * self.TOTAL_FITNESS
        cfTotal = 0
        selectedSnake = 0
        for i in range(0, len(self.SNAKE_LIST)):
            cfTotal += self.FITNESS_LIST[i]
            
            if(cfTotal > fSlice):
                selectedSnake = i
                break
            
        return self.SNAKE_LIST[selectedSnake]

    def CrossoverOperation(self, Snake1, Snake2, empty1, empty2):
        
        chosenPoint = int(math.floor(random.uniform(0, len(Snake1.brain.get_Weights()) - 1)))
        s1weights = Snake1.brain.get_Weights()
        s2weights = Snake2.brain.get_Weights()
        for i in range(0, chosenPoint):
            empty1.append(s1weights[i])
            empty2.append(s2weights[i])
        
        for j in range(chosenPoint, len(s1weights)):
            empty1.append(s2weights[j])
            empty2.append(s1weights[j])
        
        return empty1, empty2
    
    def Epoch(self):
        self.TOTAL_FITNESS  = self.calcTotalFitness()
        
        newBabies = 0
        babySnakes = []
        while (newBabies < self.POP_SIZE):
            mother_snake = self.RouletteWheelSelection()
            father_snake = self.RouletteWheelSelection()
            
            b1wt, b2wt = self.CrossoverOperation(mother_snake, father_snake, [],[])
            
            self.mutate(b1wt)
            self.mutate(b2wt)
            
            baby1 = Snake(10,10,5)
            baby2 = Snake(10,10,5)
            
            baby1.brain.put_Weights(b1wt)
            baby2.brain.put_Weights(b2wt)
            
            babySnakes.append(baby1)
            babySnakes.append(baby2)
            
            newBabies += 2
            
        
        self.SNAKE_LIST = babySnakes
        self.GENERATION += 1 
        self.TOTAL_FITNESS  = self.calcTotalFitness()
        
        
            
        
        
            
            
            
            
                    
            
                           
        
        
        
        
            
        