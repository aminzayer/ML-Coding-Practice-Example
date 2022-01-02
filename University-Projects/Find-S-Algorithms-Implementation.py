import pandas as pd
import numpy as np

# to read the data in the csv file or Create Data frame
# ---------------- Read File Codes ------------
# data = pd.read_csv("data.csv")
# print(data, "n")
# ----------- Create DataFrame Codes ----------
data = pd.DataFrame([['Morning', 'Sunny', 'Warm', 'Yes', 'Mild', 'Strong', 'Yes'],
                     ['Evening', 'Rainy', 'Cold', 'No', 'Mild', 'Normal', 'No'],
                     ['Morning', 'Sunny', 'Moderate',
                         'Yes', 'Normal', 'Normal', 'Yes'],
                     ['Evening', 'Sunny', 'Cold', 'Yes', 'High', 'Strong', 'Yes'],
                     ['Morning', 'Sunny', 'Moderate', 'Yes', 'Mild', 'Strong', 'Yes']],
                    columns=['Time', 'Weather', 'Temperature', 'Company', 'Humidity', 'Wind', 'Goes'])

# making an array of all the attributes
d = np.array(data)[:, :-1]
print("n The attributes are: ", d)

# segragating the target that has positive and negative examples
target = np.array(data)[:, -1]
print("n The target is: ", target)

# training function to implement find-s algorithm
def train(c, t):
    for i, val in enumerate(t):
        if val == "Yes":
            specific_hypothesis = c[i].copy()
            break

    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
        print("level ",i," ",specific_hypothesis)

    return specific_hypothesis


# obtaining the final hypothesis
print("n The final hypothesis is:", train(d, target))

# New DataFrame For test
data = pd.DataFrame([['a1', 'b2', 'c1', 'd3', 'e2', 'f1', 'Yes'],
                     ['a1', 'b2', 'c2', 'd3', 'e1', 'f1', 'No'],
                     ['a1', 'b3', 'c1', 'd3', 'e1', 'f1', 'Yes'],
                     ['a1', 'b1', 'c1', 'd3', 'e3', 'f1', 'Yes'],
                     ['a2', 'b2', 'c1', 'd3', 'e3', 'f3', 'Yes']],
                    columns=['A', 'B', 'C', 'D', 'E', 'F', 'Target'])

# making an array of all the attributes
d = np.array(data)[:, :-1]
print("n The attributes are: ", d)

# segragating the target that has positive and negative examples
target = np.array(data)[:, -1]
print("n The target is: ", target)

# obtaining the final hypothesis
print("n The final hypothesis is:", train(d, target))
