import requests
import json
import sqlite3
import random
import datetime

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": "731b735b0cmsh57b9761a93782bdp196090jsnd979c5b98aec",
	"X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

movies = response.json()

for movie in movies:
    print(movie.get('title', 'Unknown'))
    
    name = movie.get('title', 'Unknown')
    genre = movie.get('genre', 'Unknown')[0]
    year = movie.get('year', 'Unknown')
    description = movie.get('description', 'Unknown')
    rating = float(movie.get('rating', 'Unknown'))
    
    name = name.replace('"', "'")
    genre = genre.replace('"', "'")
    description = description.replace('"', "'")
    
    print(name, genre, year, description, rating)
    
    cursor.execute(f'INSERT INTO movie (name, genre, year, description, rating) VALUES ("{name}", "{genre}", {year}, "{description}", {rating})')
    connection.commit()


cinemas = [
    {
        'name' : 'Арман',
        'address' : '​Проспект Кабанбай батыр, 21'  
    },
    {
        'name' : 'Chaplin cinemas',
        'address' : '​Проспект Туран, 37'  
    },
    {
        'name' : 'Kinopark ',
        'address' : '​Проспект Туран, 24'  
    },
    {
        'name' : 'Евразия Cinema 7',
        'address' : '​Улица Алексея Петрова, 24а/1'  
    },
    {
        'name' : 'Арсенал ',
        'address' : '​Улица Ыбырай Алтынсарин, 4'  
    },
]

for cinema in cinemas:
    cursor.execute(f'INSERT INTO cinema (name, address) VALUES ("{cinema.get("name")}", "{cinema.get("address")}")')
    connection.commit()


start_date = datetime.date.today()
end_date = datetime.date(2024, 5, 30)
start_time = datetime.time(16, 0, 0)
end_time = datetime.time(0, 0, 0)
movies_id = [random.randint(1, 100) for i in range(1, 51)]
cinemas_id = [random.randint(1, 5) for i in range(1, 51)]
prices = [random.randint(1000, 5000) for i in range(1, 51)]
gap = int((end_date - start_date).total_seconds())
dates = [start_date + datetime.timedelta(seconds=random.randint(0, gap)) for i in range(1, 51)]
times = [f"{random.randint(16, 23)}:{random.randint(0, 5)}0:00" for i in range(1, 51)]
capacities = [random.randint(50, 100) for i in range(1, 51)]
for i in range(0, 50):
    cursor.execute(
        f'INSERT INTO afisha (movie_id, cinema_id, price, date, time, capacity) VALUES ({movies_id[i]}, {cinemas_id[i]}, {prices[i]}, "{dates[i]}", "{times[i]}", {capacities[i]})'
    )
    connection.commit()

afishas = [i for i in range(1, 51)]
rooms = [random.randint(1, 6) for i in range(1, 51)] 
rows = [random.randint(1, 16) for i in range(1, 51)]
columns = [random.randint(1, 16) for i in range(1, 51)]

for i in range(0, 50):
    cursor.execute(
        f"INSERT INTO place (afisha_id, room, row, seat) VALUES ({afishas[i]}, {rooms[i]}, {rows[i]}, {columns[i]})"
    )
    connection.commit()