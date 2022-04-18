
import re
# text = "The film, '@Pulp Fiction' was ? released _ in % $ year 1994."
# result = re.sub(r"[,@\'?\.$%_]", "", text, flags=re.I)
# print(result)

# text = "The film      Pulp Fiction      was released in   year 1994."
# result = re.sub(r"\s+"," ", text, flags = re.I)
# print(result)

# "split function use"
# text = "The film      Pulp   Fiction was released in year 1994      "
# result = re.split(r"\s+", text)
# print(result)

# text = "The film, Pulp Fiction, was released in year 1994"
# result = re.split(r"\,", text)
# print(result)



# import requests
# url="https://www.imdb.com/india/top-rated-indian-movies/"
# page=requests.get(url)
# print(page.text)
# pprint.pprint(page)

# soup=BeautifulSoup(page.text,'html.parser')
# soup.find('h1').get_text()

# print(soup)

# -mona = "my name is monika"
# print("m" in -mona)

# a=int(input('enter the number'))
# b=int(input('enetr the number'))
# c=int(input('enetr the number'))
# if a>b>c:
#     print(a,'a is second maximum')
# elif b<c>a:
#     print(b,'b is second maximum')
# else:
#     print(c,'c is maximum')