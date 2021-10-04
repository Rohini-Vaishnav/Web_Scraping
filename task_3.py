import json
import pprint
with open("imdb_movies.json","r")as file:
    data1=json.load(file)
    # print(data1)
def group_ten_year(movies):
    details={}
    movie_1960=[]
    movie_1970=[]
    movie_1980=[]
    movie_1990=[]
    movie_2000=[]
    movie_2010=[]
    movie_2020=[]

    for movies_Details in movies:
        # print(movies_Details)
        if (int(movies_Details["year"]>=1960 and movies_Details["year"]<=1969)):
            movie_1960.append(movies_Details)
        elif (int(movies_Details["year"]>=1970 and movies_Details["year"]<=1979)):
            movie_1970.append(movies_Details)
        elif (int(movies_Details["year"]>=1980 and movies_Details["year"]<=1989)):
            movie_1980.append(movies_Details)
        elif (int(movies_Details["year"]>=1990 and movies_Details["year"]<=1999)):
            movie_1990.append(movies_Details)
        elif (int(movies_Details["year"]>=2000 and movies_Details["year"]<=2009)):
            movie_2000.append(movies_Details)
        elif (int(movies_Details["year"]>=2010 and movies_Details["year"]<=2019)):
            movie_2010.append(movies_Details)
        else:
            movie_2020.append(movies_Details)

        details["1960"]=movie_1960
        details["1970"]=movie_1970
        details["1980"]=movie_1980
        details["1990"]=movie_1990
        details["2000"]=movie_2000
        details["2010"]=movie_2010
        details["2020"]=movie_2020
    
    pprint.pprint(details)

    with open("10_year_movies.json","w")as file:
        json.dump(details,file,indent=4)
group_ten_year(data1)