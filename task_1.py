from bs4 import BeautifulSoup
import requests
import json
import pprint
url="https://www.imdb.com/india/top-rated-indian-movies/"
page=requests.get(url)
print(page.text)
soup=BeautifulSoup(page.text,"html.parser")
# print(soup)
def scrap_top_list():
    main_div=soup.find('div', class_='lister')
    # print(main_div)
    tbody=main_div.find('tbody', class_='lister-list')
    # print(tbody)
    trs=tbody.find_all('tr')
    # print(trs)
    movie_ranks=[]
    movie_name=[]
    year_of_realease=[]
    movie_urls=[]
    movie_ratings=[]
    for tr in trs:
        position=tr.find('td', class_='titleColumn').get_text().strip()
        # print(position)
        rank=''
        for i in position:
            if '.' not in i:
                rank=rank+i
            else:
                break
        movie_ranks.append(rank)
        # print(movie_ranks)
        title=tr.find('td', class_="titleColumn").a.get_text()
        # print(title)
        movie_name.append(title)
        # print(movie_name)
        year=tr.find('td', class_="titleColumn").span.get_text()
        # print(year)
        year_of_realease.append(year)
        # print(year_of_realease)
        imdb_rating=tr.find('td', class_="ratingColumn imdbRating").strong.get_text()
        print()
        movie_ratings.append(imdb_rating)

        link=tr.find('td' , class_="titleColumn").a['href']
        movie_link="https://www.imdb.com"+link
        movie_urls.append(movie_link)
        # print(movie_urls)
    top_list=[]
    i=0
    while i<len(movie_ranks):
        d1={}
        d1["name"]=str(movie_name[i])
        d1["year"]=int(year_of_realease[i][1:5])
        d1["position"]=int(movie_ranks[i])
        d1["rating"]=float(movie_ratings[i])
        d1["url"]=movie_urls[i]
        top_list.append(d1)
        i=i+1
    with open("imdb_movies.json","w") as f1:
        f2=json.dump(top_list,f1,indent=4)
    # pprint(top_list)
    return top_list
    # with open("rohoni.json","w") as f1:
    #     f2=json.dump(top_list,f1,indent=4)
pprint.pprint(scrap_top_list())