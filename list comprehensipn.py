names = ['yogesh' ,'ety' ,'preethi' ]
print(names)
print()

l = []

for perosn in names:
    l.append(perosn)
print(l)
print()

#list comprehension

print([person for person in names])
print()


l = []

for perosn in names:
    l.append(perosn + 'abcd')
print(l)
print()

#list comprehension

print([person + 'abcd' for person in names])
print()

l = []
movie_and_ratings = {"dark knight" :9 ,"harry p0tter" :8 ,"50 shades" :4 , "50 shades darker" :2}
print(movie_and_ratings)

for movies in movie_and_ratings:
    if movie_and_ratings[movies] > 7:
        l.append(movies)

print(l)

#list comprehension
print([ movie for movie in movie_and_ratings if movie_and_ratings[movie]>7 ])