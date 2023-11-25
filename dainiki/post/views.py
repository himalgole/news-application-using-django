from django.shortcuts import render
from .models import post,front

def home(req):
    snapshots = post.objects.all().values()
    data = {
        'posts':snapshots
    }
    return render(req,'home.html',data)

def readdainiki(req,id):
    snapshot = post.objects.get(id = id)
    snapshots = post.objects.all().values()
    data = {
        'posts':snapshots,
        'post': snapshot,
        'current':snapshot
    }
    return render(req,'readdainiki.html',data)