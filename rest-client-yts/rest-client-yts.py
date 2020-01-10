#!/usr/bin/env python3
# List latest good movies on YTS

from simple_rest_client.api import API
from simple_rest_client.resource import Resource
import progressbar


class MovieResource(Resource):
    actions = {
        'list': {'method': 'GET', 'url': 'list_movies.json'},
    }


def good(movie):
    return movie['rating'] >= 7.5


api = API(api_root_url='https://yts.am/api/v2')
api.add_resource(resource_name='movies', resource_class=MovieResource)

max_movies = 20
with progressbar.ProgressBar(max_value=max_movies) as bar:
    page = 0
    movies = []
    while len(movies) < max_movies and page < 20:
        page += 1
        movies_new = api.movies.list(params={'limit': 50, 'page': page}).body['data']['movies']
        movies_new = [movie for movie in movies_new if good(movie)]
        movies += movies_new
        bar.update(min(max_movies, len(movies)))

for movie in sorted(movies, key=lambda m: m['rating'], reverse=True):
    print('{rating:3.1f} {title}\n    {url}'.format(**movie))
