import requests
import os
import json 
with open("imdb_movies.json","r")as file:
    data1=json.load(file)
def num(movie):
    list = []
    for i in movie:
        path = "imdb_movies"+i["name"]+".text"
        if os.path.exists(path):
            pass
        else :
            create = open("imdb_movies"+ i["name"] + ".text","w")
            url = requests.get(i['url'])
            create1= create.write(url.text)
            create.close()
num(data1)