import requests
import json
import os
with open("imdb_movies.json","r")as file:
    data1=json.load(file)
def get_movie_list_details(movie):
    movie_list = []
    for i in movie:
        path = "imdb_movies" + i["name"] + ".json"
        if os.path.exists("file.json"):
            pass
        else:
            create = open("imdb_movies" + i["name"] + ".json","w")
            url = requests.get(i["url"])
            create1 = create.write(url.text)
            create.close()
            a = movie(i["name"],i["url"])
            movie_list.append(a)
        with open("task_9.json","w") as file5:
            json.dump(a,file5,indent = 4)
        print(a)
get_movie_list_details(data1)