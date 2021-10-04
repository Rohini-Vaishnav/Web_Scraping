import json
with open("10_movies_details.json","r")as file:
    data1=json.load(file)
def movies_director(movie):
    director=[]
    dic={}
    for a in movie:
        for b in a:
            if b == 'director':
                director.append(a[b])  
    index=0
    while index<len(director):
        i=0
        count=0
        while i<len(director):
            if director[index]==director[i]:
                count=count+1
            i=i+1
        if director[index] not in dic:
            dic[director[index]]=count
        index=index+1
    print(dic)
    with open("movie_director.json","w") as lang_uage:
        json.dump(dic,lang_uage,indent=4)
movies_director(data1)