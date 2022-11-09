import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

data = pd.read_csv("./rating.csv")




userIds = {}
movieIds = {}

for i in range(len(data["userId"])):
    if userIds.get(data["userId"][i]):
        currentRating = userIds[data["userId"][i]]["rating"]
        currentCount = userIds[data["userId"][i]]["count"]
        userIds[data["userId"][i]] =  {"count" : currentCount + 1, "rating" : currentRating + data["rating"][i]  }
    else:
        userIds[data["userId"][i]] =  {"count" : 1, "rating" : data["rating"][i] }

    if movieIds.get(data["movieId"][i]):
        currentRating = movieIds[data["movieId"][i]]["rating"]
        currentCount = movieIds[data["movieId"][i]]["count"]
        userIds[data["movieId"][i]] =  {"count" : currentCount + 1, "rating" : currentRating + data["rating"][i]  }
    else:
        movieIds[data["movieId"][i]] =  {"count" : 1, "rating" : data["rating"][i] }



def avarage(n :int= 0, value:int = 0):
    return value/n




X = []
Y = []





for key in userIds:
    currentRating = userIds[key]["rating"]
    currentCount = userIds[key]['count']
    av = avarage(currentCount, currentRating)
    X.append(av)

for key in movieIds:
    currentRating = movieIds[key]["rating"]
    currentCount = movieIds[key]['count']
    av = avarage(currentCount, currentRating)
    Y.append(av)


X_avg = np.average(X)
Y_avg = np.average(Y)

# numerator

numerator = 0

sig_X = 0
sig_Y = 0

for i in range(len(X)):
    val_X = X[i] - X_avg
    sig_X = sig_X+val_X

for i in range(len(Y)):
    val_Y = Y[i] - Y_avg
    sig_Y = sig_Y+val_Y


numerator = sig_X*sig_Y

print("numerator" ,numerator)

# denominator

sig_X = 0
sig_Y = 0

for i in range(len(X)):
    val_X = np.power(X[i] - X_avg,2)
    sig_X = sig_X+val_X

for i in range(len(Y)):
    val_Y =  np.power( Y[i] - Y_avg,2)
    sig_Y = sig_Y+val_Y

import math

denominator = math.sqrt(sig_X*sig_Y)

print('denominator',denominator)

r = numerator /denominator
print("R", r)