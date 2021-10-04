import json
import pprint
with open("imdb_movies.json")as data:
    data1=json.load(data)
def group_by_year(movies):
    detail={}
    for i in movies:
        # print(i)
        year=i["year"]
        # print(year1)
        list=[]
        for j in movies: 
            if year==j["year"]:
                list.append(j)
        detail[year]=list
        pprint.pprint(detail)
        with open("year_by_movies.json","w")as file:
            json.dump(detail,file,indent=4)
group_by_year(data1)