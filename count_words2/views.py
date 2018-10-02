from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')

def count(request):
     texto=request.GET['fullt']
     arreglo =texto.split()
     dicionario={}
     for palabra in arreglo:
         if palabra in dicionario:
             dicionario[palabra]+=1
         else:
            dicionario[palabra]=1

     ordenado=sorted(dicionario.items())

     return render(request , 'count.html',{'texto':texto, 'arreglo':len(arreglo),'dicionario':ordenado})
def about(request):
    return render(request, 'about.html')
