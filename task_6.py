import json
with open("10_movies_details.json","r")as file:
    data1=json.load(file)
def movies_language(movie):
    language=[]
    dic={}
    for a in movie:
        for b in a:
            if b == 'langauge':
                language.append(a[b])  
    index=0
    while index<len(language):
        i=0
        count=0
        while i<len(language):
            if language[index]==language[i]:
                count=count+1
            i=i+1
        if language[index] not in dic:
            dic[language[index]]=count
        index=index+1
    print(dic)
    with open("movie_language.json","w") as lang:
        json.dump(dic,lang,indent=4)
movies_language(data1)