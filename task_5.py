import requests
import json
from bs4 import BeautifulSoup

with open("imdb_movies.json","r")as file:
    data1=json.load(file)
def scrape_movie_details(movies):
    s=[] 
    for i in movies:
        s.append(i)
    s1=s[:10]
    list1=[]
    for j in s1:

        url=j["url"]
        dict1={}

        r = requests.get(url)

        soup = BeautifulSoup(r.text,"html.parser")

        poster=soup.find("div",class_="ipc-poster").a["href"]
        
        poster1="https://www.imdb.com"+poster

        dict1["name"]=j["name"]
        dict1["poster_image_url"]=poster1

        para1=soup.find_all('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
        for k in para1:
            para2=k.find_all('li')
            for i in para2:
                if "Language" in i.text:
                    a=i.find('a').text
                    dict1["langauge"]=a
                elif 'Country of origin' in i.text:
                    a=i.find('a').text
                    dict1["country"]=a

        dram=soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-all Storyline__StorylineMetaDataList-sc-1b58ttw-1 esngIX ipc-metadata-list--base")
        # print(dram)
        namedata=dram.find_all("li",class_="ipc-metadata-list__item")
        
        l1=[]
        for j in namedata:
            if "Genres" in j.text:
                k=j.find_all('a')
                for l in k:
                    l1.append(l.text)
                break
        dict1['Genres']=l1

        der=soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt")
        der1=der.find_all('li')
        der2=der1[0].find_all('a')

        l2=[]
        for k in der2:
            l2=(k.text)
        dict1['director']=l2
        list1.append(dict1)
    print(list1)

    with open ("10_movies_details.json","w")as file:
        data=json.dump(list1,file,indent=4)

scrape_movie_details(data1)