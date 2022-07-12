from csv import reader
from math import sqrt
from random import randrange, seed


# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# Convert string column to float:
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# Calculate root mean squared error
def rmse_metric(actual, predicated):
    sum_error = 0.0
    for i in range(len(actual)):
        predication_error = predicated[i] - actual[i]
        sum_error += (predication_error ** 2)
    mean_error = sum_error / float(len(actual))
    return sqrt(mean_error)

# Split a dataset into a train and test set
def train_test_split(dataset, split):
    train = list()
    dataset_copy = list(dataset)
    train_size = split * len(dataset)
    while len(train) < train_size:
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    return train, dataset_copy 

# Evaluate an algorithm using a train/test split
def evaluate_algorithm(dataset, algorithm, split, *args):
    train, test = train_test_split(dataset, split)
    test_set = list()
    for row in test:
        row_copy = list(row)
        row_copy[-1] = None
        test_set.append(row_copy)   
    actual = [row[-1] for row in test]
    predicated = algorithm(train, test_set, *args)
    rmse = rmse_metric(actual, predicated)
    return rmse

# Calculate the mean value of a list of numbers
def mean(values):
    return sum(values) / float(len(values))

# Calculate covariance between x and y
def covariance(x, x_mean, y, y_mean):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - x_mean) * (y[i] - y_mean)
    return covar

# Calculate variance of a list of numbers
def variance(values, mean):
    return sum([(x-mean)**2 for x in values])

# Calculate coefficients
def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    x_mean, y_mean = mean(x), mean(y)
    b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return [b0, b1]

# Simple linear regression algorithm
def simple_linear_regression(train, test):
    predictions = list()
    b0, b1 = coefficients(train)
    for row in test:
        yhat = b0 + b1 * row[0]
        predictions.append(yhat)
    return predictions

# Simple linear regression on salary dataset
seed(1)
# load and prepare data
salary_data = 'Salary_Data.csv'
insurance_data = 'insurance.csv'
dataset = load_csv(insurance_data)
for i in range(len(dataset[0])):
    str_column_to_float(dataset, i)
# evaluate algorithm
split = 0.6
rmse = evaluate_algorithm(dataset, simple_linear_regression, split)
print('RMSE: %.3f' % rmse)
