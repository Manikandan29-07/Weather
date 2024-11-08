# views.py
import requests
from django.shortcuts import render
from django.conf import settings

def get_movie_data(movie_title):
    api_key = "e771ac004ecb8bd40740087d16cb6958"
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
    response = requests.get(url)
    return response.json()

def movie_search(request):
    movie_data = None
    query = request.GET.get('movie_title')
    if query:
        movie_data = get_movie_data(query)
    
    return render(request, 'weather/movie_dashboard.html', {'movie_data': movie_data, 'query': query})
