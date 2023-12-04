import anime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import anime
from.  forms import AnimeForm

# Create your views here.
def index(request):
    Anime=anime.objects.all()
    context={
        'anime_list':Anime
    }
    return render(request,'index.html',context)
def detail(request,movieid):
    Anime=anime.objects.get(id=movieid)
    return render(request,'detail.html',{'Anime':Anime})
def add_anime(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        Anime = anime(name=name,desc=desc,year=year,img=img)
        Anime.save()
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    Anime=anime.objects.get(id=id)
    form=AnimeForm(request.POST or None,request.FILES,instance=Anime)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'Anime':Anime})
def delete(request,id):
    if request.method=="POST":
        Anime=anime.objects.get(id=id)
        Anime.delete()
        return redirect('/')
    return render(request,'delete.html')
