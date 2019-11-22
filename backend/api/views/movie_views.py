# from rest_framework import status
# from rest_framework.decorators import api_view
# from api.models import Movie
# from api.serializers import MovieSerializer
# from rest_framework.response import Response


# @api_view(['GET', 'POST', 'DELETE'])
# def movies(request):

#     if request.method == 'GET':
#         # id = request.GET.get('id', request.GET.get('movie_id', None))
#         # title = request.GET.get('title', None)
#         # genres = request.GET.get('genres', None)
#         # sorting = request.GET.get('sorting', None)
#         # if genres =="All":
#         #     genres = None
#         movies = Movie.objects.all()
#         # if id:
#         #     movies = movies.filter(pk=id)
#         # if title:
#         #     movies = movies.filter(title__icontains=title)
#         # if genres:
#         #     movies = movies.filter(genres__icontains=genres)
#         # if sorting == "조회수 많은 순으로 보기":
#         #     movies = sorted(movies, key = lambda movie : movie.count, reverse=True)
#         # if sorting== "평점 높은순으로 보기":
#         #     movies = sorted(movies, key = lambda movie : movie.likes, reverse=True)

#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=10000)
#         movie.delete()
#         return Response(status=status.HTTP_200_OK)

#     if request.method == 'POST':
#         movies = request.data.get('movies', None)
#         print(movies)
#         for movie in movies:
#             id = movie.get('id', None)
#             title = movie.get('title', None)
#             genres = movie.get('genres', None)
#             likes = movie.get('likes', None)
#             count = movie.get('count', None)

#             if not (id and title and genres):
#                 continue
#             if Movie.objects.filter(id=id).count() > 0 or Movie.objects.filter(title=title).count() > 0:
#                 continue

#             Movie(id=id, title=title, genres='|'.join(genres), likes=likes, count=count).save()
#         print(Movie)
#         return Response(status=status.HTTP_200_OK)
