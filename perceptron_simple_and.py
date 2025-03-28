#imoprtando librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Perceptron():
    def __init__(self,inputs,labels,learning_rate,weights,bias,epochs=20):
        self.inputs = inputs
        self.labels = labels
        self.learning_rate = learning_rate
        self.weights = weights
        self.bias = bias
        self.epochs = epochs

    
    def activation(self,z):
        return 1 if z > 0 else 0

    def predict(self, input_x, weights_ajustados, bias_ajustado):
        #Calcular la funcion z
        z = np.dot(input_x,weights_ajustados) + bias_ajustado
        #Calcular Y predicha
        y_pred = self.activation(z)
        return y_pred
    
    def fit(self):
        #Abrir un ciclo deacuerdo a las iteraciones (Epochs)
        for epoch in range(self.epochs):
            print(f"Epoch {epoch+1}/{self.epochs}", end = " ")
            #Variable para obtener el Error por cada epoch
            total_error = 0
            #Abrir ciclo para recorrer las entradas
            for input,label in zip(self.inputs,self.labels):
                # print(f"Input: {input}, Label: {label}")
                #Calcular la funcion z
                z = np.dot(input,self.weights) + self.bias
                #Calcular Y predicha
                y_pred = self.activation(z)
                #Cacular el error
                error = label - y_pred
                total_error += abs(error)
                #Calcular el Delta W
                delta_w = self.learning_rate * error * input
                # Actualizar los weights
                self.weights = self.weights + delta_w
                #Actualizar el bias
                delta_bias = self.learning_rate * error
                self.bias = self.bias + delta_bias
            #Calcular error primedio por epoch
            average_error = total_error/len(self.labels)
            print(f"Average Error: {average_error}")
        #Retornar los pesos y bias actualizados
        
        return self.weights, self.bias
                

