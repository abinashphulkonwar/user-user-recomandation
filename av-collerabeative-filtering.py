import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./data.csv")




def getUserRateItemJCount(j):
    count = 0
    av = 0
    for i in range(len(data["rating"])):
        if data["user_id"][i] == j:
            count = count +1 
            av = av+data["rating"][i]
    return {
        "count":count,
        "av" : av
    }

# def s(j):
#     val = getUserRateItemJCount(j)
#     denominator = val["count"]  
#     nuramotar = val["av"] 
#     return nuramotar/denominator



# sj = s(31043)

# print("avarage rating of item 31043 :" , sj)



def averageRatinOfUserI(i):
    count = 0
    av = 0
   
    for index in range(len(data["rating"])):
        if data["user_id"][index] == i:
            count = count +1 
            av = av + data["rating"][index]
    return av/count

userRatings = {}

def userIIPrimeWeight():
    return userRatings

def averageRatinOfUsers(i):

    for index in range(len(data["rating"])):
        currentUserId =data["user_id"][index]
        if userRatings.get(currentUserId):
            count = userRatings[currentUserId]["count"]
            rating = userRatings[currentUserId]["rating"]
           # print(userRatings)
            userRatings[currentUserId]  = {"count" : count + 1, "rating": rating + data["rating"][index] }
        else:
            userRatings[currentUserId]  = {"count" : 1, "rating": data["rating"][index] }
    userIData = userRatings[i]
    for index in userRatings:
      if userRatings[index] != i:
        count = userRatings[index]["count"]
        rating = userRatings[index]["rating"]
        userRatings[index]  = {"rating" : rating/count, "weight" : (rating + userIData["rating"]) /(count+userIData["count"]) }
    return userRatings






def sumIraingToJ(i,j):
    sum = 0
    count = 0
    w_ii = 0
    for user in userRatings:
        weight = userRatings[user]["weight"]
        w_ii = w_ii +weight
            
    for index in range(len(data["rating"])):
        if data["anime_id"][index] == j:
             count = count+1
             currentUserId =data["user_id"][index]
             defi = data["rating"][index] -  userRatings[currentUserId]["rating"]
             sum = sum + (w_ii * defi)
    count = count + w_ii
    return sum/count

def s(i,j):
    averageRatinOfUser = averageRatinOfUserI(i)
    averageRatinOfUsers(i)
    dev = sumIraingToJ(i,j)
    return dev + averageRatinOfUser
   

score = s(2,15)

print(score)