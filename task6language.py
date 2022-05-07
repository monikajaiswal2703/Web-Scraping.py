import json
with open("task5_100movie.json","r") as file:
    data=json.load(file)
def analyse_movie_language(movie_list):
    language_list=[]
    list=[]
    for i in range(len(movie_list)):
        for j in range(len(movie_list[i]["Original Language"])):
            if movie_list[i]["Original Language"][j] not in language_list:
                language_list.append(movie_list[i]["Original Language"][j])
            list.append(movie_list[i]["Original Language"][j])
        # print(list)
    language_dict={i:""for i in language_list}
    # print(language_dict)
    for x in language_dict.items():
        # print(x)
        count=0
        for i in range(len(list)):
            # print(list[i])
            if x==list[i]:
                count+=1
                language_dict[x]=count
    print(language_dict)    
    with open("task6.json","w") as file:
        json.dump(language_dict,file,indent=4)
analyse_movie_language(data)