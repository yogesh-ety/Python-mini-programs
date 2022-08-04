import re

text = "my name is ety , i m six feet tall"

pattern = re.compile("i m six feet tall")

result = pattern.search(text)
print(result)


#for single letter match
#terminates after finding the 1st match even though there are matches upcoming



pattern = re.compile("[LMI]")
patter = re.compile("[a-zA-Z]") #A-Z and a-z means here fiding all the aphabets match
result1 = patter.search(text)
result = pattern.search(text)
print(result)
print(result1)


#for matching one and more

text = "random26536 pattern "

pattern = re.compile("[rndmoa]+")
patter = re.compile("[a-zA-Z]+")
patt = re.compile("[1-9]+")

#A-Z and a-z means here fiding all the aphabets match
#terminates the matching process when there is a space
result1 = patter.search(text)
result2 = patt.search(text)
result = pattern.search(text)
print(result)
print(result1)
print(result2)


#matching the mail aadress
text = "my email is thenameis123@gmail.com yeah "
patt =re.compile("[a-zA-Z0-9]+\@[A-Za-z]+\.[a-zA-Z]+")
result3 = patt.search(text)
print(result3)



#to find one or more mail adresses


text = "my email is thenameis123@gmail.com yeah the next mail is companyname@gamail.com "
pat =re.compile("[a-zA-Z0-9]+\@[A-Za-z]+\.[a-zA-Z]+")
result4 = pat.findall(text)
print(result4)

