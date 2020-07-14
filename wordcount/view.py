#from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    #return HttpResponse('Hello!!') #passing HTML code directly
    #return render(request,'home2.html',{'hithere':'This is me'}) #passing HTML code through a file
    return render(request,'home.html')

def count(request):
    text = request.GET['fulltext']
    #print(text)
    wordlist = text.split()
    worddictionary ={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    
    sorteddictionary=sorted (worddictionary.items(),
                             key=operator.itemgetter(1),
                             reverse=True)
        
    return render(request,
                  'count.html',
                  {"fulltext_len":len(wordlist),
                   "sorteddictionary":sorteddictionary})

def about(request):
    return render(request,'about.html')
    

