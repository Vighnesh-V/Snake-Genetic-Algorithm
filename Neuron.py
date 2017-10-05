import random
class Neuron(object):
    #number of inputs includes the bias - considered a hidden input, but a visible weight
    def __init__(self, numInputs):
        self.NUMBER_OF_INPUTS = numInputs + 1
        self.weight_vector = []
        
        for i in range(0,self.NUMBER_OF_INPUTS):
            thresh = random.random()
            if(thresh < 0.5):
                self.weight_vector.append(-1.0 * random.random())
            else:
                self.weight_vector.append(random.random())
            