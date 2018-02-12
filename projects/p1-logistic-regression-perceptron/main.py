# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import argparse
import logreg
import numpy as np
import pandas as pd
from perceptron import Perceptron
from logreg import LogReg
from sklearn.utils import shuffle


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


def train_test_split(data, frac=0.8, seed=5):
    """
    Shuffles original data and performs a train-test split for training.
    Scikit-learn's shuffle function may be useful here.

    :param data: List of data to split on.
    :param frac: Percentage of data to use for training (.8 -> 80% for training, 20% for testing).

    :return: Returns two lists: one used for training and one for testing.
    """
    data = shuffle(data, random_state=seed)
    split_index = int(frac * len(data))
    train = data[:split_index]
    test = data[split_index:]
    X_train = [example.features for example in train]
    y_train = [example.label for example in train]
    X_test = [example.features for example in test]
    y_test = [example.label for example in test]
    return X_train, X_test, y_train, y_test


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


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--lr_logreg', help='Logistic learning rate',
                           type=float, default=0.1, required=False)
    argparser.add_argument('--lr_perceptron', help='Perceptron learning rate',
                           type=float, default=0.1, required=False)
    argparser.add_argument('--epochs', help='Number of epochs to train for',
                           type=int, default=100, required=False)
    argparser.add_argument('--batch_size', help='Number of samples per batch',
                           type=int, default=10, required=False)
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
    print('[INFO] Loading data.')
    data = load_data(file_name, columns)
    X_train, X_test, y_train, y_test = train_test_split(data, frac=0.8, seed=5)

    # Logistic Model
    print('\n[INFO] Training logistic regression model.')
    logreg = LogReg(args.lr_logreg, args.epochs, len(X_train[0]))
    bias_logreg, weights_logreg = logreg.train(X_train, y_train)
    y_logistic = [round(logreg.predict(example)) for example in X_test]

    # Perceptron Model
    print('[INFO] Training Perceptron model.')
    perceptron = Perceptron(args.lr_perceptron, args.epochs, len(X_train[0]))
    bias_perceptron, weights_perceptron = perceptron.train(X_train, y_train)
    y_perceptron = [round(perceptron.predict(example)) for example in X_test]

    # Compare accuracies
    accuracy_logistic = get_accuracy(y_logistic, y_test)
    accuracy_perceptron = get_accuracy(y_perceptron, y_test)
    print('\n[INFO] Logistic Regression Accuracy: {:0.3f}'.format(
        accuracy_logistic))
    print('[INFO] Perceptron Accuracy: {:0.3f}'.format(accuracy_perceptron))

    print('\n[DONE]')
