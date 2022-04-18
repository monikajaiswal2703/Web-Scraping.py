
from textwrap import indent
import requests
import pprint
from bs4  import BeautifulSoup
url="https://www.imdb.com/india/top-rated-indian-movies/"
page=requests.get(url)
# print(page.text)
# pprint.pprint(page)

soup=BeautifulSoup(page.text,'html.parser')

def scape_top_list():
    main_div = soup.find('div',class_ = 'lister')
    tbody = main_div.find('tbody',class_='lister-list')
    trs = tbody.find_all('tr')
#     return trs
# print(scape_top_list())
    movie_ranks=[]
    movie_name=[]
    year_of_relesed=[]
    movie_urls=[]
    movie_rating=[]
    for tr in trs:
        position = tr.find('td',class_="titleColumn").get_text().strip()
        rank=''
        for i in position:
            if '.' not in i:
                rank+=i
            else:
                break
        movie_ranks.append(rank)
        title=tr.find('td',class_="titleColumn").a.get_text()
#         return title
# print(scape_top_list())
        movie_name.append(title)
#     return movie_name
# print(scape_top_list())

        year = tr.find('td',class_= "titleColumn").span.get_text()
#         return year
# print(scape_top_list())
        year_of_relesed.append(year)
#         return year_of_relesed
# print(scape_top_list())
        imdb_rating = tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
#         return imdb_rating
# print(scape_top_list())
        movie_rating.append(imdb_rating)
#         return movie_rating
# print(scape_top_list())
        link = tr.find('td',class_="titleColumn").a['href']
        movie_link="https://www.imdb.com"+link
        movie_urls.append(movie_link)
#         return movie_urls
# print(scape_top_list())
    Top_Movies = []
    details={'position':"",'name':"",'year':"",'rating':"",'url':""}
    for i in range(0,len(movie_ranks)):
        details['position'] = int(movie_ranks[i])
        details['name'] = str(movie_name[i])
        year_of_relesed[i] = year_of_relesed[i][1:5]
        details['year'] = int(year_of_relesed[i])
        details['rating'] = float(movie_rating[i])
        details['url'] = movie_urls[i]
        Top_Movies.append(details.copy())
    import json
    with open ("data1.json","w")as f:
        json.dump(Top_Movies,f,indent=4)      
    return Top_Movies
print(scape_top_list())
# import pprint
# pprint.pprint(scape_top_list())