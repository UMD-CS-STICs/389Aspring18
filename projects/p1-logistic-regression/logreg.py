# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import argparse
import numpy as np
import pandas as pd
from math import exp
from sklearn.utils import shuffle


kSEED = 5


def normalize_dataframe(df):
    """
    Normalize dataframe so all real number features are between -1 and 1.
    (Optional): Extra Credit if completed.

    :return: normalized dataframe
    """
    return df


def load_data(file_name, columns):
    """
    Loads in data as dataframe, sets data type, and returns list of Examples.

    :param file_name: Dataset file to read in
    :param columns: Names of each column in dataset

    :return: A list of Examples
    """
    data = []
    df = pd.read_csv(file_name, names=columns, delimiter=',', header=-1)
    df[columns[:-1]] = df[columns[:-1]].astype(float)
    df[columns[-1]] = df[columns[-1]].astype(int)

    # (Optional) Implement for extra credit.
    df = normalize_dataframe(df)

    for row in df.itertuples():
        label = row[9]
        features = row[1:9]
        example = Example(features, label)
        data.append(example)
    return data


def train_test_split(data, frac=0.8):
    """
    Shuffles original data and performs a train-test split for training.
    Scikit-learn's shuffle function may be useful here.

    :param data: List of data to split on.
    :param frac: Percentage of data to use for training (.8 -> 80% for training, 20% for testing).

    :return: Returns two lists: one used for training and one for testing.
    """
    




    return data, data


def get_accuracy(y_bar, y_pred):
    """
    Computes what percent of the total testing data the model classified correctly.

    :param y_bar: List of ground truth classes for each example.
    :param y_pred: List of model predicted class for each example.

    :return: Returns a real number between 0 and 1 for the model accuracy.
    """
    correct = 0
    for i in range(len(y_bar)):
        if y_bar[i] == y_pred[i]:
            correct += 1
    accuracy = (correct / len(y_bar)) * 100.0
    return accuracy


class Example:
    """
    Class to represent a logistic regression example.
    """

    def __init__(self, features, label):
        """
        Create a new example.

        :param label: The label (0 / 1) of the example
        :param vocab: The real valued features of patient (list)
        """
        self.features = features
        self.label = label


class Model:
    """
    Class to represent a logistic regression model.
    """

    def __init__(self, l_rate, n_epoch, train):
        """
        Create a new model with certain parameters.

        :param l_rate: Initial learning rate for model.
        :param n_epoch: Number of epochs to train for.
        :param train: List of training Examples to train model on.
        """
        self.l_rate = l_rate
        self.n_epoch = n_epoch
        self.coef = [0.0] * (len(train[0].features))
        self.bias = 0.0

    def predict(self, features):
        """
        Given an example's features and the coefficients, predicts the class.

        :param features: List of real valued features for a single training example.

        :return: Returns the predicted class (either 0 or 1).
        """
        



        return 0

    def sg_update(self, example):
        """
        Computes the update to the weights based on a predicted example.

        :param example: Example to predict class on.
        """
        yhat = self.predict(example.features)
        



        return

    def sgd(self):
        """
        Computes logistic regression coefficients using stochastic gradient descent.

        :return: Returns a list of model weight coefficients where coef[0] is the bias.
        """
        for epoch in range(self.n_epoch):
            for example in train:
                self.sg_update(example)
        return self.coef


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--lr", help="Initial learning rate",
                           type=float, default=0.1, required=False)
    argparser.add_argument("--n_epoch", help="Number of epochs to train for",
                           type=float, default=100, required=False)
    args = argparser.parse_args()

    file_name = 'diabetes.csv'
    columns = [
        'Number of times pregnant',
        'Plasma glucose concentration a 2 hours in an oral glucose tolerance test',
        'Diastolic blood pressure (mm Hg)',
        'Triceps skin fold thickness (mm)',
        '2-Hour serum insulin (mu U/ml)',
        'Body mass index (weight in kg/(height in m)^2)',
        'Diabetes pedigree function',
        'Age (years)',
        'Class variable (0: no diabetes, 1: diabetes)']

    # Load data and perform train test split.
    data = load_data(file_name, columns)
    train, test = train_test_split(data, frac=0.8)

    # Train model.
    print('[INFO] Began training model.')
    model = Model(args.lr, args.n_epoch, train)
    model.sgd()

    # Get model predictions.
    print('[INFO] Getting predictions.')
    y_pred = list()
    y_pred = [round(model.predict(example.features)) for example in test]

    # Evaluate model.
    y_bar = [example.label for example in test]
    accuracy = get_accuracy(y_bar, y_pred)
    print('[INFO] Accuracy: {:0.3f}'.format(accuracy))

    print('\n[DONE]')
