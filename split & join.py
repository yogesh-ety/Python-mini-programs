lists = 'one, two, three, four, five'
problems = 'abc/ def? ghi, jkl>'
print(lists)

#  SPLITING THE ARRAY
l = lists.split(", ")
print(l)

m = problems.split("? ")
print(m)

#JOING STRING
c = ' and '.join(l)
print(c)

v = ' and '.join(m)
print(v)



