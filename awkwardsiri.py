import urllib2, google, bs4, re

q="who played spiderman"
r = google.search(q,num=10,start=0,stop=10)
l=[]
for result in r:
    l.append(result)

#print l[0]

u = urllib2.urlopen(l[0])
page = u.read()
#print page
soup = bs4.BeautifulSoup(page)
raw = soup.get_text()
#print raw
text = re.findall("[A-Z][a-z]+ [A-Z][a-z]+",raw)
dict = {}
for name in text:
    if name in dict.keys():
        dict[name]+=1;
    else:
        dict[name]=1;

for key in sorted(dict):
    print "%s: %s" % (key, dict[key])
#print dict
