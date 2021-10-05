import json
with open("10_movies_details.json","r")as f:
    data = json.load(f)
def analyse_language_and_directors(data):
    dic={}
    for i in data:
        for j in i["director"]:
            dic[j]={}
    for director in dic:
        for dic_movie in data:
            if director in dic_movie["director"]:
                if "langauge" in dic_movie:
                    lan=dic_movie["langauge"]
                    language_Count=0
                    dic[director][lan]=language_Count
                    for each_dict in data:
                        if "langauge" in each_dict:
                            lan2=each_dict["langauge"]
                            if (lan==lan2) and director in each_dict["director"]:
                                dic[director][lan]+=1
    with open("task_10.json","w") as file:
        json.dump(dic,file,indent = 4)
analyse_language_and_directors(data)