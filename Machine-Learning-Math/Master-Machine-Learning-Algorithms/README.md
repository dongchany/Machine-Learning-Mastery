# Master Machine Learning Algorithms

In the journey, You will get some points:

1. You started off with an interest in machine learning algorithms.
2. You learned the underlying principle for all supervised machine learning algorithms that they are estimating a mapping function from input to output variables.
3. You discovered the difference between parametric and nonparametric algorithms, supervised and unsupervised algorithms and error introduced from bias and variance.
4. You discovered and implemented linear machine learning algorithms including linear regression, logistic regression and linear discriminant analysis.
5. You implemented from scratch nonlinear machine learning algorithms including classification and regression trees, naive Bayes, k-nearest neighbors, learning vector quantization and support vector machines.
6. Finally, you discovered and implemented two of the most popular ensemble algorithms bagging with decision trees and boosting with adaboost.



### Background

When the journey start, we need to know and master some knowledge point and concepts in advance.



##### How to talk about data in machine learning

- You started with the standard understanding of tabular data as seen in a spreadsheet as columns, rows and cells.

- You learned the statistical terms of input and output variables that may be denoted as X and Y respectively.

- You learned the computer science terms of attribute, feature and instance.

- Finally you learned that talk of models and algorithms can be separated into learned

  representation and process for learning.



##### Algorithms learn a mapping from input to output

- You learned that machine learning algorithms work to estimate the mapping function (f) of output variables (Y ) given input variables (X), or Y = f(X).
- You also learned that different machine learning algorithms make different assumptions about the form of the underlying function.
- That when we don’t know much about the form of the target function we must try a suite of different algorithms to see what works best.



##### Parametric and nonparametric machine learning algorithms

- You learned that parametric methods make large assumptions about the mapping of the input variables to the output variable and in turn are faster to train, require less data but may not be as powerful.
- You also learned that nonparametric methods make few or no assumptions about the target function and in turn require a lot more data, are slower to train and have a higher model complexity but can result in more powerful models.



##### Supervised, unsupervised and semi-supervised learning

- Supervised: All data is labeled and the algorithms learn to predict the output from the input data.
- Unsupervised: All data is unlabeled and the algorithms learn to inherent structure from the input data.
- Semi-supervised: Some data is labeled but most of it is unlabeled and a mixture of supervised and unsupervised techniques can be used.



##### The bias-variance trade-off

- Bias is the simplifying assumptions made by the model to make the target function easier to approximate.
- Variance is the amount that the estimate of the target function will change given different training data.
- Trade-off is tension between the error introduced by the bias and the variance.



##### Overfitting and underfitting

- Overfitting: Good performance on the training data, poor generalization to other data. 
- Underfitting: Poor performance on the training data and poor generalization to other data.



### Linear Algorithms



##### Gradient descent for machine learning

- Optimization is a big part of machine learning.
- Gradient descent is a simple optimization procedure that you can use with many machine learning algorithms.
- Batch gradient descent refers to calculating the derivative from all training data before calculating an update.
- Stochastic gradient descent refers to calculating the derivative from each training data instance and calculating the update immediately.



##### Linear regression

- The common names used when describing linear regression models.
- The representation used by the model.
- Learning algorithms used to estimate the coefficients in the model.
- Rules of thumb to consider when preparing data for use with linear regression