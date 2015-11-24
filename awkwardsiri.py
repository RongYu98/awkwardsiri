import urllib2, google, bs4, re

q="who played spiderman"
r = google.search(q,num=10,start=0,stop=10)
l=[]
for result in r:
    l.append(result)

u = urllib2.urlopen(l[0])
page = u.read()
#print page
soup = bs4.BeautifulSoup(page)
raw = soup.get_text()
#print raw

text = re.findall("[A-Z][a-z]+ [A-Z][a-z]+",raw)

file = open("20k.txt", "r")
words = file.read()
file.close()
content = words.split("\n") #content is now a list of strings of words
for word in content:
    word = word.lower()
for word in text:
    twoWords = word.split(" ")
    if ( (twoWords[0].lower() in content) or (twoWords[1].lower() in content) ):
        text.remove(word)
file = open("CommonWords.csv", "r")
words = file.read()
file.close()
content = words.split("\n") #content is now a list of strings of words
for word in content:
    word = word.lower()
for word in text:
    twoWords = word.split(" ")
    if ( (twoWords[0].lower() in content) or (twoWords[1].lower() in content) ):
        text.remove(word)



dict = {}
for name in text:
    if name in dict.keys():
        dict[name]+=1;
    else:
        dict[name]=1;


for key in sorted(dict):
    if dict[key]==1:
        dict.pop(key)
    else:
        print "%s: %s" % (key, dict[key])
#print dict
