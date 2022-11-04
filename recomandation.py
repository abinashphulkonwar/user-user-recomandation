import pandas as pd

data = pd.read_csv("./rating.csv")
movies = pd.read_csv("movie.csv")

userIds = {}




for i in range(len(data["userId"])):
    if userIds.get(data["userId"][i]):
        currentRating = userIds[data["userId"][i]]["rating"]
        currentCount = userIds[data["userId"][i]]["count"]
        userIds[data["userId"][i]] =  {"count" : currentCount + 1, "rating" : currentRating + data["rating"][i]  }
    else:
        userIds[data["userId"][i]] =  {"count" : 1, "rating" : data["rating"][i] }


def avarage(n :int= 0, value:int = 0):
    return value/n


for key in userIds:
    currentRating = userIds[key]["rating"]
    currentCount = userIds[key]['count']
    av = avarage(currentCount, currentRating)
    userIds[key] =  {"count" : currentCount, "rating" : currentRating, "avarage": av }



def dev(user :int= 0, movie:int = 0, av :int=0):
    return movie - av

userDeviation = []

userToPredict = {
"userId" : 20,
"avarage" : 4.5
}

def getWeidthAvarage(currentUserAvarage):
    for key in userIds:
        avarage = userIds[key]["avarage"]
        weidthAvarage =  (avarage + currentUserAvarage)/2
        userDeviation.append(weidthAvarage)


print( getWeidthAvarage(userToPredict["avarage"]))
print( userDeviation)