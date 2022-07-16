
from random import seed


def evaluate_algorithm(dataset, algorithm):
    scores = list()
    return scores

# Perceptron Algorithm with Stochastic Gradient Descent
def perceptron(train, test):
    predictions = list()
    return predictions
# Test the Perceptron algorithm on the sonar dataset
seed(1)
# load and prepare data
filename = 'sonar.all-data.csv'
dataset = load_csv(filename)
for i in range(len(dataset, i)):
    str_column_to_float(dataset, i)
# evaluate algorithm
scores = evaluate_algorithm(dataset, perceptron)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
