# Load libraries
from matplotlib import pyplot

# Load dataset

# Spot-Check Algorithms
models = []
# evaluate each model in turn 
results = []
names = []
for name, model in models:
    

# Compare Algorithms
fig = pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklables(names)
pyplot.show()


# Make predictions on validation dataset

