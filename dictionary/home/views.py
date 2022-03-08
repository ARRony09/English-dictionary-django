from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.
def index(request):
    return render(request,'index.html')

def word(request):
    search_query = request.GET["query"]
    dictionary=PyDictionary()
    #translate=dictionary.translate(search_query, "bn")
    meaning=dictionary.meaning(search_query)
    #synonyms=dictionary.synonym(search_query)
    #antonyms=dictionary.antonym(search_query)
    context ={
        "meaning":meaning["Noun"],
        }
    return render(request,"word.html",context)
    