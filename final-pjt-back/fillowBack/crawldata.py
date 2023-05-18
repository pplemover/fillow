import requests
import json
import pandas as pd

TMDB_API_KEY = '6aee34be99bb1d1b3fa358b709332b7e'  # .env 파일에서 불러옴.

def get_movie_datas():
    total_data = []
    with open('checking.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    # for mv in json_data:
    #     print(mv['tmdb_id'])

    # 1페이지부터 3페이지까지의 데이터를 가져옴.
    for i in json_data:
        request_url = f"https://api.themoviedb.org/3/movie/{i['tmdb_id']}?api_key={TMDB_API_KEY}&language=ko-KR"
        print(request_url)
        movie = requests.get(request_url).json()
        # print(movie)

        # for movie in movies['results']:
        #         # Movie 모델 필드명에 맞추어 데이터를 저장함.
        data = {
            "model": "fillow.movie",
            "pk": movie['id'],
            'fields': {
                'title': movie['title'],
                'release_date': movie['release_date'],
                'popularity': movie['popularity'],
                'vote_avg': movie['vote_average'],
                'overview': movie['overview'],
                'poster_path': movie['poster_path'],
                'genres': movie['genres'],
                'vote_count': movie['vote_count'],
            },
        }
        total_data.append(data)

    # print(total_data)


    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=" ", ensure_ascii=False)


#==================================================================================================================================================================

def get_genre_datas():

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko"
    genres = requests.get(request_url).json()
    total_data = []
    for genre in genres['genres']:
        data = {
            "model": "fillow.genre",
            'pk': genre['id'],
            'fields': {
                "name": genre['name']
            },
        }
        total_data.append(data)



    with open("genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=" ", ensure_ascii=False)

#==================================================================================================================================================================
def edit_json():
    pass
    

get_movie_datas()
get_genre_datas()

# readcsv = pd.read_csv('helloworld.csv',engine='python',encoding='CP949')
# readcsv = pd.DataFrame(readcsv)
# readcsv.to_json(r'C:/Users/SSAFY/Desktop/fillow222/final-pjt-back/fillowBack/checking.json', force_ascii=False, indent=2, orient='records')

