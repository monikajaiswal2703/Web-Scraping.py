import pprint
import requests
import json
from bs4 import BeautifulSoup
def get_movies_list_details(movie_list):
    with open("task1_movieData.json","r") as file:
        data=json.load(file)
        # print(data)
    for i in range(90,100):
        # print(i)
        url=requests.get(data[i]["url"])
        # print(url)
        htmlcontect=url.content
        # print(htmlcontect)
        dict={}
        soup=BeautifulSoup(htmlcontect,"html.parser")
        title_div=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip() 
        ul=soup.find("ul",class_="content-meta info")
        li=ul.find_all('li',class_='meta-row clearfix')
        h1=soup.find('h1',class_='scoreboard__title').get_text()
        dict.update({"movie name":h1})
        dict['Bio']=title_div
        # print(dict)
        for i in li:
            # print(i)
            key=i.find("div",class_="meta-label subtle").get_text().strip()
            # print(key)
            value=i.find("div",class_="meta-value").get_text().strip()
            dict.update({key:value})
            # print(dict)
        movie_list.append(dict)
    # pprint.pprint(movie_list)
    with open("task5_details.json","w") as file:
        json.dump(movie_list,file,indent=4)
get_movies_list_details([])

