Project 1: Logistic Regression & Perceptron
=

Due: 16. February (23:59)

Overview
-
In this assignment you will implement logistic regression along with a basic perceptron model both using stochastic gradient descent (SGD). The task we will apply this to is predicting whether or not a patient has diabetes (0: no diabetes, 1: diabetes). The information we are given about the patient include:
1. Number of times pregnant 
2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test 
3. Diastolic blood pressure (mm Hg) 
4. Triceps skin fold thickness (mm) 
5. 2-Hour serum insulin (mu U/ml) 
6. Body mass index (weight in kg/(height in m)^2) 
7. Diabetes pedigree function 
8. Age (years)

You should **not** use any libraries that implement any of the logistic regression, perceptron, or sgd functionality for you. In the future we will be able to use premade implementations but this assignment will serve as a warm up and should not take more than an hour to complete.

You will turn in the assigment using the submit server by 2/16 at 11:59 p.m.

Assignment
-

#### Coding (20 points):

1. Understand how the code works.
2. (5 points) Logistic Regression: In `logreg.py`, implement the `predict` function that predicts the class given the feature vector and weights. The `sigmoid` function is already implemented for you just call `self.sigmoid(float value)`.
3. (5 points) Logistic Regression: In `logreg.py`, finish implementing the `sg_update` function to update the weights based on the predicted class value using SGD.
4. (5 points) Perceptron: In `perceptron.py`, implement the `predict` function that predicts the class given the feature vector and weights.
5. (5 points) Perceptron: In `perceptron.py`, finish implementing the `sg_update` function to update the weights based on the predicted class value using SGD.

The accuracy of both models should be above 60% for full credit.

#### Analysis (10 points):

Questions (1-4) refer to the logistic regression model.
1. What is the role of the learning rate?
2. How many passes over the data do you need to complete?
3. What words are the best predictors of each class?  How (mathematically) did you find them?
4. What words are the poorest predictors of classes?  How (mathematically) did you find them?
5. What is an advantage of the perceptron algorithm compared to logistic regression?

#### Extra credit:

1. Implemenent the `normalize_dataframe` function.
    - Normalize all the real valued features to be between -1 and 1.
    - Explain why this would be useful.
2. Use a schedule to update the learning rate.
    - Supply an appropriate argument to step parameter
    - Support it in your `sg_update`
    - Show the effect in your analysis document

What to turn in
-

1. Submit your `logreg.py` and `perceptron.py` file (include your name at the top of the source)
1. Submit your `analysis.pdf` file
    - no more than one page
    - pictures are better than text
    - include your name at the top of the PDF

Hints
-

1. The methods for the perceptron model and the logistic regression model should look very similar with only slight differences in the update logic and prediction.
2. Try debugging your code with a small number of epochs first and check if your accuracy improves over time.
3. You may find `df['feature'].max()`, `df['feature'].min()`, and `df['feature'].mean()` to be useful for the  `normalize_dataframe` function extra credit.


###### Thanks to the writers of <a href = "https://github.com/Pinafore/ml-hw/blob/master/logreg/assign.md">this</a> assigment for the wording and inspiration of much of this project. Also thanks to UCI for the Pima Indians Diabetes Dataset available <a href="https://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes">here</a>.
