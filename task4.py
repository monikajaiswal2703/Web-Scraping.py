# import json
# import pprint
# from bs4 import BeautifulSoup
# import requests

# movie_detail=[]
# def scape_movie_details(movie_url):
#     d1={}
#     page=requests.get(movie_url)
#     soup=BeautifulSoup(page.text,'html.parser')
#     # return soup
#     d1['name']="Black panther"
#     # return(d1)
#     title_div=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
#     # print(title_div)
#     d1['Bio']=title_div
#     title=soup.find_all("div",class_="meta-label subtle")
#     # return(title)
#     value=soup.find_all("div",class_="meta-value")
#     # return value
#     for i in range(len(title)):
#         # return i
#         d1[str(title[i].get_text().strip())] = value[i].get_text().strip()
#     movie_detail.append(d1)
#     pprint.pprint (movie_detail)
#     with open("task4.json","w")as f:
#         json.dump(movie_detail,f,indent=4)
# print(scape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018"))



# a=[1,2,3]
# b=[4,5,6]
# s=""
# s1=""
# i=1
# while i<len(a)+1:
#     s+=str(a[-i])
#     s1+=str(b[-i])
#     i+=1
# print(s)
# print(s1)
# c=int(s)+int(s1)
# d=str(c)
# e=''
# for i in range(1,(len(d)+1)):
#     e+=d[-i]
# print(e)


# a=[[4,5,6],[6,7,8],[9,10],[4,5,6,7]]
# s=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if i==0:
#             s+=a[i][j]
#         if (len(a[i])-1)==j and i!=0:
#             s+=a[i][j]
#         j+=1
#     i+=1
# print(s)
