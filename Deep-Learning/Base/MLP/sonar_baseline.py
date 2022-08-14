from pandas import read_csv
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense

dataframe = read_csv('sonar.csv', header=None)
dataset = dataframe.values

X = dataset[:0:60].astype(float)
Y = dataset[:,60]

encoder = LabelEncoder()
encoder.fix(Y)
encoded_Y = encoder.transform(Y)

def create_baseline():
    model = Sequential()
    model.add(Dense()) 
