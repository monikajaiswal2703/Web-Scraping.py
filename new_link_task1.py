import requests
import pprint,json
from bs4  import BeautifulSoup
"task1"
url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
page=requests.get(url)
# print(page)
soup=BeautifulSoup(page.text,'html.parser')
# pprint.pprint(soup)
def scape_top_list():
    main_div = soup.find('table',class_= "table")
    name=main_div.find_all("a",class_="unstyled articleLink")
    position = main_div.find_all('td',class_="bold") 
    rating=main_div.find_all("span",class_="tMeterIcon tiny")
    topMovie=[]
    details={'position':"",'name':"",'year':"",'rating':"",'url':""}
    def Dividename(a):
        b=a.split("(")
        # print(b)
        return b[0]
    for i in range(0,len(position)):
        movie_name=name[i].get_text()
        # print(n)
        a=name[i].get_text().strip()
        # print(a)
        r=Dividename(a)
        print(r)
        details['position'] = i+1
        details["name"]=r
        details['year'] = movie_name.split()[-1][1:5]
        details['rating'] = rating[i].get_text().strip()
        details['url'] = "https://www.rottentomatoes.com"+name[i]["href"]
        topMovie.append(details.copy())
        
        
        # pprint.pprint(topMovie)
    with open("movieData.json","w") as read:
        json.dump(topMovie,read,indent=4)
    return topMovie
scrapped=scape_top_list()

"task2"

def group_by_year(movies):
    years=[]
    for i in movies:
    #    print(movies)
        year=i['year']
        if year not in years:
           years.append(year)
    movie_dict={i:[]for i in years}
    # print(movie_dict)
    for i in movies:
        # print(i)
        year = i['year']
        # print(year)
        for x in movie_dict:
            # print(x)
            if str(x) ==  str(year):
                movie_dict[x].append(i)
        pprint.pprint(movie_dict)
    with open ("task2.json","w")as f:
        json.dump(movie_dict,f,indent=4)      
    return movie_dict
dec_arg=group_by_year(scrapped)


"task3"

def group_by_decade(movies):
    moviedec={}
    list1=[]
    for index in movies:
        mod = int(index)%10
        decade = int(index)-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10 = int(i)+9
        for x in movies:
            if int(x)<= dec10 and int(x)>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
                with open("task3.json","w")as f:
                    json.dump(moviedec,f,indent=4)
    return (moviedec)
print(group_by_decade(dec_arg))

"task4"




