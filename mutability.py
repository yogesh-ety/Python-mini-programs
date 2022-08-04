#mutablity   = can be change
#example : list (elememts in the list can be changed ,removed ,delete...._)
         #: dictionaries ,orderdictionaries
#imutability = cannot be changed
#example : tuple (elements in the tuple cannot be changed ever , it remains constant throughout the code
         #: ints ,floats ,boolean


t = (1 ,2 ,3 ,[5 ,6 ,7])
print(t)

#t(0) = 9 --> this is not possible since tuple is immutable

t[3][0] = 8
print(t)
#list is mutable so there can be change

