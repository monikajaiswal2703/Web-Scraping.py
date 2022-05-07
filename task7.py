import json
with open("task5_100movie.json","r") as file:
    data=json.load(file)
def analyse_movie_language(movie_list):
    language_list=[]
    list=[]
    for i in range(len(movie_list)):
        for j in range(len(movie_list[i]["Director"])):
            if movie_list[i]["Director"][j] not in language_list:
                language_list.append(movie_list[i]["Director"][j])
            list.append(movie_list[i]["Director"][j])
        # print(list)
    language_dict={i:""for i in language_list}
    for x,y in language_dict.items():
        count=0
        for i in range(len(list)):
            if x==list[i]:
                count+=1
                language_dict[x]=count
    print(language_dict)    
    with open("task7Director.json","w") as file:
        json.dump(language_dict,file,indent=4)
analyse_movie_language(data)