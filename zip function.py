list1 = [1 ,2 ,3 ,4 ,5]
list2 = ['one' ,'two' ,'three' ,'four' ,'five']

zipped = list(zip(list1 ,list2))
print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)

for (l1 ,l2) in zip(list1 ,list2):
    print(l1)
    print(l2)

fruits = ['apples' ,'orange' ,'banana']
counts = [2 ,3 ,6]
prices =[50 ,60 , 10]

sentences =[]

for (fruit ,count ,price) in zip(fruits ,counts ,prices):
    (fruit ,count ,price) = str(fruits) ,str(counts) ,str(prices)
    sentence = 'i bought ' + count + ' ' + fruit + ' ' + 'for' + price
    sentences.append(sentence)

print(sentences)