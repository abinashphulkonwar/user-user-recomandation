import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

data = pd.read_csv("./archive-1/rating.csv")





# 31043
def getUserRateItemJCount(j):
    count = 0
    av = 0
    for i in range(len(data["rating"])):
        if data["anime_id"][i] == j:
            if data["rating"][i] != -1:
                 count = count +1  
                 av = av+data["rating"][i]
    return {
        "count":count,
        "av" : av
    }
def s(j):
    val = getUserRateItemJCount(j)
    print(val)
    denominator = val["count"]  # type: ignore
    nuramotar = val["av"]  # type: ignore
    return nuramotar/denominator



sj = s(31043)

print(sj)