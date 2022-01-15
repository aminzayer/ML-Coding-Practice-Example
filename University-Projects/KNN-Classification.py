# K-NN Classification Algorithms Implementation
from statistics import mean
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import math
import operator


class KNN():
    def __init__(self, k):
        self.k = k
        print(self.k)

    def fit(self, X_train, y_train):
        self.x_train = X_train
        self.y_train = y_train

    def calculate_Manhattan(self, sample1, sample2):
        distance = 0.0
        for i in range(len(sample1)):
            # Euclidean Distance = sqrt(sum i to N (x1_i – x2_i)^2)
            distance += abs(sample1[i]-sample2[i])
        return distance

    def nearest_neighbors(self, test_sample):
        distances = []  # calculate distances from a test sample to every sample in a training set
        for i in range(len(self.x_train)):
            distances.append(
                (self.y_train[i], self.calculate_Manhattan(self.x_train[i], test_sample)))

        print("\nAll Distances from a test sample to every sample in a training set :\n", distances)
        # sort in ascending order, based on a distance value
        distances.sort(key=lambda x: x[1])
        neighbors = []
        for i in range(self.k):  # get first k samples
            neighbors.append(distances[i][0])

        print("Neighbors Test Data (", test_sample, ") is : ", neighbors, "\n")
        return neighbors

    def predict(self, test_set):
        predictions = []
        for test_sample in test_set:
            neighbors = self.nearest_neighbors(test_sample)
            labels = [sample for sample in neighbors]
            prediction = max(labels, key=labels.count)
            predictions.append(prediction)
        return predictions

    def predict_regression(self, test_set):
        predictions = []
        for test_sample in test_set:
            neighbors = self.nearest_neighbors(test_sample)
            labels = [sample for sample in neighbors]
            print(labels)
            prediction = max(labels, key=labels.count)
            predictions.append(prediction)
        return predictions


data = pd.DataFrame([[3, 7, '+'],
                     [4, 6, '+'],
                     [2, 1, '-'],
                     [1, 1, '-'],
                     [7, 7, '+'],
                     [4, 8, '+'],
                     [3, 0, '-'],
                     [2, 4, '-'],
                     [8, 8, '+'], ],
                    columns=['F1', 'F2', 'Class'])

Test_data = pd.DataFrame([[2, 5, '?'],
                          [3, 4, '?'], ],
                         columns=['F1', 'F2', 'Class'])

X = np.array(data)[:, 0:2]
print("\nInstances are:\n", X)
y = np.array(data)[:, -1]
print("\nTarget Values are: \n", y)
model = KNN(3)  # our model
model.fit(X, y)
X_test = np.array(Test_data)[:, 0:2]
print("\nTest Values are: \n", X_test)
predictions_KNN = model.predict(X_test)
print("\nKNN Perdiction values are : ", predictions_KNN)
predictions_KNN_Reg = model.predict_regression(X_test)
print('\nKNN Regression Perdiction values are : ', predictions_KNN_Reg)

# True Positive (TP): True positive represents the value of correct predictions of positives out of actual positive cases
# Main is True & Predict True ( + => + )
TP = 1 
# False Positive (FP): False positive represents the value of incorrect positive predictions.
# Main is False & Predict True ( - => + )
FP = 2
# True Negative (TN): True negative represents the value of correct predictions of negatives out of actual negative cases.
# Main is False & Predict False ( - => - )
TN = 1
# False Negative (FN): False negative represents the value of incorrect negative predictions.
# Main is True & Predict Flase ( + => - )
FN = 1
Accuracy = (TP + TN) / (TP+FN+TN+FP)
print("Accuracy = (TP=", TP, "+", "TN= ", TN, ") / (",
      "TP=", TP, "+", "FN=", FN, "+", "TN=", TN, "+", "FP=", FP, ") = ", (TP + TN), "/", (TP+FN+TN+FP)," = ", Accuracy," = %",Accuracy*100 )
