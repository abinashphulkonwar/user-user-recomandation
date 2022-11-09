import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

data = pd.read_csv("./rating.csv")




X = []
Y = []


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


X_mean = statistics.mean(X)
Y_mean = statistics.mean(Y)





r = 0

XiX = 0
XiX_numarator = 0
for i in range(len(X)):
    val = X[i] - X_mean
    XiX = XiX + val
    XiX_numarator = XiX_numarator + val


import math

XiX_numarator= math.pow(XiX_numarator,2)

YiY = 0
YiY_numarator = 0

for i in range(len(Y)):
    val = Y[i] - Y_mean
    YiY = YiY + val
    YiY_numarator = YiY_numarator + val

print("YiY_numarator",YiY_numarator)
YiY_numarator = math.pow(YiY_numarator,2)

denomator = XiX * YiY

numarator = XiX_numarator * YiY_numarator

print(denomator,numarator, math.sqrt(numarator))

r = denomator / math.sqrt(numarator)

print(r)