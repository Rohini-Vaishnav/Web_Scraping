import json
with open("10_movies_details.json","r")as f:
    data=json.load(f)
def language_and_directors(data):
    dic1={}
    for movie in data:
        for director in movie["director"]:
            dic1[director]={}
    for director in dic1:
        for dic_movie in data:
            if director in dic_movie["director"]:
                if "langauge" in dic_movie:
                    lan=dic_movie["langauge"]
                    count=0
                    dic1[director][lan]=count
                    for eachdic in data:
                        if "langauge" in eachdic:
                            lan2=eachdic["langauge"]
                            if (lan==lan2) and director in eachdic["director"]:
                                dic1[director][lan]+=1
    with open("task10.json","w") as f:
        json.dump(dic1,f,indent=4)
language_and_directors(data) 