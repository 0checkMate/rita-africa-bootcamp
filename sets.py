#creating a set of favourite movies
movie_set = {'cars 1', 'cars 2', 'cars 3'}
print(movie_set)

#adding a movie to the set
movie_set.add('cars 4')
print(movie_set)

#adding three additional movies
movie_set.update(['cars 5', 'cars 6', 'cars 7'])
print(movie_set)

#removing a movie from the set
movie_set.pop()
print(movie_set)

#checking for a specific movie in the set
if 'cars 1' in movie_set:
    print('Get some popcorn!')
else:
    print('Maybe grab a book')