import urllib2, google, bs4, re

def finder(str):
    #q="who played spiderman"
    q = str
    r = google.search(q,num=10,start=0,stop=10)
    l=[]
    for result in r:
	print result
        l.append(result)
    dict = {}
    
    for i in range(0,11):
        try:
            print "------------"
            print l[i]
            u = urllib2.urlopen(l[i])
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
                #if ( (twoWords[0].lower() in content) or (twoWords[1].lower() in content) ):
                    #text.remove(word)
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

            file = open("names.csv", "r")
            names = file.read()
            file.close()
            content = names.split(",")
            for word in content:
                if word.lower in text:
                    print word
                    text.remove(word)
            
            for name in text:
                if name in dict.keys():
                    dict[name]+=1;
                else:        
                    dict[name]=1;

        except urllib2.HTTPError, e:
            print(e.code)
        except urllib2.URLError, e:
            print(e.args)

    return findmax(dict)




def findmax(dict):
    for key in sorted(dict):
        if dict[key] < 21:
            dict.pop(key)

    for key in sorted(dict):
        print "%s: %s" % (key, dict[key])

    max = 0;
    maxKey = ""
    for key in dict:
        if dict[key] > max:
            maxKey = key
	    max = dict[key]

    return "The answer is most likely: %s" % (maxKey)


#finder("who played spiderman")
#Sample Questions: 
#Where is Stuyvesant
#Who is  Mike Zamansky?
#Who is the strongest man alive?