from pandas import read_csv
import matplotlib.pyplot as plt
import numpy
from keras.models import Sequential
from keras.layers import Dense

def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
    return numpy.array(dataX), numpy.array(dataY)    

dataframe = read_csv('international-airline-passengers.csv', usecols=[1])
dataset = dataframe.values

train_size = int(len(dataset) * 0.67)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print(len(train), len(test))

model = Sequential()
model.add(Dense())
