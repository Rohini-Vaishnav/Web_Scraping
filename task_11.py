import json
# from task_5 import scrape_movie_details
# data1=scrape_movie_details
with open("10_movies_details.json","r")as file:
    data1 = json.load(file)

def anlyse_movie_genre(data):
    i = 0
    list = []
    while i < len(data):
        for key in data[i]:
            if key == "Genres":
                index = 0
                while index < len(data[i][key]):
                    list.append(data[i][key][index])
                    index += 1
        i += 1
    j = 0
    dic = {}
    while j < len(list):
        if list[j] not in dic:
              dic[list[j]] = 1
        else:
            dic[list[j]] += 1
        j += 1
    with open("task_11.json","w")as f:
        json.dump(dic,f,indent = 4)
    print(dic)
anlyse_movie_genre(data1)