from Neuron import Neuron
class NeuronLayer(object):
    
    def __init__(self, num_neurons, inputs_per_neuron):
        self.NUMBER_OF_NEURONS = num_neurons
        self.neuron_list = []
        for i in range(0, num_neurons):
            n = Neuron(inputs_per_neuron)
            self.neuron_list.append(n)
        