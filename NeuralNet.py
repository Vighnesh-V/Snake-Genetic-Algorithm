from NeuronLayer import NeuronLayer
from Neuron import Neuron
import math

class FFNeuralNet(object):
    
    def __init__(self, num_inputs,num_outputs, num_hidden_layers, num_neuronsp_hl):
        self.NUM_INPUTS = num_inputs
        self.NUM_OUTPUTS = num_outputs
        self.NUM_HIDDEN_LAYERS = num_hidden_layers
        self.NEURONS_PER_HIDDEN_LAYER = num_neuronsp_hl
        self.LAYER_LIST = []
        self.NUM_WEIGHTS = 0
        self.create_Net()
        self.INITIAL_BIAS = -1
        
    
    def create_Net(self):
        num_weights = 0
        if(self.NUM_HIDDEN_LAYERS > 0):
            x = NeuronLayer(self.NEURONS_PER_HIDDEN_LAYER, self.NUM_INPUTS)
            self.LAYER_LIST.append(x)
            num_weights += (self.NUM_INPUTS + 1) * self.NEURONS_PER_HIDDEN_LAYER
            
            for i in range(0, self.NUM_HIDDEN_LAYERS - 1):
                y = NeuronLayer(self.NEURONS_PER_HIDDEN_LAYER, self.NEURONS_PER_HIDDEN_LAYER)
                self.LAYER_LIST.append(y)
                num_weights += (self.NEURONS_PER_HIDDEN_LAYER + 1) * self.NEURONS_PER_HIDDEN_LAYER
            
            z = NeuronLayer(self.NUM_OUTPUTS,self.NEURONS_PER_HIDDEN_LAYER)
            self.LAYER_LIST.append(z)
            num_weights += (self.NEURONS_PER_HIDDEN_LAYER + 1) * self.NUM_OUTPUTS
        else:
            j = NeuronLayer(self.NUM_OUTPUTS, self.NEURONS_PER_HIDDEN_LAYER)
            self.LAYER_LIST.append(j)
            num_weights += (self.NEURONS_PER_HIDDEN_LAYER + 1) * self.NUM_OUTPUTS
        
        self.NUM_WEIGHTS = num_weights
    
    def get_Weights(self):
        weight_list = [0.2]
        for layer in self.LAYER_LIST:
            for neuron in layer.neuron_list:
                weight_list.extend(neuron.weight_vector)
        weight_list.pop(0)
        return weight_list
            
        
            
                
        
    
    def get_NumWeights(self):
        return self.NUM_WEIGHTS
        
        
        
    
    def put_Weights(self, bigList):
        index = 0
        for layer in self.LAYER_LIST:
            for neuron in layer.neuron_list:
                vct_length = len(neuron.weight_vector)
                neuron.weight_vector = bigList[index:index + vct_length]
                index += vct_length
            
    
    #response should be set to -1
    def sigmoid(self, activation, response):
        return 1 / (1 + math.exp(activation/response))
    
    def feed_forward(self, input_list):
    
        outputs = []
        input = input_list
        iWeight = 0
        if(len(input_list) != self.NUM_INPUTS):
            return outputs
        
        for layer in self.LAYER_LIST:
            
            #set input = output if layer index > 0
            if(self.LAYER_LIST.index(layer) > 0):
                input = outputs
            outputs = []
            iWeight=0
            #for each layer clear the output list
            for neuron in layer.neuron_list:
                nsum = 0
                #reset summation of activation here - needs to happen for EACH neuron
                for weight in neuron.weight_vector:
                    #multiplication by input list happens here
                    if(neuron.weight_vector.index(weight) == len(neuron.weight_vector) - 1):
                        nsum += weight*self.INITIAL_BIAS
                    else:
                        nsum += weight*input[iWeight]
                        iWeight += 1
                #pass through sigmoid here
                #append to output list here
                outputs.append(self.sigmoid(nsum,1))
                iWeight = 0
        
        return outputs
                    
                    
                
                
                    
            
            
        
        
        