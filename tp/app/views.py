from django.shortcuts import render
from .forms import LivreForm
from . import models
def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            livre = form.save() # sauvegarde dans la base
            return render(request,"app/affiche.html",{"livre" : livre}) #

        else:
            return render(request,"app/ajout.html",{"form": form})
    else :
        form = LivreForm() # création d'un formulaire vide
        return render(request,"app/ajout.html",{"form" : form})


def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"app/affiche.html",{"livre" : livre})
    else:
        return render(request,"app/ajout.html",{"form": lform})

def show(request):
    queryset = models.Livre.objects.all()  
    return render(request,"app/show.html",{"Livre" : queryset})


def read(request,id):
    print(id)
    queryset = models.Livre.objects.all()  
    return render(request,"app/showid.html",{"Livre" : queryset,'ID':id})